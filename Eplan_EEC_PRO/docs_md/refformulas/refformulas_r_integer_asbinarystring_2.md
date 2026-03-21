---
title: "asBinaryString(Integer length)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_integer_asbinarystring_2.htm"
file: "refformulas_r_integer_asbinarystring_2"
category: "refformulas"
---

# asBinaryString(Integer length)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  asBinaryString(Integer length) Integer methods Creates a string which represents the integer as a binary number. The character string is filled-up with leading 0 characters until the length of <length>. If the result is already larger than <length>, the result will not be affected. Is equivalent to asString(2, length). asBinaryString(Integer length)  
---  
Arguments | Integer | length | Length of the binary  
Return value | String |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=12.asBinaryString(5) | 01100
