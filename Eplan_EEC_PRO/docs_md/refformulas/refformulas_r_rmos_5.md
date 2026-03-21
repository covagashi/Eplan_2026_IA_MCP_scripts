---
title: "rmos(String typeName, Boolean alsoDisabled)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_rmos_5.htm"
file: "refformulas_r_rmos_5"
category: "refformulas"
---

# rmos(String typeName, Boolean alsoDisabled)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  rmos(String typeName, Boolean alsoDisabled) Navigation methods for mechatronic components rmos(typeName, alsoDisabled) corresponds to the method rmos(String typeName) for alsoDisabled=false. If the return value is alsoDisabled=true also the disabled children of the mechatronic component are returned. **rmos(String typeName, Boolean alsoDisabled)**  
---  
Arguments | String | typeName | Type of the components to be determined  
Boolean | alsoDisabled |  true = deactivated project components are also taken into consideration false = deactivated project components are not taken into consideration  
Return value | List |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
rmos('T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Axis', true) | [<<X_Axis>>, <<Y_Axis>>]
