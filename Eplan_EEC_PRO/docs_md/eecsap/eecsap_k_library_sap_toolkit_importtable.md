---
title: "Parameter ImportTable"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecsap_k_library_sap_toolkit_importtable.htm"
file: "eecsap_k_library_sap_toolkit_importtable"
category: "eecsap"
---

# Parameter ImportTable

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Parameter ImportTable

The ImportTable parameter contains table structures to be passed.

Syntax:
    
        =Map{Pair{'MATERIALDESCRIPTION',List{
    List{'LANGU','LANGU_ISO','MATL_DESC'},
    List{'EN','EN',mc.$MaterialNameEN},
    List{'DE','DE',mc.$MaterialNameDE}

### [Example](javascript:void\(0\);)
    
        [SELECTIONCRITERIONSÂ»[[NAME_CHAR, CHAR_VALUE], [FREQUENCY, 50], [VOLTAGE, 400]]]
