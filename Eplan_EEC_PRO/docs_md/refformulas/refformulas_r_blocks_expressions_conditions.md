---
title: "Block, expression, condition"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_blocks_expressions_conditions.htm"
file: "refformulas_r_blocks_expressions_conditions"
category: "refformulas"
---

# Block, expression, condition

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Block, expression, condition A block is a group of instructions (expressions) or conditions (conditions). An instruction (expression) is any construct of the formula language. [Example for the sortedBy(Block expression) method:](javascript:void\(0\);) Formula | Result  
---|---  
=List{'abc','c','bf'}.sortedBy(x|x.size) | [c, bf, abc]  
=List{'abc','c','bf'}.sortedBy(x|x.$Name) | [abc,bf,c]  
A condition (Condition) is a formula that must return a Boolean-type value. [Example for the method select(Block condition):](javascript:void\(0\);) Formula | Result  
---|---  
=Map{Pair{'A',1}, Pair{'B',2}}.select(x|x.key='A') | [AÂ»1]
