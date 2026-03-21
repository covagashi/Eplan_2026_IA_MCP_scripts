---
title: "Replace parameters"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_replace_parameter.htm"
file: "eecplc_k_replace_parameter"
category: "eecplc"
---

# Replace parameters

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Replace parameters

Replace parameters are used to replace, resp. insert parts of code whilst creating. The opening and closing tokens are specified in the text discipline configuration or respectively in the settings for the PLC disciplines (e.g. opening token = "M8B_" closing token = "_M8E"). The tokens must be defined in a way, that no conflicts with existing names in the text, which is to generate, appear (e.g. < as the opening token in XML documents). The text between the tokens appears in the interface as parameter. The parameter for the PLC disciplines is declared by the variable type REPLACE.

When the code is imported into a new discipline component to be created, the name of the Replace parameter is read out and a parameter with the same name is created that is allocated to the discipline component. Optionally, in addition to the name, also the type and the default value can be defined.

### [Example code](javascript:void\(0\);)
    
        // M8B_String:TestParam1=TestValue1_M8E

This code creates a parameter of type String with the name TestParam1 and the default value TestValue1.

### [Example for action component](javascript:void\(0\);)

Structure of the CoDeSys resource:

Replace marking within the action component Action1:

This results in a parameter in the superordinate component and in the action component:

If no default value is set for the created parameter of the action component (through the corresponding pool parameter or through the specification of a value within the resource), a reference is placed by default to the parameter of the same name in the discipline-superordinate component. Since this is a default value, it can be overwritten as usual in the library component or in the instances.
