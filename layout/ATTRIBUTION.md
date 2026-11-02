# Layout PCell attribution

The PCell definitions in `pcells.py` are ICE-native replicas of the
GlobalFoundries GF180MCU device generators. Layer numbers, device names, and
parameter families follow the open-source GF180MCU PDK:

- Project: GF180MCU PDK
- Source: https://github.com/google/gf180mcu-pdk
- License: Apache-2.0

The geometry is produced entirely by the ICE `icepy.pcells` layout builder.
`devices.json` is generated from these definitions and contains default
parameter values and flattened polygons for the Devices panel.
