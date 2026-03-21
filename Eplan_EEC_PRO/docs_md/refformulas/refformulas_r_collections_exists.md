---
title: "exists(Block condition)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_collections_exists.htm"
file: "refformulas_r_collections_exists"
category: "refformulas"
---

# exists(Block condition)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  exists(Block condition) General methods for Collections Delivers true if at least one object satisfies the condition. exists(Block condition)  
---  
Argument | Block | Condition | Condition which at least one object has to satisfy.  
Return value | Boolean |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=List{'abc','bc','c'}.exists(x|x.size=1) | true
