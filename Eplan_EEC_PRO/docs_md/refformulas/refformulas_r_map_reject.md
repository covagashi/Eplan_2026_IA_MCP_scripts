---
title: "reject(Block condition)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_map_reject.htm"
file: "refformulas_r_map_reject"
category: "refformulas"
---

# reject(Block condition)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  reject(Block condition) Methods For Map Selects the objects that do not meet the condition. reject(Block condition)  
---  
Argument | Block | condition | Condition that the objects which are to be selected must not meet.  
Return value | Map | Map of all key-value pairs that do not meet the condition.  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=Map{Pair{'A',1}, Pair{'B',2}}.reject(x|x.key='A') | [BÂ»2]
