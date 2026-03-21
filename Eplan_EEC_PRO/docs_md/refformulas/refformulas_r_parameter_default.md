---
title: "default()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_parameter_default.htm"
file: "refformulas_r_parameter_default"
category: "refformulas"
---

# default()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  default() Methods for Parameters The default method returns the (calculated) default value of a parameter. Returns <null> if no default value is set. default()  
---  
Argument |  |  |   
Return value |  | The (calculated) default value of a parameter  
[Examples](javascript:void\(0\);) Parameter name | Value | Standard  
---|---|---  
TotalLength | 1000 | = Length1 + Length2  
Length1 | 500 |   
Length2 | 300 |   
Formula | Result  
---|---  
=this.parameter('TotalLength').default | 800
