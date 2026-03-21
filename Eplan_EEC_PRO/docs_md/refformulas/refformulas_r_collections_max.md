---
title: "max()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_collections_max.htm"
file: "refformulas_r_collections_max"
category: "refformulas"
---

# max()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  max() General methods for Collections Returns the element of a collection with the maximum value. So that this method can function, the elements of a collection must be comparable. If a collection contains different data types or if an element of the collection offers no comparison method, no error message is displayed. **max()**  
---  
Argument |  |  |   
Return value | Engineering.Object | Maximum object  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=Bag{3,3,2,1,4,3}.max |  4  
=List{1,2,3,4}.max |  4  
=Set{1,4,2,3}.max |  4  
=List{Pair{'a',1},Pair{'b',2},Pair{'c',3},Pair{'d',4}}.max |  Error message because pairs have no comparison method
