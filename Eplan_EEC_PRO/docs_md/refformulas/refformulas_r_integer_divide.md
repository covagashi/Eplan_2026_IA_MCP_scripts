---
title: "Division operator for integer"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_integer_divide.htm"
file: "refformulas_r_integer_divide"
category: "refformulas"
---

# Division operator for integer

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Division operator for integer Integer operator Integer division It is frequently expected that the result of the division of two integers is a floating point number. To achieve this result either the dividend or the divisor is to be converted to a double (see [asDouble()](refformulas_r_conversion_asdouble.htm)). <Integer1> / <Integer2>  
---  
Expressions | Integer | Integer1 | Arithmetic operator  
Integer | Integer2 | Arithmetic operator  
Return value | Integer |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
= 4/2 | 2  
= 8/3 | 2  
=-7/2 | -3  
=asDouble(8)/3 | 2.6666666666666665  
=8/asDouble(3) | 2.6666666666666665
