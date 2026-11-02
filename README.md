# GlobalFoundries GF180MCU package

This package provides the GlobalFoundries GF180MCU 180 nm CMOS open-source PDK
definition for ICE. It points to the upstream PDK repository:

<https://github.com/google/gf180mcu-pdk>

The package also contains the GF180MCU ngspice simulation subset under
`libs.tech/ngspice` (`design.ngspice` and `sm141064*.ngspice`). Simulation
depends only on this ICE package, not on Volare, CIEL, or `PDK_ROOT`.

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

## Simulation

The package declares `[pdk.simulation]` in `package.toml`: `design.ngspice`,
`sm141064.ngspice`, section `typical`, and the GF180MCU NMOS/PMOS device names.
Verify with `ice-cli pdk-info gf180mcuA --probe`.
