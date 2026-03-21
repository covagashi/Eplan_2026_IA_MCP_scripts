---
title: "and operator for Boolean"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_boolean_and.htm"
file: "refformulas_r_boolean_and"
category: "refformulas"
---

# and operator for Boolean

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  and operator for Boolean Boolean operator Logical and (commutative). **< Expression1> and <Expression2>**  
---  
Expressions | Boolean | Expression1 | Logical operator  
Boolean | Expression2 | Logical operator  
Return value | Boolean |   
Value table  
---  
Expression1 | Expression2 | Result  
true | true | true  
true | false | false  
false | true | false  
false | false | false  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
= true and false | false  
= true and null | null  
= false and null | false  
= error('Hello World') and false | false  
= error('Hello World') and true | error  
= error('Hello World') and null | error
