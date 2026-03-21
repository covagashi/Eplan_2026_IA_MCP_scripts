---
title: "Method simpleQuery()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecsap_k_methods_sap_interface_simplequery.htm"
file: "eecsap_k_methods_sap_interface_simplequery"
category: "eecsap"
---

# Method simpleQuery()

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Method simpleQuery()

The simpleQuery() method creates a simple callup without transaction management (Commit, Rollback) and is suitable for querying data. The simpleQuery() method is defined in the library component SAPArchitecture.Methods.Native.

The method has the following arguments:

Argument | Type | Description  
---|---|---  
changingParameter | Map | Data in one-dimensional format that the SAP module requires. The values are changed in comparison to importParameter.  
destination | String | Connection to be able to access SAP.  
exportParamFilter | List | Filter that should return data of the SAP module.  
Not specified:  
All data that the SAP module provides is returned.  
Limitation:  
Only the data of the SAP module that was requested will be returned.  
exportTableFilter | List | Filter that should return data of the SAP module.  
Not specified:  
All data that the SAP module provides is returned.  
Limitation:  
Only the data of the SAP module that was requested will be returned.  
functionBlock | String | Name of function module.  
importParameter | Map | Data in one-dimensional format that the SAP module requires.  
importTable | Map | Data in multi-dimensional format that the SAP module requires.  
  
The method callup has the following syntax:
    
        simpleQuery(String destination, String functionBlock, Map importParameter, Map importTable, List exportParamFilter, List exportTableFilter, Map changingParameter)
