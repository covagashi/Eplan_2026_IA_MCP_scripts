---
title: "collect(Block expression)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_map_collect.htm"
file: "refformulas_r_map_collect"
category: "refformulas"
---

# collect(Block expression)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  collect(Block expression) Map methods Generates a bag which includes the objects specified by expression. collect(Block expression)  
---  
Argument | Block | expression | Expression that is applied to all objects in the collection.  
Return value | Bag | Bag with the results which arise by executing of the expression.  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=Map{Pair{'A',1}, Pair{'B',2}}.collect(x|x.value) | [1, 2]
