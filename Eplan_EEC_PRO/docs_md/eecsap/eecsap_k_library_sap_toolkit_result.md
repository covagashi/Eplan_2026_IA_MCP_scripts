---
title: "Parameter Result"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecsap_k_library_sap_toolkit_result.htm"
file: "eecsap_k_library_sap_toolkit_result"
category: "eecsap"
---

# Parameter Result

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Parameter Result

The Result parameter contains the returned object of the query.

That object that an SAP function module returns is a list that contains, in turn, three lists. Depending on the function module, however, the lists are filled very differently and are therefore divided into different types as the following table shows.

|  | List 1 | List 2 | List 3 | List 4 | Example  
---|---|---|---|---|---|---  
Type 1 | S | Object RETURN with status (E, S, etc.), message, etc. | Values | Changing parameter values | <<null>> | BAPI_MATERIAL_GETINTNUMBER, BAPI_MATERIAL_SAVEDATA  
| E | <<null>>  
Type 2 | S | Return value | Values | Changing parameter values | <<null>> | CCAP_ECN_HEADER_CREATE  
| E | <<null>> | <<null>> | <<null>> | EXCEPTION object  
Type 3 | S | Return status (1 for success, "" for error) | Among other things, a multi-line object RETURN with status (E, S, etc.), message, etc. | Changing parameter values | <<null>> | BAPI_OBJCL_CREATE  
| E | <<null>>  
  
S=Success

E=Error

Information, success and error messages of one or more modules can be displayed as shown in the following figure:
