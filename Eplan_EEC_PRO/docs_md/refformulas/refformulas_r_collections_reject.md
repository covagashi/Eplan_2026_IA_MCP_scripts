---
title: "reject(Block condition)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_collections_reject.htm"
file: "refformulas_r_collections_reject"
category: "refformulas"
---

# reject(Block condition)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  reject(Block condition) General methods for Collections Selects the objects that do not meet the condition. reject(Block condition)  
---  
Argument | Block | condition | Condition that the objects which are to be selected must not meet.  
Return value | Collection | Collection of all objects that do not meet the condition. The collection has the same type, as the collection, that reject is sent to.  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=List{1,1,2}.reject(x|x=1) | [2]
