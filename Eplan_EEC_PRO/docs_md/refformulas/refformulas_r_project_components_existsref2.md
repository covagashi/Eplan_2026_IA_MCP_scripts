---
title: "existsRef(String absoluteName, Boolean alsoDisabled)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_project_components_existsref2.htm"
file: "refformulas_r_project_components_existsref2"
category: "refformulas"
---

# existsRef(String absoluteName, Boolean alsoDisabled)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  existsRef(String absoluteName, Boolean alsoDisabled) Navigation methods for project components Determines if the project component given by absoluteName is referencable. **existsRef(String absoluteName, Boolean alsoDisabled)**  
---  
Arguments | String | absoluteName | The path to a project component  
Boolean | alsoDisabled |  true = deactivated project components are also taken into consideration false = deactivated project components are not taken into consideration  
Return value | Boolean |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=existsRef('Feeder.Mechatronic.Feeder.Inspect', true) | true or false
