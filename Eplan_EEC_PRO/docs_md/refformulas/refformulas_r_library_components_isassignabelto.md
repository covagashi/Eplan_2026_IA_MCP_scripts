---
title: "isAssignableTo(String typeName)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_library_components_isassignabelto.htm"
file: "refformulas_r_library_components_isassignabelto"
category: "refformulas"
---

# isAssignableTo(String typeName)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  isAssignableTo(String typeName) Delivers true if the type equals the type of the library component <typeName>. **isAssignableTo(String typeName)**  
---  
Argument | String | typeName |  Name of the library component May be assigned as name or absolute name (always the absolute name should be used, because it identifies the library component unique)  
Return value | Boolean |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
type(âModularSystem.Interfaces,IconfigurableStationâ)isAssignableTo(âModularSystem.Interfaces.IStationâ) | true
