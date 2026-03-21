---
title: "hasValue()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_parameter_hasvalue.htm"
file: "refformulas_r_parameter_hasvalue"
category: "refformulas"
---

# hasValue()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  hasValue() Methods for Parameters The method hasValue() returns true if a value is entered, or false if the value of the parameter is empty. This allows the user to be indicated whether the value of a parameter was entered manually, or whether it is a formula result. hasValue()  
---  
Argument |  |  |   
Return value | Boolean |  true = a value exists false = a value does not exist  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
Feeder.Mechatronic.Feeder.parameter('Option_Inspect_available').hasValue | true
