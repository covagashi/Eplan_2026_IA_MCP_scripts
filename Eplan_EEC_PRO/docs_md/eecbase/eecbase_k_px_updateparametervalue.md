---
title: "updateParameterValue"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_px_updateparametervalue.htm"
file: "eecbase_k_px_updateparametervalue"
category: "eecbase"
---

# updateParameterValue

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

updateParameterValue

## updateParameterValue

Updates the value of the parameter with the stated absolute path in all existing projects.

updateParameterValue(String parameterAbsPath, Object parameterValue)  
---  
Argument | String | instanceAbsPath | Absolute path to the project component.  
Object | parameterValue | New value of the parameter.  
Return value | Boolean | true = at least one parameter value has been updated.  
false = no parameter value has been updated.
