---
title: "asHexString(Integer length)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_integer_ashexstring_2.htm"
file: "refformulas_r_integer_ashexstring_2"
category: "refformulas"
---

# asHexString(Integer length)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  asHexString(Integer length) Integer methods Creates a character string which represents the integer as a hexadecimal number. The character string is filled-up with leading 0 characters until the length of <length>. If the result is already larger than <length>, the result will not be affected. Is equivalent to asString(16, length). asHexString(Integer length)  
---  
Arguments | Integer | length | Lengtj of the hexadecimal number  
Return value | String |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=12.asHexString(5) | 0000c
