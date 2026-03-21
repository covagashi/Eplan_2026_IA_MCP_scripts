---
title: "error(String errorText)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_function_error_string_errortext.htm"
file: "refformulas_r_function_error_string_errortext"
category: "refformulas"
---

# error(String errorText)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  error(String errorText) Functions This function triggers an exception. The error text to be displayed is passed as a string argument. error(String errorText)  
---  
Argument | String | errorText | Error text to display  
Return value |  |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
$Condition = '3'; =switch $Condition { case 1: 'a' case 2: 'b' else: error('Condition false') } | Condition false
