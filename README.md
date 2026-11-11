# GlobalFoundries GF180MCU package

This package provides the GlobalFoundries GF180MCU 180 nm CMOS open-source PDK
definition for ICE. It is self-contained for simulation and the 9-track 5 V
digital implementation flow; it does not require Volare, CIEL, `PDK_ROOT`, or
an external OpenROAD-flow-scripts checkout.

The package contains:

- the GF180MCU ngspice simulation subset under `libs.tech/ngspice`
  (`design.ngspice` and `sm141064*.ngspice`);
- the 9-track, 5 V standard-cell implementation set under `implementation/`
  (technology/cell LEF, Liberty, OpenRCX rules, and a tapcell hook for all four
  metal stacks).

## PDK metadata

The package declares the GF180MCU drawing and routing layers in `package.toml`
under `[pdk]`. ICE uses these layers when the package technology is activated
for a project. The default schematic name is `gf180mcu_top`.

## Schematic symbols

The package ships sidecar definitions for core GF180MCU devices:

- 3.3 V and 6.0 V NMOS/PMOS
- 5 x 5 um NPN
- 3.3 V diode
- 2k poly resistor
- 2.0 fF/um2 MIM capacitor

The sidecars reference ICE's shared artwork with `generic:<file>.svg`, so the
package does not include duplicate SVG files.

## Layout PCells

The package ships ICE-native PCell replicas under `layout/`:

- `layout/pcells.py` implements the GF180MCU PCell families with the
  `icepy.pcells` layout builder API (MOS, BJT, MOS/MIM capacitors, diodes, and
  the full poly/diffusion/well/metal resistor family).
- `layout/devices.json` is the generated ICE layout device library used by the
  Devices panel. It contains default geometry, parameter metadata, and
  generator bindings.
- `layout/device_generator.py` regenerates geometry when a parameter changes.
- `layout/generate_devices.py` rebuilds the library from the PCell definitions.

The device library also records the GF180MCU purpose datatypes: `dummy`
(4), `label` (10), `slot` (3), and `block` (5) for the metal layers. ICE groups
these under their base layer number and keeps non-drawing purposes hidden by
default.

The PCells do not require KLayout, Volare, CIEL, or `PDK_ROOT`. Regenerate the
library after editing `layout/pcells.py`:

```text
PYTHONPATH=<ice>/build/linux/x86_64/release:<ice>/python \
  python3 layout/generate_devices.py
```

## Physical implementation

`package.toml` declares explicit per-stack implementation data for the
9-track, 5 V standard-cell library:

- `implementation/lef/` — technology and cell LEF for 3LM, 4LM, 5LM, and 6LM
  stacks;
- `implementation/lib/` — `gf180mcu_fd_sc_mcu9t5v0` `tt_025C_5v00` Liberty;
- `implementation/rcx/` — OpenRCX extraction rules for each stack;
- `implementation/tapcell.tcl` — tapcell/endcap insertion hook.

The default stack is `5LM_1TM`; the default corner is `tt`. No
`OPENROAD_FLOW_SCRIPTS` environment variable is needed.

## Simulation

The package declares `[pdk.simulation]` in `package.toml`: `design.ngspice`,
`sm141064.ngspice`, section `typical`, and the GF180MCU NMOS/PMOS device names.
Verify with `ice-cli pdk-info gf180mcuA --probe`.
