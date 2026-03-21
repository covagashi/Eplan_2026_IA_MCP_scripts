---
title: "Component absSapObject"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecsap_k_library_sap_architecture_abssapobject.htm"
file: "eecsap_k_library_sap_architecture_abssapobject"
category: "eecsap"
---

# Component absSapObject

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Component absSapObject

The abstract component absSapObjekt, or SapObject as an actual derivation of this component, is used as a wrapping object. Components that communicate with SAP can be installed (pre-instantiated) in these components.

In addition, scripts can be stored here that coordinate multiple mutually dependent functionBlock objects.

Specification of target system:

To be able to switch between different SAP systems, the parameters that define a connection must be stored in a file outside of the model. The file name extension is *.jcoDestination.

Language | jco.client.lang=en  
---|---  
Host system | jco.client.ashost=/H/212.14.236.15/H/172.168.0.20  
SAP user | jco.client.user=<User>  
System number | jco.client.sysnr=01  
Password | jco.client.passwd=<Password>  
Client | jco.client.client=100  
Maximum number of connections | jco.destination.pool_capacity=3  
  
### [Example](javascript:void\(0\);)

SAP-System | Client | Language | Name  
---|---|---|---  
APS | 200 | German | AP5_200_DE.jcoDestination  
T44 | 400 | English | T44_400_EN.jcoDestination  
  
In the initialization file, for example, ec.ini, the path to the jcoDestination file must be specified as follows:
    
        -Dde.eplan.sap.destination=AP5_200_DE
