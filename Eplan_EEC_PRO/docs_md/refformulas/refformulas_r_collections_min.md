---
title: "min()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_collections_min.htm"
file: "refformulas_r_collections_min"
category: "refformulas"
---

# min()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  min() General methods for Collections Returns the element of a collection with the minimum value. So that this method can function, the elements of a collection must be comparable. If a collection contains different data types or if an element of the collection offers no comparison method, no error message is displayed. **min()**  
---  
Argument |  |  |   
Return value | Engineering.Object | Minimum object  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=Bag{3,3,2,1,4,3}.min |  1  
=List{1,2,3,4}.min |  1  
=Set{1,4,2,3}. min |  1  
=List{Pair{'a',1},Pair{'b',2},Pair{'c',3},Pair{'d',4}}.min |  Error message because pairs have no comparison method
