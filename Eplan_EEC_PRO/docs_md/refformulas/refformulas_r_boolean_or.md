---
title: "or operator for Boolean"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_boolean_or.htm"
file: "refformulas_r_boolean_or"
category: "refformulas"
---

# or operator for Boolean

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  or operator for Boolean Boolean operator Logical or (commutative). <Expression1> or <Expression2>  
---  
Expressions | Boolean | Expression1 | Logical operator  
Boolean | Expression2 | Logical operator  
Return value | Boolean |   
Value table  
---  
Expression1 | Expression2 | Result  
true | true | true  
true | false | true  
false | true | true  
false | false | false  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
= true or false | true  
= true or null | true  
= false or null | null  
= error('Hello World') or false | error  
= error('Hello World') or true | true  
= error('Hello World') or null | error
