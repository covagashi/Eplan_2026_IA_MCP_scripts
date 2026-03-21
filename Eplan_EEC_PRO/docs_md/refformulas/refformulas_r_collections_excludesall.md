---
title: "excludesAll(Collection sub)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_collections_excludesall.htm"
file: "refformulas_r_collections_excludesall"
category: "refformulas"
---

# excludesAll(Collection sub)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  excludesAll(Collection sub) General methods for Collections Returns true if none of the objects of the collection sub is included in the collection. excludesAll(Collection sub)  
---  
Argument | Collection | sub | Collection with objects which should not be included in the collection.  
Return value | Boolean |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=List{1,2,3,4}.excludesAll(List{1,7}) | false
