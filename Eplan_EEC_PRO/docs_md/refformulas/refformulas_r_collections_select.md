---
title: "select(Block condition)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_collections_select.htm"
file: "refformulas_r_collections_select"
category: "refformulas"
---

# select(Block condition)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  select(Block condition) Selects the objects that meet the condition. select(Block condition)  
---  
Argument | Block | condition | Condition that the objects which are to be selected must meet.  
Return value | Collection | Collection of all objects that meet the condition. The collection has the same type, as the collection, that select is sent to.  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=List{1,1,2}.select(x|x=1) | [1, 1]
