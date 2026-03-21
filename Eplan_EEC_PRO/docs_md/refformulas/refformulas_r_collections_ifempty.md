---
title: "ifEmpty(Block block)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_collections_ifempty.htm"
file: "refformulas_r_collections_ifempty"
category: "refformulas"
---

# ifEmpty(Block block)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  ifEmpty(Block block) General methods for Collections If the Collection (List, Bag or Set) is empty, the result of the formula given with the argument block is returned. ifEmpty(Block block)  
---  
Argument | Block | block | Formula, which returns an alternative result.  
Return value | Boolean |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=List{}.ifEmpty(List{'default')) | [default]
