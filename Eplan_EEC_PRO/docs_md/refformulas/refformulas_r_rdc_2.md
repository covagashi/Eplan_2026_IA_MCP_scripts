---
title: "rdc(String typeName)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_rdc_2.htm"
file: "refformulas_r_rdc_2"
category: "refformulas"
---

# rdc(String typeName)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  rdc(String typeName) Navigation methods for discipline-specific components Determines all superordinate discipline-specific components which are an instance of the type typeName (see [isInstanceOf(String typeName)](refformulas_r_project_components_isinstanceof.htm)) (see [Project component navigation methods](refformulas_r_project_components_navigation.htm)). rdc(String typeName)  
---  
Argument | String | typeName | Type of the components to be determined  
Return value | List |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
Feeder.ListOfComponents.Sensors-Actuators-Body.Actuators-Section.rdc('T_Mechatronic_ModularSystem.ListOfComponents.Sensors-Actuators-Body') | [<<Sensors-Actuators-Body>>]
