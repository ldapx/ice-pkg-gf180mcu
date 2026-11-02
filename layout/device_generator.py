#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""GF180MCU PCell generator for ICE.

ICE invokes this script with:

    device_generator.py --pdk-root <package> --module pcells --class nmos \
                        --params-file params.json --output geometry.json

The actual device implementations live in ``layout/pcells.py`` and use the
``icepy`` layout builder API shipped with ICE.
"""

from __future__ import annotations

import sys


def main() -> int:
    try:
        from icepy import pcells
    except ImportError as error:
        print(
            "The GF180MCU PCell generator requires the ICE icepy Python module. "
            f"Set PYTHONPATH to the ICE Python/build directories. ({error})",
            file=sys.stderr,
        )
        return 2
    return pcells.package_main_cli()


if __name__ == "__main__":
    raise SystemExit(main())
