---
title: "isUnique(Block expression)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_collections_isunique.htm"
file: "refformulas_r_collections_isunique"
category: "refformulas"
---

# isUnique(Block expression)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  isUnique(Block expression) General methods for Collections Returns true if the expression for each object of the Collection provides a different value. isUnique(Block expression)  
---  
Argument | Block | expression | Expression that should return a different value for each object of the collection.  
Return value | Boolean |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=List{'abc','bf','c'}.isUnique(x|x.size) | true
