---
title: "derived()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_derived.htm"
file: "refformulas_r_derived"
category: "refformulas"
---

# derived()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  derived() Navigation methods for discipline-specific components Is used in the mechatronic structure to access the corresponding object in the discipline-specific structure (see [Project component navigation methods](refformulas_r_project_components_navigation.htm)). The result is <null> if the discipline-specific structure is not created, yet. derived()  
---  
Argument |  |  |   
Return value | Mechatronic object |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
mroot.rmos('WiringDiagram').first.derived | <<WiringDiagram_Feeder>>
