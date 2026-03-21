---
title: "forAll(Block condition)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_collections_forall.htm"
file: "refformulas_r_collections_forall"
category: "refformulas"
---

# forAll(Block condition)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  forAll(Block condition) General methods for Collections Returns true if all objects of the Collection satisfy the condition. forAll(Block condition)  
---  
Argument | Block | condition | Condition which all objects of the collection have to satisfy.  
Return value | Boolean |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=List{'abc','bc','c'}.forAll(x|x.size=1) | false
