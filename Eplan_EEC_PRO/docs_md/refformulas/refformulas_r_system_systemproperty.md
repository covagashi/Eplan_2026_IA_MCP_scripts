---
title: "systemProperty(String propertyName)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_system_systemproperty.htm"
file: "refformulas_r_system_systemproperty"
category: "refformulas"
---

# systemProperty(String propertyName)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  systemProperty(String propertyName) System methods Determines the value of the given system property or null, if the value is not set. **systemProperty(String propertyName)**  
---  
Argument | String | propertyName | System property whose value is queried  
Return value | String | Value of the system property  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=type('Engineering.System').systemProperty('user.home') | C:\Users\MyUsername
