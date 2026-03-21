---
title: "mos(String typeName, Boolean alsoDisabled)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_mos_5.htm"
file: "refformulas_r_mos_5"
category: "refformulas"
---

# mos(String typeName, Boolean alsoDisabled)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  mos(String typeName, Boolean alsoDisabled) Navigation methods for mechatronic components mos(typeName, alsoDisabled) corresponds to the method mos(String typeName) for alsoDisabled=false. If the return value is alsoDisabled=true also the disabled children of the mechatronic component are returned. **mos(String typeName, Boolean alsoDisabled)**  
---  
Arguments | String | typeName | Type of the components to be determined  
Boolean | alsoDisabled |  true = deactivated project components are also taken into consideration false = deactivated project components are not taken into consideration  
Return value | List |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
Testproject.Mechatronic.Feeder  
.mos('T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Inspect', true) | [<<Inspect>>]
