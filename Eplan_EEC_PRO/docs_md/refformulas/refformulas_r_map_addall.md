---
title: "addAll(Map map)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_map_addall.htm"
file: "refformulas_r_map_addall"
category: "refformulas"
---

# addAll(Map map)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  addAll(Map map) Methods For Map Adds all key-value pairs of map to the map. Already existing pairs are replaced with those of map. addAll(Map map)  
---  
Argument | Map | map | Key-value pairs to be inserted.  
Return value | Map | Map  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=Map{Pair{'A',1}}.addAll(Map{Pair{'B',2},Pair{'C',3}}) | [AÂ»1, BÂ»2, CÂ»3]
