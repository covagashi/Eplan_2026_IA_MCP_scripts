---
title: "isMaxValue()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_integer_ismaxvalue.htm"
file: "refformulas_r_integer_ismaxvalue"
category: "refformulas"
---

# isMaxValue()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  isMaxValue() Integer methods Delivers true if the integer matches the largest possible integer. The maximum integer value is 231-1. isMaxValue()  
---  
Argument |  |  |   
Return value | Boolean |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=3.isMaxValue | false  
=2147483647.isMaxValue | true  
='7fffffff'.asInteger(16).isMaxValue | true
