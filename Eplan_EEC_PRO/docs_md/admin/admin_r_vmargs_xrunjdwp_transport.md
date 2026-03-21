---
title: "Xrunjdwp:transport"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_xrunjdwp_transport.htm"
file: "admin_r_vmargs_xrunjdwp_transport"
category: "admin"
---

# Xrunjdwp:transport

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## Xrunjdwp:transport

EEC argument |  Usage  
---|---  
-Xrunjdwp:transport=dt_socket, server=y, suspend=n, address=<port number> |  Only for eeLide  
**Annotation**  
To create a channel from the EEC runtime environment back to the EEC development environment for debugging purposes. Example:
    
        -Xrunjdwp:transport=dt_socket, server=y, suspend=n, address=5005
