---
title: "ifError(Block block)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_common_iferror.htm"
file: "refformulas_r_common_iferror"
category: "refformulas"
---

# ifError(Block block)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  ifError(Block block) If an error occurs the result of the formula given with the argument block is returned. ifError(Block block)  
---  
Argument | Block | block | Formula, which returns an alternative result.  
Return value |  |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=List{null,1,2}.first.ifError('An error occurred!') | <<null>>
