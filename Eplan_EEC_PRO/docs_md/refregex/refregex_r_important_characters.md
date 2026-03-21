---
title: "Important Characters in Regular Expressions"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refregex_r_important_characters.htm"
file: "refregex_r_important_characters"
category: "refregex"
---

# Important Characters in Regular Expressions

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Important Characters in Regular Expressions Characters | Meaning | Example | Result  
---|---|---|---  
X | Character X | 'X'.matches('X')  
'Y'.matches('X') | true  
false  
\\\ | Backslash character | '\' matches('\\\\\\\')  
'/'.matches('\\\\\\\') | true  
false  
\t | Tabulator character | ' '.matches('\\\t')  
' '.matches('\\\t') | true  
false  
\n | Line feed character | '\n'.matches('\\\n')  
'\\\n'.matches('\\\n') | true  
false
