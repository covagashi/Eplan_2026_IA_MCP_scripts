---
title: "Implies operator for Boolean"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_boolean_implies.htm"
file: "refformulas_r_boolean_implies"
category: "refformulas"
---

# Implies operator for Boolean

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Implies operator for Boolean Boolean operator Implies is a shortcut for (not <Expression1>) or <Expression2>. <Expression1> implies <Expression2>  
---  
Expressions | Boolean | Expression1 | First expression that returns a Boolean value.  
Boolean | Expression2 | Second expression that returns a Boolean value.  
Return value | Boolean |   
Value table  
---  
Expression1 | Expression2 | Result  
true | true | true  
true | false | false  
false | true | true  
false | false | true  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
= true implies false | false  
= false implies null | true  
= true implies null | null  
= true implies error('Hello World') | error  
= error('Hello World') implies true | true  
= false implies error('Hello World') | true  
= error('Hello World') implies false | error  
= null implies error('Hello World') | error  
= error('Hello World') implies null | error
