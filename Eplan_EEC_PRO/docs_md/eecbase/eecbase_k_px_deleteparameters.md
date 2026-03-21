---
title: "deleteParameters"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_px_deleteparameters.htm"
file: "eecbase_k_px_deleteparameters"
category: "eecbase"
---

# deleteParameters

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

deleteParameters

## deleteParameters

Deletes all parameters that are stated in the array. Using the prefix argument, an absolute path is provided to the parameters. If the prefix is null, all parameters will be deleted that correspond to the names in the array.

deleteParameters(String prefix, String[ ] parameterNames)  
---  
Argument | String | prefix | Absolute path to the parameters to be deleted.  
String[ ] | parameterNames | Array of parameter names.  
Return value | Boolean | true = all parameter names have been deleted successfully.  
false = no parameter name has been deleted.
