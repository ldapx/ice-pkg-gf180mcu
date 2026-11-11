# Implementation data attribution

The files under `implementation/lef`, `implementation/lib`,
`implementation/rcx`, and `implementation/tapcell.tcl` are derived from the
GF180MCU open-source PDK and the OpenROAD-flow-scripts GF180 platform.

- GF180MCU PDK: https://github.com/google/gf180mcu-pdk (Apache-2.0)
- OpenROAD-flow-scripts: https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts (Apache-2.0)

They are bundled with this ICE package so the physical implementation flow does
not depend on an external `OPENROAD_FLOW_SCRIPTS` checkout.
