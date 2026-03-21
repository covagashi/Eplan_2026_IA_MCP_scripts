---
title: "Address formats"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_modeling_address_format.htm"
file: "eecplc_k_modeling_address_format"
category: "eecplc"
---

# Address formats

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Address formats

The parameter for the input start-address format and the parameter for the output start-address format serve to control how the IO generator defines the bit of the start addresses and the byte for byte-based addressing or the word for word-based addressing (see section 0).

When entering the start address format, the rules for the byte or word are separated by periods (for example, x.0). The following symbols may be used in the process:

    1. Integers for specifying constant parts of the start address,
    2. x for indicating variable parts of the start address, and
    3. | for describing alternatives (or-operation).

Frequently used start-address formats include:

    4. x.0 the byte of the start address may be freely chosen by the IO generator. All start addresses begin with the bit 0.
    5. x.1 the byte of the start address may be freely chosen by the IO generator. All start addresses begin with the bit 1.
    6. x.0|4 the byte of the start address may be freely chosen by the IO generator. All start addresses begin with the bit 0 or 4. This format is used, for example, when addressing the ASI buses.

The name of the parameter for the start address format can be changed via the (Model > Model variables menu) Disciplines > Fieldbus > Parameter for the input start-address format or Parameter for the output start-address format model variables.
