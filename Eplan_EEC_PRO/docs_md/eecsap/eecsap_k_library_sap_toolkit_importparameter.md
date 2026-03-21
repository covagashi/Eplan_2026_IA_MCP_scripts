---
title: "Parameter ImportParameter"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecsap_k_library_sap_toolkit_importparameter.htm"
file: "eecsap_k_library_sap_toolkit_importparameter"
category: "eecsap"
---

# Parameter ImportParameter

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Parameter ImportParameter

The ImportParameter parameter contains individual parameters to be passed.

Syntax:
    
        =Map{
    	Pair{'HEADDATA',List{List{'MATERIAL','IND_SECTOR','MATL_TYPE','BASIC_VIEW'},
    	List{mc.$MaterialNumber,mc.$MaterialSector,mc.$MaterialType,'X'}}},
    	Pair{'CLIENTDATA',List{List{'BASE_UOM','BASE_UOM_ISO'},List{'ST','ST'}}},
    	Pair{'CLIENTDATAX',List{List{'BASE_UOM','BASE_UOM_ISO'},List{'X','X'}}}
    }
