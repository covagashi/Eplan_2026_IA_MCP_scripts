---
title: "Method transactionListCall()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecsap_k_methods_sap_interface_transactionlistcall.htm"
file: "eecsap_k_methods_sap_interface_transactionlistcall"
category: "eecsap"
---

# Method transactionListCall()

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Method transactionListCall()

The transactionListCall() method creates multiple calls that are passed as a List. The transactionListCall() method is defined in the library component SAPArchitecture.Methods.Native.

The method has the following arguments:

Argument | Type | Description  
---|---|---  
destination | String | Connection to be able to access SAP  
transactionList | List | List that contains a list of individual calls.  
  
The method callup has the following syntax:
    
        transactionListCall(destination, List{List{call1},List{call2},List{call3},...})

Each individual call is here a list that includes the following arguments:

Argument | Type | Description  
---|---|---  
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
changingParameter | Map | Data in one-dimensional format that the SAP module requires. The values are changed in comparison to importParameter.  
  
The method callup has the following syntax:
    
        transactionListCall(String destination, List transactionList)

A complete callup of the method has the following syntax:
    
        transactionListCall(destination, List{
    	List{ functionBlock1, importParameter1, importTable1, exportParamFilter1, exportTableFilter1, changingParameter1 },
    	List{ functionBlock2, importParameter2, importTable2, exportParamFilter2, exportTableFilter2, changingParameter2 },
    	List{ functionBlock3, importParameter3, importTable3, exportParamFilter3, exportTableFilter3, changingParameter3 },
    	â¦
    	}
    )
