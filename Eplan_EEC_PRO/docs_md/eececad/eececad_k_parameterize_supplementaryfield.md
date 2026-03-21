---
title: "Supplementary fields"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_parameterize_supplementaryfield.htm"
file: "eececad_k_parameterize_supplementaryfield"
category: "eececad"
---

# Supplementary fields

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Supplementary fields

The values of supplementary fields can be transferred by means of parameters of the type Map. The name of the parameter has the following syntax:

PropId_<Property ID>

The values are transferred as key-value pairs, whereby the key corresponds to the index of the user supplementary field and the value corresponds to the value of the supplementary field.

### [Example](javascript:void\(0\);)

    1. Create a parameter of the type Map with the name PropId_10901.
    2. Add the parameter to the discipline component of the WiringDiagram type.
    3. Enter the value =Map{Pair{'1','110 VAC'},Pair{'2','230 VAC'},Pair{'3','400 VAC'}} for the parameter.
    4. Generate the schematic.

In Eplan Electric P8 the result for the project properties looks as follows:

Property name | Value  
---|---  
Supplementary field [1] | 110 VAC  
Supplementary field [2] | 230 VAC  
Supplementary field [3] | 400 VAC
