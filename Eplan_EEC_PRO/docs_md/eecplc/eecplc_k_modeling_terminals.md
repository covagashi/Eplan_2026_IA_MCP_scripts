---
title: "Connections"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_modeling_terminals.htm"
file: "eecplc_k_modeling_terminals"
category: "eecplc"
---

# Connections

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Connections

The modeling of connection points for controller components is analogous to the modeling of connection points for sensors and actuators (see [Connection points for actuators and sensors](eecplc_k_modeling_sensors_actuators_terminals.htm)). However, formulas for calculating the addresses must also be provided. Connections with a <null> formula result are ignored by the IO generator. This can be used to intentionally disable connections, for example, when dealing with cards whose connections can optionally be configured as either input or output. The addresses are not calculated automatically by the IO generator, in order to ensure that particularities can be reacted to flexibly when allocating addresses to individual connections, for example, the non-alphabetical address sequence in ET200X assemblies (x.0, x.4, x.1, x.5, x.2, x.6, x.3, x.7). The connection addresses are calculated based on the input or output start address. It should be noted that the start addresses contain no symbol for specifying the type of address (e.g. %IX for binary addresses in IEC 61131-3 format). These should be integrated into the formula for the connection address.

An example of such a formula is ='%IX'+$$InputStartAddress.byteAddressAdd(3). The section on [PLC address methods](refformulas_r_plc_methods.htm) documents the methods that can be used for this purpose.
