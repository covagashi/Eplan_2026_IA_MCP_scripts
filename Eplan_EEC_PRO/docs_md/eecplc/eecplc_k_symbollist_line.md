---
title: "Lines"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_symbollist_line.htm"
file: "eecplc_k_symbollist_line"
category: "eecplc"
---

# Lines

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Lines

The line contains the parameters that are assigned the values that are to be included on the symbol list. The structure of the line is always platform-dependent. The following example shows a line for the symbol table in STEP 7 with replace variables.
    
        "M8B_Symbol_M8E","M8B_Adresse_M8E","M8B_Typ_M8E","M8B_Bezeichnung_M8E"

This line defines four parameters, all with the data type UNKNOWN_TYPE. In this example, it can clearly be seen that the replace variables are surrounded by two tokens which can be adjusted via the model variables in the PLC group.
