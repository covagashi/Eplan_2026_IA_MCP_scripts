---
title: "Method simpleCall()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecsap_k_methods_sap_interface_simplecall.htm"
file: "eecsap_k_methods_sap_interface_simplecall"
category: "eecsap"
---

# Method simpleCall()

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Method simpleCall()

The simpleCall() method creates a simple callup with transaction management (Commit, Rollback) and is suitable for writing data. After each Call, the BAPI_TRANSACTION_COMMIT or the BAPI_TRANSACTION_ROLLBACK is initiated. The simpleCall() method is defined in the library component SAPArchitecture.Methods.Native.

The method has the following arguments:

Argument | Type | Description  
---|---|---  
destination | String | Connection to be able to access SAP  
functionBlock | String | Name of function module  
importParameter | Map | Data in one-dimensional format that the SAP module requires.  
importTable | Map | Data in multi-dimensional format that the SAP module requires.  
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
  
The method callup has the following syntax:
    
        simpleCall(String destination, String functionBlock, Map importParameter, Map importTable, List exportParamFilter, List exportTableFilter, Map changingParameter)
