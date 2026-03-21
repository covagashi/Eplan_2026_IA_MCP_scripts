---
title: "Methods for PLC discipline"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/reftextgen_r_plc_discipline_methods.htm"
file: "reftextgen_r_plc_discipline_methods"
category: "reftextgen"
---

# Methods for PLC discipline

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Context sensitive Methods for PLC disciplines Method | Description | Example result in STEP 7 syntax  
---|---|---  
Comment | The comment to the relevant object. | //Clamps the workpiece  
Call | Generates a block call for the POU | CALL"Axis","XAxis"(Release:="KoRelease")  
<VAR-TYP>VariableDeclaration | Creates the declaration for the relevant variable type. This method is used, if no variables of that type are declared in the template.   
Variables types are:
     * Temp
     * Input
     * Output
     * InOut
     * Local
     * Global
     * External
| VAR_TEMP  
SwitchAhead:BOOL;  
END_VAR  
<VAR-TYP>Variables | Declares the variables of the relevant variable type. This method is used, if variables of that type are already declared in the template.  
Variables types are:
     * Temp
     * Input
     * Output
     * InOut
     * Local
     * Global
     * External
| SwitchAhead:BOOL;
