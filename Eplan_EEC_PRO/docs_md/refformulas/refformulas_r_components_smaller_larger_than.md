---
title: "Unequal operator for components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_components_smaller_larger_than.htm"
file: "refformulas_r_components_smaller_larger_than"
category: "refformulas"
---

# Unequal operator for components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Unequal operator for components Unequal operator. Base for the comparison is the components identity. The components identity is determined by the method absoluteName. Components are unequal if their absoluteName is unequal. <Component1> <> <Component2>  
---  
Expressions | Component | Component1 | Component  
Component | Component2 | Component  
Return value | Boolean |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
this <> this | false  
this <> mos.first | true
