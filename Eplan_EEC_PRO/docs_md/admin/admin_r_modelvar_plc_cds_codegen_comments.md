---
title: "Replacing nested comments"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_modelvar_plc_cds_codegen_comments.htm"
file: "admin_r_modelvar_plc_cds_codegen_comments"
category: "admin"
---

# Replacing nested comments

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Replacing nested comments

Path to model variable:

Disciplines > PLC > CoDeSys > Code Generator

Select a Boolean value. The value determines whether signs that can be interpreted as start and end signs for comments and that occur within comments can be replaced.

Valid values are true and false.

### [Example](javascript:void\(0\);)

Value of the model variable is true.

PLC code of the resource:
    
        (*
    moveForward: BOOL; (* X-axis moves forward*)
    *)

In the created PLC code the inner signs (* and *) are replaced by [* and *]:
    
        (*
    moveForward: BOOL; [* X-axis moves forward*]
    *)
