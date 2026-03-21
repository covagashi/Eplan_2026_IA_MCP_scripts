---
title: "any(Block condition)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_collections_any.htm"
file: "refformulas_r_collections_any"
category: "refformulas"
---

# any(Block condition)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  any(Block condition) General methods for Collections Delivers the object for which the condition is true. Is the condition for more than one object true any one of the objects is delivered. The result is undefined if no object satisfies the expression. any(Block condition)  
---  
Argument | Block | condition | Condition to be satisfied for the objects.  
Return value | Object |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=List{'abc','f','cb'}.any(x|x.size=2) | cb
