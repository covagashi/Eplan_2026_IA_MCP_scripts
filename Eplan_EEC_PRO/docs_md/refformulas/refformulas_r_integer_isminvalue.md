---
title: "isMinValue()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_integer_isminvalue.htm"
file: "refformulas_r_integer_isminvalue"
category: "refformulas"
---

# isMinValue()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  isMinValue() Methods for Integer Delivers true if the integer matches the smallest possible integer. The minimum integer value is -231. isMinValue()  
---  
Argument |  |  |   
Return value | Boolean |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=3.isMinValue | false  
=(-2).pow(31).isMinValue | true  
=(-2147483647-1).isMinValue | true  
='-80000000'.asInteger(16).isMinValue | true
