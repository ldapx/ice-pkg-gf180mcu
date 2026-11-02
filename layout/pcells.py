"""GlobalFoundries GF180MCU PCells implemented with the ICE layout API.

The classes in this module are package-local replicas of the GF180MCU device
PCells. They only depend on ``icepy.pcells`` (the ICE layout builder runtime),
so ICE can generate, edit, and preview them without KLayout or a global PDK
installation.
"""

from __future__ import annotations

from icepy import pcells


PDK = "gf180mcuA"

LAYERS = {
    "dnwell": ("dnwell", 12),
    "nwell": ("nwell", 21),
    "pwell": ("lvpwell", 204),
    "diff": ("comp", 22),
    "poly": ("poly2", 30),
    "nplus": ("nplus", 32),
    "pplus": ("pplus", 31),
    "contact": ("contact", 33),
    "met1": ("metal1", 34),
    "met2": ("metal2", 36),
    "met3": ("metal3", 42),
    "met4": ("metal4", 46),
    "met5": ("metal5", 81),
    "metaltop": ("metaltop", 53),
    "pad": ("pad", 37),
    "res": ("resistor", 62),
    "fusetop": ("fusetop", 75),
}


def parameter(name: str, value: str, description: str) -> dict[str, str]:
    return {"name": name, "value": value, "description": description}


MOS_PARAMETERS = [
    parameter("volt", "3.3V", "Operating voltage"),
    parameter("w", "1u", "Width"),
    parameter("l", "0.28u", "Length"),
    parameter("ld", "0.44u", "Diffusion length"),
    parameter("nf", "1", "Number of fingers"),
    parameter("grw", "0.36u", "Guard ring width"),
    parameter("bulk", "None", "Bulk connection"),
    parameter("deepnwell", "false", "Deep NWELL"),
    parameter("pcmpgr", "false", "Deep NWELL guard ring"),
]

RESISTOR_PARAMETERS = [
    parameter("model", "ppolyf_u_2k", "Device model"),
    parameter("w", "0.5u", "Width"),
    parameter("l", "2u", "Length"),
    parameter("resistance", "2k", "Target resistance"),
]

CAP_PARAMETERS = [
    parameter("model", "cap_mim_2f0fF", "Device model"),
    parameter("w", "2u", "Plate width"),
    parameter("h", "2u", "Plate height"),
    parameter("l", "2u", "Plate length"),
]

DIODE_PARAMETERS = [
    parameter("model", "diode_nd2ps_03v3", "Device model"),
    parameter("w", "2u", "Anode width"),
    parameter("h", "2u", "Anode height"),
]

BJT_PARAMETERS = [
    parameter("model", "npn_05p00x05p00", "Device model"),
    parameter("w", "1u", "Base width"),
    parameter("l", "1u", "Base length"),
]


class _GfPcell(pcells.PackagePcell):
    pdk = PDK
    layers = LAYERS


class nmos(_GfPcell):
    name = "nmos"
    category = "Transistors"
    family = "mos"
    parameters = MOS_PARAMETERS


class pmos(_GfPcell):
    name = "pmos"
    category = "Transistors"
    family = "mos"
    pmos = True
    parameters = MOS_PARAMETERS


class nmos_6p0_nat(_GfPcell):
    name = "nmos_6p0_nat"
    category = "Transistors"
    family = "mos"
    parameters = [
        parameter("volt", "6V", "Operating voltage"),
        *MOS_PARAMETERS[1:],
    ]


class nmos_10p0_asym(_GfPcell):
    name = "nmos_10p0_asym"
    category = "Transistors"
    family = "mos"
    parameters = [
        parameter("volt", "10V", "Operating voltage"),
        *MOS_PARAMETERS[1:],
    ]


class pmos_10p0_asym(_GfPcell):
    name = "pmos_10p0_asym"
    category = "Transistors"
    family = "mos"
    pmos = True
    parameters = [
        parameter("volt", "10V", "Operating voltage"),
        *MOS_PARAMETERS[1:],
    ]


class npn_bjt(_GfPcell):
    name = "npn_bjt"
    category = "Bipolar"
    family = "bjt"
    doping = "n"
    parameters = BJT_PARAMETERS


class pnp_bjt(_GfPcell):
    name = "pnp_bjt"
    category = "Bipolar"
    family = "bjt"
    doping = "p"
    parameters = [
        parameter("model", "vpnp_05p00x05p00", "Device model"),
        *BJT_PARAMETERS[1:],
    ]


class _GfResistor(_GfPcell):
    category = "Passives"
    family = "resistor"


class metal_resistor(_GfResistor):
    name = "metal_resistor"
    body_layer = "met1"
    doping = ""
    parameters = RESISTOR_PARAMETERS


class nplus_s_resistor(_GfResistor):
    name = "nplus_s_resistor"
    body_layer = "diff"
    doping = "n"
    parameters = RESISTOR_PARAMETERS


class pplus_s_resistor(_GfResistor):
    name = "pplus_s_resistor"
    body_layer = "diff"
    doping = "p"
    parameters = RESISTOR_PARAMETERS


class nplus_u_resistor(_GfResistor):
    name = "nplus_u_resistor"
    body_layer = "diff"
    doping = "n"
    parameters = RESISTOR_PARAMETERS


class pplus_u_resistor(_GfResistor):
    name = "pplus_u_resistor"
    body_layer = "diff"
    doping = "p"
    parameters = RESISTOR_PARAMETERS


class nwell_resistor(_GfResistor):
    name = "nwell_resistor"
    body_layer = "nwell"
    doping = "n"
    parameters = RESISTOR_PARAMETERS


class pwell_resistor(_GfResistor):
    name = "pwell_resistor"
    body_layer = "pwell"
    doping = "p"
    parameters = RESISTOR_PARAMETERS


class npolyf_s_resistor(_GfResistor):
    name = "npolyf_s_resistor"
    body_layer = "poly"
    doping = "n"
    parameters = RESISTOR_PARAMETERS


class ppolyf_s_resistor(_GfResistor):
    name = "ppolyf_s_resistor"
    body_layer = "poly"
    doping = "p"
    parameters = RESISTOR_PARAMETERS


class npolyf_u_resistor(_GfResistor):
    name = "npolyf_u_resistor"
    body_layer = "poly"
    doping = "n"
    parameters = RESISTOR_PARAMETERS


class ppolyf_u_resistor(_GfResistor):
    name = "ppolyf_u_resistor"
    body_layer = "poly"
    doping = "p"
    parameters = RESISTOR_PARAMETERS


class ppolyf_u_high_Rs_resistor(_GfResistor):
    name = "ppolyf_u_high_Rs_resistor"
    body_layer = "poly"
    doping = "p"
    parameters = [
        parameter("model", "ppolyf_u_high_Rs_2k", "Device model"),
        *RESISTOR_PARAMETERS[1:],
    ]


class _GfMoscap(_GfPcell):
    category = "Passives"
    family = "var_cap"
    parameters = CAP_PARAMETERS


class nmoscap(_GfMoscap):
    name = "nmoscap"


class pmoscap(_GfMoscap):
    name = "pmoscap"
    pmos = True


class nmoscap_b(_GfMoscap):
    name = "nmoscap_b"


class pmoscap_b(_GfMoscap):
    name = "pmoscap_b"
    pmos = True


class mimcap(_GfPcell):
    name = "mimcap"
    category = "Passives"
    family = "mim_cap"
    cap_bottom = "met4"
    cap_top = "metaltop"
    parameters = CAP_PARAMETERS


class _GfDiode(_GfPcell):
    category = "Diodes"
    family = "diode"
    doping = "n"
    parameters = DIODE_PARAMETERS


class np_diode(_GfDiode):
    name = "np_diode"


class pn_diode(_GfDiode):
    name = "pn_diode"
    doping = "p"


class nwp_diode(_GfDiode):
    name = "nwp_diode"


class dnwpw_diode(_GfDiode):
    name = "dnwpw_diode"


class dnwps_diode(_GfDiode):
    name = "dnwps_diode"


class sc_diode(_GfDiode):
    name = "sc_diode"


PCELLS = [
    nmos,
    pmos,
    nmos_6p0_nat,
    nmos_10p0_asym,
    pmos_10p0_asym,
    npn_bjt,
    pnp_bjt,
    metal_resistor,
    nplus_s_resistor,
    pplus_s_resistor,
    nplus_u_resistor,
    pplus_u_resistor,
    nwell_resistor,
    pwell_resistor,
    npolyf_s_resistor,
    ppolyf_s_resistor,
    npolyf_u_resistor,
    ppolyf_u_resistor,
    ppolyf_u_high_Rs_resistor,
    nmoscap,
    pmoscap,
    nmoscap_b,
    pmoscap_b,
    mimcap,
    np_diode,
    pn_diode,
    nwp_diode,
    dnwpw_diode,
    dnwps_diode,
    sc_diode,
]
