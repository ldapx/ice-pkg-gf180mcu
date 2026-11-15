#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Regenerate ``layout/devices.json`` for the GF180MCU package.

Run from the package root with the ICE Python bindings available:

    PYTHONPATH=<ice>/build/linux/x86_64/release:<ice>/python \
        python3 layout/generate_devices.py
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import pcells  # noqa: E402


def build_library(package_root: Path) -> dict:
    try:
        from icepy import pcells as runtime
    except ImportError as error:
        raise SystemExit(
            "icepy is required to regenerate the GF180MCU device library. "
            "Build the icepy target and set PYTHONPATH to its directory."
        ) from error

    cells = []
    for implementation in pcells.PCELLS:
        geometry = runtime.generate_package_geometry(
            package_root, "pcells", implementation.__name__
        )
        cells.append(
            {
                "name": implementation.name,
                "category": implementation.category,
                "source": "layout/pcells.py",
                "bounds": geometry["bounds"],
                "shapes": geometry["shapes"],
                "ports": geometry.get("ports", []),
                "parameters": [dict(spec) for spec in implementation.parameters],
                "generator": {
                    "module": "pcells",
                    "class": implementation.__name__,
                },
            }
        )

    stream_specs = list(pcells.LAYERS.values()) + list(
        getattr(pcells, "EXTRA_LAYER_STREAMS", [])
    )
    streams = {}
    for spec in stream_specs:
        if len(spec) == 2:
            label, number = spec
            datatype = 0
        else:
            label, number, datatype = spec
        streams[(int(number), int(datatype))] = {
            "name": str(label),
            "number": int(number),
            "datatype": int(datatype),
        }
    layers = [streams[key] for key in sorted(streams)]

    return {
        "format": "ice-layout-device-library",
        "schema_version": 2,
        "name": "GlobalFoundries GF180MCU",
        "pdk": pcells.PDK,
        "cell_prefix": "GF180 ",
        "layers": layers,
        "cells": cells,
    }


def _slugify(name: str) -> str:
    value = re.sub(r"[^A-Za-z0-9._-]+", "_", name.strip())
    return value.strip("._-") or "device"


def write_library(library: dict, output: Path) -> None:
    """Write the index plus one ``.icelay`` file per device."""
    device_dir = output.parent / "devices"
    device_dir.mkdir(parents=True, exist_ok=True)
    for existing in device_dir.glob("*.icelay"):
        existing.unlink()
    used: set[str] = set()
    cells = []
    for cell in library["cells"]:
        slug = _slugify(cell["name"])
        candidate = slug
        suffix = 2
        while candidate.lower() in used:
            candidate = f"{slug}_{suffix}"
            suffix += 1
        used.add(candidate.lower())
        relative = f"devices/{candidate}.icelay"
        payload = {
            "format": "ice-layout",
            "schema_version": 2,
            "device": {
                "name": cell["name"],
                "category": cell.get("category", ""),
                "source": cell.get("source", ""),
                "pdk": library.get("pdk", ""),
                "bounds": cell["bounds"],
                "shapes": cell["shapes"],
                "ports": cell.get("ports", []),
                "parameters": cell.get("parameters", []),
                "generator": cell.get("generator"),
            },
        }
        (output.parent / relative).write_text(
            json.dumps(payload, separators=(",", ":")) + "\n"
        )
        cells.append(
            {
                "name": cell["name"],
                "category": cell.get("category", ""),
                "source": cell.get("source", ""),
                "layout": relative,
            }
        )
    library = dict(library)
    library["cells"] = cells
    output.write_text(json.dumps(library, separators=(",", ":")) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "devices.json",
        help="Output library path (default: layout/devices.json)",
    )
    args = parser.parse_args()
    package_root = HERE.parent
    library = build_library(package_root)
    write_library(library, args.output)
    print(f"Wrote {args.output} and {len(library['cells'])} .icelay device files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
