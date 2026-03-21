---
title: "select(Block condition)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_map_select.htm"
file: "refformulas_r_map_select"
category: "refformulas"
---

# select(Block condition)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  select(Block condition) Map methods Selects the objects that meet the condition. **select(Block condition)**  
---  
Argument | Block | condition | Condition that the objects which are to be selected must meet.  
Return value | Map | Map of all key-value pairs that meet the condition.  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=Map{Pair{'A',1}, Pair{'B',2}}.select(x|x.key='A') | [AÂ»1]
