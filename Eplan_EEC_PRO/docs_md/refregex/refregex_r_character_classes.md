---
title: "Character Classes in Regular Expressions"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refregex_r_character_classes.htm"
file: "refregex_r_character_classes"
category: "refregex"
---

# Character Classes in Regular Expressions

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Character Classes in Regular Expressions Characters | Meaning | Example | Result  
---|---|---|---  
[a,b,c] | a or b or c | 'a'.matches('[a,b,c]')   
'b'.matches('[a,b,c]')  
'B'.matches('[a,b,c]') | true   
true  
false  
[^a,b,c] | any character except a, b, or c | 'a'.matches('[^a,b,c]')   
'b'.matches('[^a,b,c]')  
'B'.matches('[^a,b,c]') | false   
false  
true  
[a-z] | any character from a through z | 'a'.matches('[a-z]')   
'x'.matches('[a-z]')  
'B'.matches('[a-z]') | true   
true  
false  
[a-zA-Z] | any character from a through z or A through Z | 'a'.matches('[a-zA-Z]')   
'x'.matches('[a-zA-Z]')  
'B'.matches('[a-zA-Z]') | true   
true  
true  
[a-d[x-z]] | any character from a through d or x through z | 'a'.matches('[a-d[x-z]]')   
'x'.matches('[a-d[x-z]]')  
'B'.matches('[a-d[x-z]]') | true   
true  
false  
[a-z&&[^bp]] | any character from a through z except b or p | 'a'.matches('[a-z&&[^bp]]')   
'x'.matches('[a-z&&[^bp]]')  
'p'.matches('[a-z&&[^bp]]') | true   
true  
false
