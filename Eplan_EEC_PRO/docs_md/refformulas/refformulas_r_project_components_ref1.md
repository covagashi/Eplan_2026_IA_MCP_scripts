---
title: "ref(String absoluteName)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_project_components_ref1.htm"
file: "refformulas_r_project_components_ref1"
category: "refformulas"
---

# ref(String absoluteName)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  ref(String absoluteName) Navigation methods for project components References the project component absoluteName. Project components which are disabled cannot be referenced (see [Project component navigation methods](refformulas_r_project_components_navigation.htm)). **ref(String absoluteName)**  
---  
Arguments | String | absoluteName | The path to a project component  
Return value | Project component | The referenced project component  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
Feeder.Mechatronic.Feeder.ref('Feeder.Mechatronic.Feeder') | <<Feeder>>
