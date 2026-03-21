---
title: "relRef(String relativeName, Boolean alsoDisabled)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_project_components_relref2.htm"
file: "refformulas_r_project_components_relref2"
category: "refformulas"
---

# relRef(String relativeName, Boolean alsoDisabled)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  relRef(String relativeName, Boolean alsoDisabled) Navigation methods for project components References the project component relativeName. Project components which are disabled can also be referenced. **relRef(String relativeName, Boolean alsoDisabled)**  
---  
Arguments | String | relativeName | Project component  
Boolean | alsoDisabled |  true = deactivated project components are also taken into consideration false = deactivated project components are not taken into consideration  
Return value | Project component | The referenced project component  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
mroot.relRef('St01Roundtable.DriveSupply.Supply2',true) | <<Supply2>> or ReferenceNotFoundException
