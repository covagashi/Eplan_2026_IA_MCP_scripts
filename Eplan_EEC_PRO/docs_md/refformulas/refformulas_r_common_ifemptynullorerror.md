---
title: "ifEmptyNullOrError(Block block)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_common_ifemptynullorerror.htm"
file: "refformulas_r_common_ifemptynullorerror"
category: "refformulas"
---

# ifEmptyNullOrError(Block block)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  ifEmptyNullOrError(Block block) Returns the result of the formula given with the argument block if one of the following conditions is met:  
     * The receiver is null.
     * The receiver is an empty collection or map.
     * An error occurred while determining the receiver.
ifEmptyNullOrError(Block block)  
---  
Argument | Block | block | Formula, which returns an alternative result.  
Return value |  |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=List{}.ifEmptyNullOrError(List{'default'}) | [default]
