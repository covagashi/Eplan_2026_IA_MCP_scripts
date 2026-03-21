---
title: "Reserved bits"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_modeling_occupied_bits.htm"
file: "eecplc_k_modeling_occupied_bits"
category: "eecplc"
---

# Reserved bits

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Reserved bits

The parameter for the size of the input block and the parameter for the size of the output block can be used to regulate how many bits the IO generator is supposed to reserve for the controller components. The value of this parameter should be at least as large as the actual number of bits required, for example 32, for a bus coupler with 32 binary connections. To create reserves, however, the parameter can also be assigned a larger value; for example, if a free byte is to remain after each bus coupler, a value of 40 should be assigned for a bus coupler with 32 binary inputs.

The name of the parameter for the reserved bits can be changed via the (Model > Model variables menu) Disciplines > IO generator > Name of the parameter for the input block size or Name of the parameter for the output block size model variables.
