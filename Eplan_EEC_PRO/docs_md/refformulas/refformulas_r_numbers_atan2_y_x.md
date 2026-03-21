---
title: "atan2(y,x)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_numbers_atan2_y_x.htm"
file: "refformulas_r_numbers_atan2_y_x"
category: "refformulas"
---

# atan2(y,x)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  atan2(y,x) General methods for numbers Arc tangent of rectangular coordinates x and y in the range of -PI to PI in radians. Special cases:  
     * If both arguments are infinite, the result is also infinite.
     * If the first argument is positive zero and the second is positive, or the first argument is positive and finite and the second argument is positive infinity, the result is positive zero.
     * If the first argument is negative zero and the second is positive, or the first argument is negative and finite and the second argument is positive infinity, the result is negative zero.
     * If the first argument is positive zero and the second is negative, or the first argument is positive and finite and the second argument is negative infinity, the result is the double-value closest to PI.
     * If the first argument is negative zero and the second is negative, or the first argument is negative and finite and the second argument is negative infinity, the result is the double-value closest to -PI.
     * If the first argument is positive zero and the second is zero or negative zero, or the first argument is positive infinity and the second argument is finite, the result is the double-value closest to PI/2.
     * If the first argument is negative and the second is positive zero or negative zero, or the first argument is negative infinity and the second argument is infinite, the result is the double-value closest to -PI/2.
     * If both arguments are positive infinity, the result is the double-value closest to -PI/4.
     * If the first argument is positive infinity and the second argument is negative infinity, the result is the double-value closest to 3*PI/4.
     * If the first argument is negative infinity and the second argument is positive infinity, the result is the double-value closest to -PI/4.
     * If both arguments are negative infinity, the result is the double-value closest to -3*PI/4.
The result of the calculation must correspond to the exact result down to the last two decimal places. The results must be semi-monotonic. **atan2(y,x)**  
---  
Arguments | Integer/Double | y | Coordinate  
Integer/Double | x | Coordinate  
Return value | Double |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=atan2(PI()/2,1) | 1.0038848218538872
