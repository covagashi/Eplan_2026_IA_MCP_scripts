---
title: "if-then-else-endif"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_condition_if_then_else_endif.htm"
file: "refformulas_r_condition_if_then_else_endif"
category: "refformulas"
---

# if-then-else-endif

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  if-then-else-endif Conditions Is used to define conditions. Contrary to the if-then-else-endif statements of the most programming languages the else condition is always to be executed, because the formula language has to deliver a value even if the condition does not deliver true. For if-then-else-endif also a concise and even style exists: <Condition>?<ExpressionTrue>: <ExpressionFalse> Expressions can also be nested. **if <Condition> then <ExpressionTrue> else <ExressionFalse> endif**  
---  
Example | Formula | Result  
= if 2 = 3 then '2=3' else '2<>3' endif | 2<>3  
= 2 = 3?'2=3':'2<>3' | 2<>3  
= if 2=3 then if 2=4 then '2=4' else '2<>4' endif else '2<>3' endif | 2<>3  
=2=3?2=4?'2=4':'2<>4':'2<>3' | 2<>3  
= if null then 'a' else 'b' endif | b
