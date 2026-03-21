---
title: "mos(Integer depth)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_mos_3.htm"
file: "refformulas_r_mos_3"
category: "refformulas"
---

# mos(Integer depth)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  mos(Integer depth) Navigation methods for mechatronic components mos(depth) returns the children of the depth level below the mechatronic component. **mos(Integer depth)**  
---  
Argument | Integer | depth | Subordinate hierarchy level in which mechatronic components are determined  
Return value | List |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
Testproject.Mechatronic.Feeder  
.mos(2) | [<<Stack>>, <<Separator>>, <<Orientationinspector>>, <<X_Axis>>, <<Y_Axis>>, <<Gripper>>]
