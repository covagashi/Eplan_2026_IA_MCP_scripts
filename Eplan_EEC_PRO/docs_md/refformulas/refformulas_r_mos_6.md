---
title: "mos(String typeName, Integer depth)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_mos_6.htm"
file: "refformulas_r_mos_6"
category: "refformulas"
---

# mos(String typeName, Integer depth)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  mos(String typeName, Integer depth) Navigation methods for mechatronic components mos(typeName, depth) returns the children of the depth level below the mechatronic component, which correspond to the type typeName. **mos(String typeName, Integer depth)**  
---  
Arguments | String | typeName | Type of the components to be determined  
Integer | depth | Subordinate hierarchy level in which mechatronic components are determined  
Return value | List |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
Testproject.Mechatronic.Feeder  
.mos('T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Axis', 2) | [<<X_Axis>>, <<Y_Axis>>]
