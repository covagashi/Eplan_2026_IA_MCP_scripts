---
title: "existsRelRef(String relativeName)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_project_components_existsrelref1.htm"
file: "refformulas_r_project_components_existsrelref1"
category: "refformulas"
---

# existsRelRef(String relativeName)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  existsRelRef(String relativeName) Navigation methods for project components Determines if the project component given by relativeName is referencable. Project components which are disabled cannot be referenced. existsRelRef(String relativeName)  
---  
Arguments | String | relativeName | Relative path to a project component  
Return value | Boolean |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
mroot.existsRelRef('St01Rundtisch.Antriebseinspeisung.Einspeisung2') | true or false
