---
title: "collect(Block expression)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_collections_collect.htm"
file: "refformulas_r_collections_collect"
category: "refformulas"
---

# collect(Block expression)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  collect(Block expression) Generates a new collection which contains the objects specified by expression. collect(Block expression)  
---  
Argument | Block | expression | Expression that is applied to all objects in the collection.  
Return value | Collection | Collection with the results which arise by executing of the expression. The collection has the same type (e.g. list), as the collection, that collect is sent to.  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=List{'abc','bc','c'}.collect(x|x.size) | [3, 2, 1]
