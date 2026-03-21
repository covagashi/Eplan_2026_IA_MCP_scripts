---
title: "Inserting code from subordinate discipline components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_programcode_insert_code_from_subcomponents.htm"
file: "eecplc_k_programcode_insert_code_from_subcomponents"
category: "eecplc"
---

# Inserting code from subordinate discipline components

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Inserting code from subordinate discipline components

To insert the code from child discipline components into the code of an POU, the Plug-Socket principle is used in the comments.

In accordance with this principle, the comment is completely replaced by the code of the child component whose plug matches the specified socket.

For this purpose, the comment must contain a Replace parameter that carries the name of the socket.

### [Example code](javascript:void\(0\);)
    
        // M8B_Socket:CodeSocket1_M8E

In graphics languages, comments can be created within the code area only in networks. For this reason, not only the comment, but also the completely marked network is erased.

It is possible to specify multiple socket markers within the code. At each position marked in this way, only the code of the child components whose plug matches this socket is inserted. If there are multiple matching socket markers (same name), then the code for all of these markers is added.

If the child component is a reference, then a call to its referenced component is inserted instead of the code.

For components that are written with the language Structured Text (ST), the Plug-Socket principle can be used both in line comments and also block comments.

### [Example code for line comment](javascript:void\(0\);)
    
        // M8B_Socket:CodeSocket1_M8E

### [Example code for block comment](javascript:void\(0\);)
    
        (*
    M8B_Socket:CodeSocket1_M8E
    *)

### [Example for replacement](javascript:void\(0\);)
    
        Replace-Parameter in Blockkommentar einer POU:
    IF g_ErrorQuit THEN Fault[0] := FALSE;
    END_IF;
    (*M8B_Socket:ST_Socket=Socket_ST_1_M8E*)
    IF STATION_ON AND NOT g_OmacAutoMoving THEN
    	(* limit MasterEncOffset to valid values *) 
    	tmpLreal := limit_Period();
    END_IF;

Code to be inserted in a child component with matching plug:
    
        InsertVar1 = 0
    IF A > 0 THEN OutVar := FALSE
    END_IF

POU with inserted code from child component:
    
        IF g_ErrorQuit THEN Fault[0] := FALSE;
    END_IF;
    InsertVar1 = 0
    IF A > 0 THEN OutVar := FALSE;
    END_IF
    IF STATION_ON[0] AND NOT g_OmacAutoMoving THEN
    	(* limit MasterEncOffset to valid values *)
    	tmpLreal := limit_Period();
    END_IF;
