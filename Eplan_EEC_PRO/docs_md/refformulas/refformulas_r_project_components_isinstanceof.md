---
title: "isInstanceOf(String typeName)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_project_components_isinstanceof.htm"
file: "refformulas_r_project_components_isinstanceof"
category: "refformulas"
---

# isInstanceOf(String typeName)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  isInstanceOf(String typeName) General methods for project components Returns true if for the project component either the library component <typeName>, the library component <typeName> is a superclass of the library component, or <typeName> is an interface associated with the library component. **isInstanceOf(String typeName)**  
---  
Argument | String | typeName | Name of the library component  
May be assigned as name or absolute name (always the absolute name should be used, because it identifies the library component unique)  
Return value | Boolean |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
Feeder.Mechatronic.Feeder  
.isInstanceOf('T_Mechatronic_ModularSystem.Mechatronic  
.Stations.Feeder') | true
