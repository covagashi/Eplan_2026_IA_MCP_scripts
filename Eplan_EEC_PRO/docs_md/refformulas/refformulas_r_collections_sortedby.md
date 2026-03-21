---
title: "sortedBy(Block expression)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_collections_sortedby.htm"
file: "refformulas_r_collections_sortedby"
category: "refformulas"
---

# sortedBy(Block expression)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  sortedBy(Block expression) General methods for Collections Sorts the Collection according to the assigned expression. sortedBy(Block expression)  
---  
Argument | Block | expression |   
Return value | Collection | Sorted collection. The collection has the same type, as the collection, that sortedBy is sent to.  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=List{'abc','c','bf'}.sortedBy(x|x.size) | [c, bf, abc]  
=List{'abc','c','bf'}.sortedBy(x|x.$Name) | [abc,bf,c]
