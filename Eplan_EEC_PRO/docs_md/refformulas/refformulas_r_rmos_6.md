---
title: "rmos(String typeName, Integer depth)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_rmos_6.htm"
file: "refformulas_r_rmos_6"
category: "refformulas"
---

# rmos(String typeName, Integer depth)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  rmos(String typeName, Integer depth) Navigation methods for mechatronic components rmos(typeName, depth) returns all children of the mechatronic component to the depthlevel, which correspond to the type typeName. **rmos(String typeName, Integer depth)**  
---  
Arguments | String | typeName | Type of the components to be determined  
Integer | depth | Subordinate hierarchy level in which mechatronic components are determined  
Return value | List |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
rmos('T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Axis', 2) | [<<X_Axis>>, <<Y_Axis>>]
