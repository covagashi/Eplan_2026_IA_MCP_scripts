---
title: "Generate comments in calls"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_modelvar_plc_awx_codegen_calls.htm"
file: "admin_r_modelvar_plc_awx_codegen_calls"
category: "admin"
---

# Generate comments in calls

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Generate comments in calls

Path to model variable:

Disciplines > PLC > AutomationWorX > Code Generator

Select a Boolean value. The value determines whether block calls are provided with comments during the generation of the PLC code.

Valid values are true and false.

### [Example](javascript:void\(0\);)

Block call with comments (Value = true):
    
        Xaxis1(
    	moveForward := forward1,
    	moveBack := backward1,(* X-axis moves backward*)
    	inFront := inFront1,
    	inBack := inBack1,(* X-axis reached back position*)
    	forward => forward1,
    	Bus := Bus.No1(*Transportation*)
    	);

Block call without comments (Value = false):
    
        Xaxis1(
    	moveForward := forward1,
    	moveBack := backward1,
    	inFront := inFront1,
    	inBack := inBack1,
    	forward => forward1,
    	Bus := Bus.No1
    	);
