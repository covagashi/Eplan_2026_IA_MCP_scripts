---
title: "Equal operator for components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_components_equal.htm"
file: "refformulas_r_components_equal"
category: "refformulas"
---

# Equal operator for components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Equal operator for components Equal operator. Base for the comparison is the components identity. The components identity is determined by the method absoluteName. Components are equal if their absoluteName is equal. **< Component1> = <Component2>**  
---  
Expressions | Component | Component1 | Component  
Component | Component2 | Component  
Return value | Boolean |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
this = this | true  
this = mos.first | false
