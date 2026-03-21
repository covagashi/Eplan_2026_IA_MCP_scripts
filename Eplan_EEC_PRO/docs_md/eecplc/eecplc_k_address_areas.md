---
title: "Address spaces"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_address_areas.htm"
file: "eecplc_k_address_areas"
category: "eecplc"
---

# Address spaces

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Address spaces

Before the modeling of specific controller components can begin, it has to be decided whether the controller to be modeled should be equipped with separate or shared address spaces for inputs and outputs:

     * separate address spaces: It is possible, for example, for there to be both an input with an address of 1.0 and an output with an address of 1.0.
     * common address space: If, for example, there is an input with an address of 1.0, there cannot be an output with an address of 1.0.

When modeling controller components with a shared address space, it has to be decided which of the two predefined address spaces (input or output space) should be used for addressing (see also the section on [Connections](eecplc_k_modeling_terminals.htm)). If, for example, the input address space is selected, the outputs will also be assigned to this address space when modeling the common address space.

Which address area a controller component occupies is determined by the presence of the parameter for the input start-address or the parameter for the output start-address. A controller component can also have both parameters, provided it possesses both input and output connections.

Control components without parameters for both the input and output start-address are not taken into account by the IO generator.

The name of the parameter for start addresses can be changed via the (Model > Model variables menu) Disciplines > IO generator > Name of the parameter for the input start-address or Name of the parameter for the output start-address model variable.
