---
title: "Creating parameters in ECAD macro"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_create_parameter_in_macros.htm"
file: "eececad_k_create_parameter_in_macros"
category: "eececad"
---

# Creating parameters in ECAD macro

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Creating parameters in ECAD macro

Parameters can be defined only on symbol properties that are captured by a placeholder object. For example, it is not possible to define the variant of the symbol or the property Main function as a parameter. The following figure shows what a parameter may look like for the technical characteristic of a device:

The parameter name can generally be chosen freely. When choosing a name, it should be kept in mind that the same parameter name should always be used for the same task, where possible, including in various macros, in order to avoid an excessive number of parameters.

If a parameter name is preceded by "hidden_" (for example "hidden_Order"), the parameter value is not visible in a created schematic. The invisible parameter value is still available in the Eplan Electric P8, for example for calculations.

When it comes to the placing of the placeholder object, a suitable position near the affected graphic should be selected. The following figure shows what the parameters for a device in a placeholder object look like:

When generating the window macro keep in mind that the placeholder object is part of the macro content. Otherwise, no variables will be defined in the macro. If text objects for Plug and / or Socket are also defined in the same macro, note that these texts must **not** be assigned to the placeholder object! But they do have to be included in the macro graphic.

During the generation of the schematic with EEC, the parameter is replaced by the value defined or calculated in EEC.
