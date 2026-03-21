---
title: "rmc(String typeName)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_rmc_2.htm"
file: "refformulas_r_rmc_2"
category: "refformulas"
---

# rmc(String typeName)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  rmc(String typeName) Navigation methods for mechatronic components Determines all superordinate mechatronic components which are an instance of the type typeName (see [isInstanceOf(String typeName)](refformulas_r_project_components_isinstanceof.htm)) (see [Project component navigation methods](refformulas_r_project_components_navigation.htm)). **rmc(String typeName)**  
---  
Argument | String | typeName | Type of the components to be determined  
Return value | List |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
Testproject.Mechatronic.Feeder.Inserting.  
Stack.Positionsensor_optical.rmc('Functionunit') | [<<Stack>>]
