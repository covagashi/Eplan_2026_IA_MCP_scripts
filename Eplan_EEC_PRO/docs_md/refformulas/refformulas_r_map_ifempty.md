---
title: "ifEmpty(Block block)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_map_ifempty.htm"
file: "refformulas_r_map_ifempty"
category: "refformulas"
---

# ifEmpty(Block block)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  ifEmpty(Block block) Methods For Map If the Map (Map, OrderedMap or BidiMap) is empty, the result of the formula given with the argument block is returned. ifEmpty(Block block)  
---  
Argument | Block | block | Formula, which returns an alternative result.  
Return value |  |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=Map{}.ifEmpty(Map{Pair{1,2}}) | [1Â»2]
