---
title: "existsRelRef(String relativeName, Boolean alsoDisabled)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_project_components_existsrelref2.htm"
file: "refformulas_r_project_components_existsrelref2"
category: "refformulas"
---

# existsRelRef(String relativeName, Boolean alsoDisabled)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  existsRelRef(String relativeName, Boolean alsoDisabled) Navigation methods for project components Determines if the project component given by relativeName is referencable. Project components which are disabled can also be referenced. **existsRelRef(String relativeName, Boolean alsoDisabled)**  
---  
Arguments | String | relativeName | Relative path to a project component  
Boolean | alsoDisabled |  true = deactivated project components are also taken into consideration false = deactivated project components are not taken into consideration  
Return value | Boolean |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
mroot.existsRelRef('St01RCircularPlate.DriveSupply.Supply2',true) | true or false
