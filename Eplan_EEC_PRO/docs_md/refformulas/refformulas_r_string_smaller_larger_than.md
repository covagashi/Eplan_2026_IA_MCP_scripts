---
title: "Unequal operator for string"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_string_smaller_larger_than.htm"
file: "refformulas_r_string_smaller_larger_than"
category: "refformulas"
---

# Unequal operator for string

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Unequal operator for string String operator Unequal operator. Attention should be paid to case-sensitivity for comparison of character strings. <Character string1> <> <Character string2>  
---  
Expressions | String | String1 | Compare operator  
String | String2 | Compare operator  
Return value | String  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
= 'ab' <> 'ab' | false  
= 'ab' <> 'AB' | true  
= 'ab' <> null | null  
The compare operators <,>,<=,>= are defined for character strings, but can be used meaningfully only in exceptional cases, because they compare the sums of the Unicode values of the character strings.
