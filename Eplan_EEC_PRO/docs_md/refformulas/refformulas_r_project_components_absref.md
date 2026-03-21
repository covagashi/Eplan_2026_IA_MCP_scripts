---
title: "absRef(String absoluteName)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_project_components_absref.htm"
file: "refformulas_r_project_components_absref"
category: "refformulas"
---

# absRef(String absoluteName)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  absRef(String absoluteName) Navigation methods for project components References the project component absoluteName. Project components which are disabled cannot be referenced. This method is only applicable in JMX files for the Job Server environment. **absRef(String absoluteName)**  
---  
Arguments | String | absoluteName | Absolute path to the project component.  
Return value | Project component |  | The referenced project component  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
"T_Mechatronic_ModularSystem.Mechatronic.Actions.UpdateAction", "List{absRef('Feeder.Mechatronic.Feeder')}"); | <<Feeder>>
