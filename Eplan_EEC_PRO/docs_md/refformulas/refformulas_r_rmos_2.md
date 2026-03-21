---
title: "rmos(Boolean alsoDisabled)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_rmos_2.htm"
file: "refformulas_r_rmos_2"
category: "refformulas"
---

# rmos(Boolean alsoDisabled)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  rmos(Boolean alsoDisabled) Navigation methods for mechatronic components rmos(alsoDisabled) corresponds to the method rmos for alsoDisabled=false. If the return value is alsoDisabled=true also the disabled children of the mechatronic component are returned. **rmos(Boolean alsoDisabled)**  
---  
Argument | Boolean | alsoDisabled |  true = deactivated project components are also taken into consideration false = deactivated project components are not taken into consideration  
Return value | List |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
Testproject.Mechatronic.Feeder  
.rmos(true) | [<<Store>>, <<Discard>>, <<Insert>>, <<Stack>>, <<Positionsensor_optical>>, <<Separator>>, <<Cylinder>>, <<Valve>>, <<Position_1>>, <<Position_2>>, <<Inspect>>, <<Orientationinspector>>, <<Positionsensor_optical>>, <<Move>>, <<X_Axis>>, <<Cylinder>>, <<Valve>>, <<Position_1>>, <<Position_2>>, <<Position_3>>, <<Position_4>>, <<Y_Axis>>, <<Cylinder>>, <<Valve>>, <<Position_1>>, <<Position_2>>, <<Position_3>>, <<Position_4>>, <<Gripper>>, <<Cylinder>>, <<Pressuresensor>>]
