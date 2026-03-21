---
title: "rdos(String typeName)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_rdos_2.htm"
file: "refformulas_r_rdos_2"
category: "refformulas"
---

# rdos(String typeName)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  rdos(String typeName) Navigation methods for discipline-specific components All recursively determined discipline-specific children of a discipline-specific component which are an instance of the type typeName (see [isInstanceOf(String typeName)](refformulas_r_project_components_isinstanceof.htm)) (see [Project component navigation methods](refformulas_r_project_components_navigation.htm)). The argument can be declared with and without unit path. rdos(String typeName)  
---  
Argument | String | typeName | Type of the components to be determined  
Return value | List |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
Feeder.ListOfComponents.Sensors-Actuators-Body.Actuators-Section.rdos('T_Mechatronic_ModularSystem.ListOfComponents.Sensors-Actuators-Row') | [<<Sensors-Actuators-Row>>, <<Sensors-Actuators-Row2>>, <<Sensors-Actuators-Row3>>, <<Sensors-Actuators-Row4>>, <<Sensors-Actuators-Row5>>, <<Sensors-Actuators-Row6>>, <<Sensors-Actuators-Row7>>]
