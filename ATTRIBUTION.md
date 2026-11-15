# Attribution

This package bundles data from the GF180MCU open-source PDK ecosystem.

- GlobalFoundries GF180MCU PDK: https://github.com/google/gf180mcu-pdk
  (Apache-2.0)
- OpenROAD-flow-scripts GF180 platform:
  https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts (Apache-2.0)

The package's `LICENSE` is Apache-2.0. Directory-level details are recorded in:

- `layout/ATTRIBUTION.md` — PCell definitions and the device index.
- `implementation/ATTRIBUTION.md` — standard-cell, stack, RCX, and script data.

The device geometry is produced by ICE's `icepy.pcells` layout builder from the
package-local PCell definitions; no KLayout or global PDK installation is
required.
