---
title: "rmc()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_rmc_1.htm"
file: "refformulas_r_rmc_1"
category: "refformulas"
---

# rmc()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  rmc() Navigation methods for mechatronic components Determines all superordinate mechatronic components. The component determined by mc is the first component of the list. The component determined by mroot is the last component of the list (see [Project component navigation methods](refformulas_r_project_components_navigation.htm)). **rmc()**  
---  
Argument |  |  |   
Return value | List |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
Testproject.Mechatronic.Feeder.Inserting.  
Stack.Positionsensor_optical.rmc | [<<Stack>>, <<Insert>>, <<Feeder>>]
