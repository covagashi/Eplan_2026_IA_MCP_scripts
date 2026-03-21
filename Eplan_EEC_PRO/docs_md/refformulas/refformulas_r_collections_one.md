---
title: "one(Block condition)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_collections_one.htm"
file: "refformulas_r_collections_one"
category: "refformulas"
---

# one(Block condition)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  one(Block condition) General methods for Collections Returns true if the expression for exactly one object in the Collection returns true. one(Block condition)  
---  
Argument | Block | condition | Condition which should return true for exactly one object of the collection.  
Return value | Boolean |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=List{'abc','bf','cb'}.one(x|x.size=3) | true
