---
title: "includingAll(Collection coll)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_collections_includingall.htm"
file: "refformulas_r_collections_includingall"
category: "refformulas"
---

# includingAll(Collection coll)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  includingAll(Collection coll) General methods for Collections Adds the objects of the collection coll to the Collection. includingAll(Collection coll)  
---  
Argument | Collection | coll | Collection with the objects to be added  
Return value | Collection |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=List{1, 2, 2, 3}.includingAll(Set{2}) | [1, 2, 2, 3, 2]
