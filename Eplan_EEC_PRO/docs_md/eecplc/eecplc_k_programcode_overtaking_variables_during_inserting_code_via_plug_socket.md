---
title: "Applying variables when code is inserted in accordance with the Plug-Socket principle"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_programcode_overtaking_variables_during_inserting_code_via_plug_socket.htm"
file: "eecplc_k_programcode_overtaking_variables_during_inserting_code_via_plug_socket"
category: "eecplc"
---

# Applying variables when code is inserted in accordance with the Plug-Socket principle

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Applying variables when code is inserted in accordance with the Plug-Socket principle

If the code of one component is inserted into another in CoDeSysV3 in accordance with the Plug-Socket principle (e.g., insert networks), in addition to the inserted code, all of the variables not already present in the variable declaration of the inserting component are passed. An already declared variable is not written again, regardless of what declaration area (e.g., VAR_INPUT) it is located in or which data type the variable has in the two components.

All of the variables are passed, regardless of whether these are used in the inserted code or not.

Variable declarations with comment in the same line are passed completely into the code of the inserted component. This also applies for block comments that begin in the same line of the variable declarations.

### [Example for variable application](javascript:void\(0\);)

Declaration of the inserting component before the variables are passed:
    
        PROGRAMM Basis_ST
    VAR_INPUT
    	InVar1: BOOL;
    END_VAR
    
        VAR
    	Var1: BOOL;
    	// comment
    	VAR2: INT;
    END_VAR

Declaration of the component to be inserted:
    
        PROGRAMM Insert_ST
    VAR
    	Var1: BOOL;
    	// comment
    	InsVAR1: BOOL; // comment to InsVar1
    	InsVAR2: INT; (* block comment
    	to InsVAR2*)
    	// free comment
    END_VAR

Declaration of the inserting component after the variables have been passed:
    
        PROGRAMM Basis_ST
    VAR_INPUT
    	InVar1: BOOL;
    END_VAR
    
        VAR
    	Var1: BOOL;
    	// comment
    	VAR2: INT;
    	InsVAR1: BOOL; // comment to InsVar1
    	InsVAR2: INT; (* block comment
    	to InsVAR2*)
    END_VAR

If all of the variables for which there is no declaration area in the inserting component are inserted, the declaration area, including the variable declaration, is inserted.

Declaration areas with flags (CONSTANT, PERSISTENT, and/or RETAIN) are handled as standalone declaration areas, with the following declaration equations applying:
    
        PERSISTENT <=> PERSISTENT RETAIN <=> RETAIN PERSISTENT

Examples for explaining declaration equalities/inequalities:

VAR_INPUTdoes not equalVAR

VAR does not equal VAR CONSTANT

VAR_OUTPUT PERSISTENT RETAIN equals VAR_OUTPUT PERSISTENT
