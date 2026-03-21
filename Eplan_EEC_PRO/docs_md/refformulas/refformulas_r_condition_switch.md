---
title: "switch"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_condition_switch.htm"
file: "refformulas_r_condition_switch"
category: "refformulas"
---

# switch

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  switch Is used to define conditions. The following comparisons are made: Expression = Expression1 (any expressions) Expression8>=Expression<=Expression9 (Integer or Double) Contrary to if-then-else-endif the method is always executed independent of an input condition. The case expressions have to be unique! A default expression always has to be assigned because the formula language always has to deliver a value. **switch <Expression> {   
case Expression1: Expression2   
case Expression3: Expression4   
case Expression5: case Expression6: Expression7   
case Expression8..Expression9: Expression10   
case Expression11. case Expression12..Expression13: Expression14   
else: Default expression   
}**  
---  
Arguments |  |  |   
Return value |  |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
= switch 1 {case 1: 'Hello' case 2: 'world' else: 'foo'} | Hello  
= switch 2 {case 1: 'Hello' case 2: 'world' else: 'foo'} | World  
= switch 1 {case 1:case 2: 'Hello' else: 'foo'} | Hello  
= switch 2 {case 1:case 2: 'Hello' else: 'foo'} | Hello  
= switch 3 {case 0..4: 'Hello world' else: 'foo'} | Hello World  
= switch 3 {case 0: case 2..4: 'Hello world' else: 'foo'} | Hello World  
= switch 1 {case 0: case 2..4: 'Hello world' else: 'foo'} | foo  
= switch null {case 3: 'a' else: 'b'} | b  
= switch 7 {case null: 'a' else: 'b'} | b  
= switch 7 {case null..3: 'a' else: 'b'} | b  
= switch 7 {case 3..null: 'a' else: 'b'} | b
