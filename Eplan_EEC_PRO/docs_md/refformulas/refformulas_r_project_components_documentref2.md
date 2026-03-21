---
title: "documentRef(String absoluteName, Boolean alsoDisabled)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_project_components_documentref2.htm"
file: "refformulas_r_project_components_documentref2"
category: "refformulas"
---

# documentRef(String absoluteName, Boolean alsoDisabled)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  documentRef(String absoluteName, Boolean alsoDisabled) Navigation methods for project components Checks if the document (e.g. a diagram) given by absoluteName is referencable. Documents of super ordinary components which are disabled can also be referenced. **documentRef(String absoluteName, Boolean alsoDisabled)**  
---  
Expressions | String | absoluteName | Absolute name of a document  
Boolean | alsoDisabled |  true = deactivated project components are also taken into consideration false = deactivated project components are not taken into consideration  
Return value | Document | The referenced document  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=documentRef('IT.Mechatronic.Building.IT_SolutionMap', true) | <<IT_SolutionMap>>
