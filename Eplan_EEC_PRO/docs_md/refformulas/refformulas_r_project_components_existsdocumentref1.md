---
title: "existsDocumentRef(String absoluteName)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_project_components_existsdocumentref1.htm"
file: "refformulas_r_project_components_existsdocumentref1"
category: "refformulas"
---

# existsDocumentRef(String absoluteName)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  existsDocumentRef(String absoluteName) Navigation methods for project components Checks if the document (e.g. a diagram) given by absoluteName exists. If the parent component, which contains the document, is disabled, the value false is returned. **existsDocumentRef(String absoluteName)**  
---  
Arguments | String | absoluteName | The absolute path to the document  
Return value | Boolean |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=existsDocumentRef('IT.Mechatronic.Building.IT_SolutionMap') | true or false
