---
title: "selectionValues()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_parameter_selectionvalues.htm"
file: "refformulas_r_parameter_selectionvalues"
category: "refformulas"
---

# selectionValues()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  selectionValues() Methods for Parameters The method selectionValues() returns the selection values of a parameter which are defined in the related library component. If no selection values are defined, the method returns null. selectionValues()  
---  
Argument |  |  |   
Return value | List | List of selection values or null, if no selection value is defined for the parameter.  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
Feeder.Mechatronic.Feeder.parameter('Option_Inspect_available').selectionValues | [true, false]
