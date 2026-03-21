---
title: "mos(Boolean alsoDisabled)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_mos_2.htm"
file: "refformulas_r_mos_2"
category: "refformulas"
---

# mos(Boolean alsoDisabled)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  mos(Boolean alsoDisabled) Navigation methods for mechatronic components mos(alsoDisabled) corresponds to the method mos for alsoDisabled=false. If the return value is alsoDisabled=true also the disabled children of the mechatronic component are returned. **mos(Boolean alsoDisabled)**  
---  
Argument | Boolean | alsoDisabled |  true = deactivated project components are also taken into consideration false = deactivated project components are not taken into consideration  
Return value | List |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
Testproject.Mechatronic.Feeder  
.mos(true) | [<<Store>>, <<Discard>>, <<Insert>>, <<Inspect>>, <<Move>>]
