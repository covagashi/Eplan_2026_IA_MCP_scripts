---
title: "existsRef(String absoluteName)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_project_components_existsref1.htm"
file: "refformulas_r_project_components_existsref1"
category: "refformulas"
---

# existsRef(String absoluteName)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  existsRef(String absoluteName) Navigation methods for project components Determines if the project component given by absoluteName is referencable. Project components which are disabled cannot be referenced. **existsRef(String absoluteName)**  
---  
Arguments | String | absoluteName | The path to a project component  
Return value | Boolean |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=existsRef('Feeder.Mechatronic.Feeder.Inspect') | true or false
