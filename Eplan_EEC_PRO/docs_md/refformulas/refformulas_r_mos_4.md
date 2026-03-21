---
title: "mos(String typeName)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_mos_4.htm"
file: "refformulas_r_mos_4"
category: "refformulas"
---

# mos(String typeName)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  mos(String typeName) Navigation methods for mechatronic components mos(typeName) returns all not disabled children of the mechatronic component which are an instance of typeName (see [isInstanceOf(String typeName)](refformulas_r_project_components_isinstanceof.htm)). The argument can be declared with and without unit path. **mos(String typeName)**  
---  
Argument | String | typeName | Type of the components to be determined  
Return value | List |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
Testproject.Mechatronic.Feeder  
.mos('T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Inspect') | [<<Inspect>>]
