---
title: "ref(String absoluteName, Boolean alsoDisabled)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_project_components_ref2.htm"
file: "refformulas_r_project_components_ref2"
category: "refformulas"
---

# ref(String absoluteName, Boolean alsoDisabled)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  ref(String absoluteName, Boolean alsoDisabled) Navigation methods for project components References the project component absoluteName. **ref(String absoluteName,Boolean alsoDisabled)**  
---  
Expressions | String | absoluteName | Absolute name of a component.  
Boolean | alsoDisabled |  true = deactivated project components are also taken into consideration false = deactivated project components are not taken into consideration  
Return value | Project component | The referenced project component  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=ref('Feeder.Mechatronic.Feeder',true) | <<Feeder>>
