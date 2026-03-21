---
title: "Changing the symbol table resource file"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task3_edit_symboltable.htm"
file: "tutstep7_h_task3_edit_symboltable"
category: "tutstep7"
---

# Changing the symbol table resource file

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Changing the symbol table resource file The symbol table resource file will be filled with generic content. For this purpose, a directive must be inserted into the resource file instead of the previous symbol information.
    1. Select the SymbolTable symbol table.
    2. Select Edit POU > Fragment from the popup menu.
    3. Write the following content into the file:
    
        (*{LOOP:dos}*)(*{Call}*)(*{END_LOOP}*)

With the help of this instruction, the parser of the PLC discipline is iterated over all Call callups and the contents of the callups are added into the symbol table.
    1. Save the changes.
