---
title: "excluding(Object keyToRemove)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_map_excluding.htm"
file: "refformulas_r_map_excluding"
category: "refformulas"
---

# excluding(Object keyToRemove)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  excluding(Object keyToRemove) Methods For Map Removes the entry of a map. excluding(Object keyToRemove)  
---  
Argument | Object | keyToRemove | Key for the pair to be removed.  
Return value | Map | Map without the pair to be removed.  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=Map{Pair{'A',1}, Pair{'B',2}, Pair{'C',3}}.excluding('B') | [AÂ»1, CÂ»3]
