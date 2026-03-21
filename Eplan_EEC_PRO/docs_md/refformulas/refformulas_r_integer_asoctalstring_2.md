---
title: "asOctalString(Integer length)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_integer_asoctalstring_2.htm"
file: "refformulas_r_integer_asoctalstring_2"
category: "refformulas"
---

# asOctalString(Integer length)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  asOctalString(Integer length) Integer methods Creates a character string which represents the integer as an octal number. The character string is filled-up with leading 0 characters until the length of <length>. If the result is already larger than <length>, the result will not be affected. Is equivalent to asString(8, length). asOctalString(Integer length)  
---  
Arguments | Integer | length | Length of the octal number  
Return value | String |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=12.asOctalString(5) | 00014
