---
title: "existsDocumentRef(String absoluteName, Boolean alsoDisabled)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_project_components_existsdocumentref2.htm"
file: "refformulas_r_project_components_existsdocumentref2"
category: "refformulas"
---

# existsDocumentRef(String absoluteName, Boolean alsoDisabled)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  existsDocumentRef(String absoluteName, Boolean alsoDisabled) Navigation methods for project components Checks if the document (e.g. a diagram) given by absoluteName exists. Documents of parent components which are disabled can also be checked for their existence. **existsDocumentRef(String absoluteName, Boolean alsoDisabled)**  
---  
Arguments | String | absoluteName | The absolute path to the document  
Boolean | alsoDisabled |  true = deactivated project components are also taken into consideration false = deactivated project components are not taken into consideration  
Return value | Boolean |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=existsDocumentRef('IT.Mechatronic.Building.IT_SolutionMap', true) | true or false
