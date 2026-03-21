---
title: "Circle references (recursions)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_recursions.htm"
file: "refformulas_r_recursions"
category: "refformulas"
---

# Circle references (recursions)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Circle references (recursions) Circle references arise through references to the end result or an intermediate result of a term within a formula. Circle references generally lead to unwanted results or error messages. [Example](javascript:void\(0\);) Parameter name | Value  
---|---  
A | 8  
B | if $Result > 21 then 3 else 4 endif  
Result | =$A * $B  
Resulting error message: `Recursion detected: 'Recursion_Test':$Result --> 'Recursion_Test':$B --> 'Recursion_Test':$Result` The error message in the console describes that the error is caused by the value of parameter B. Parameter B calculates its value taking into account the value of parameter Result. In the project component the text is displayed for $B and $Result instead of a value .
