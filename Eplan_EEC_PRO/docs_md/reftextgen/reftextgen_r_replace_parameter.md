---
title: "Replace parameters"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/reftextgen_r_replace_parameter.htm"
file: "reftextgen_r_replace_parameter"
category: "reftextgen"
---

# Replace parameters

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Replace parameters Text generator Replace parameters are used to replace parts of the template whilst generating. The opening and closing tokens are specified in the text discipline configuration or respectively in the settings for the PLC disciplines (e.g. opening token = "M8B_" closing token = "_M8E"). The tokens must be defined in a way, that no conflicts with existing names in the text, which is to generate, appear (e.g. < as the opening token in XML documents). The text between the tokens appears in the interface as parameter. The parameter for the PLC disciplines is declared by the variable type REPLACE. [Example](javascript:void\(0\);)  
      
        CALL"Achse","M8B_Name_M8E"(Freigabe:="KoFreigabe");
