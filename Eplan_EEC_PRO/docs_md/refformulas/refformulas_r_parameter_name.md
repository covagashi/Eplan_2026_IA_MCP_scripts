---
title: "name"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_parameter_name.htm"
file: "refformulas_r_parameter_name"
category: "refformulas"
---

# name

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  name Methods for Parameters The parameter.name or Parameter().name method delivers the name of the parameter object whose formula is executed. name  
---  
Argument |  |  |   
Return value | String |   
[Example](javascript:void\(0\);) Given: Parameter name | Value  
---|---  
Data | =Map{Pair{'Example1','A'},Pair{'Example2','B'},Pair{'Example3','C'}}  
With the following formula a value can then be determined from the map whose key corresponds to the name of the parameter: Formula | Result  
---|---  
Example3= if $Data.containsKey(parameter.name) then $Data.value(parameter.name) else '' | C
