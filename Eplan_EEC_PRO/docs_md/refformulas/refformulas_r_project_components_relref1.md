---
title: "relRef(String relativeName)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_project_components_relref1.htm"
file: "refformulas_r_project_components_relref1"
category: "refformulas"
---

# relRef(String relativeName)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  relRef(String relativeName) Navigation methods for project components References the project component relativeName. Project components which are disabled cannot be referenced (see [Project component navigation methods](refformulas_r_project_components_navigation.htm)). **relRef(String relativeName)**  
---  
Arguments | String | relativeName | Relative path to a project component  
Return value | Project component |  | The referenced project component  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
mroot.relRef('St01CircularPlate.DriveSupply.  
Supply2') | <<Supply2>> or ReferenceNotFoundException
