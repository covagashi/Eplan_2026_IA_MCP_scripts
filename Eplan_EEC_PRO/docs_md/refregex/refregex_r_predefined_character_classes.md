---
title: "Predefined Character Classes in Regular Expressions"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refregex_r_predefined_character_classes.htm"
file: "refregex_r_predefined_character_classes"
category: "refregex"
---

# Predefined Character Classes in Regular Expressions

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Predefined Character Classes in Regular Expressions Characters | Meaning | Example | Result  
---|---|---|---  
. | any character except the line terminator | 'a'.matches('.')  
'b'.matches('.')  
'\n'.matches('.') | true  
true  
false  
\d | any digit matching [0-9] | 'a'.matches('\\\d')  
'8'.matches('\\\d') | false  
true  
\D | no digit matching [^0-9] | 'a'.matches('\\\D')  
'8'.matches('\\\D') | true  
false  
\s | any whitespace character (\n,\t etc.) |  |   
\S | nor "whitespace" character |  |   
\w | any word character matching [a-zA-Z_0-9] |  |   
\W | no word character is matching [^a-zA-Z_0-9] |  |
