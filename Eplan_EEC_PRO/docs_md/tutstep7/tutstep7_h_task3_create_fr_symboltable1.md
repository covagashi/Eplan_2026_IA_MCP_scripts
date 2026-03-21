---
title: "Creating the resource file FR_SymbolTable"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task3_create_fr_symboltable1.htm"
file: "tutstep7_h_task3_create_fr_symboltable1"
category: "tutstep7"
---

# Creating the resource file FR_SymbolTable

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating the resource file FR_SymbolTable Two resource files are needed that can be created with any editor.
    1. Create the file FR_SymbolTable.sdf in the folder ..\installation folder\resources\Step7\.
    2. Write the following content into the file:
    
        FRAGMENT "FR_SymbolTable"
    VAR
    END_VAR
    BEGIN
    "M8B_Symbol_M8E","M8B_Address_M8E","M8B_DataType_M8E","M8B_Comment_M8E"
    END_FRAGMENT

    1. Save and close the file.
