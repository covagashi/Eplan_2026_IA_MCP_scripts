---
title: "de.eplan.eec.jobserver.httpsPort"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_jobserver_httpsport.htm"
file: "admin_r_vmargs_jobserver_httpsport"
category: "admin"
---

# de.eplan.eec.jobserver.httpsPort

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## de.eplan.eec.jobserver.httpsPort

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dde.eplan.eec.jobserver.httpsPort=<Port number> |  Only for Job Server  
**Annotation**  
Number of the port on which the Job Server is listening. This specification is only valid for connections using the https protocol. Example:
    
        -Dde.eplan.eec.jobserver.httpsPort=443  
  
### Read more

     * [de.eplan.eec.jobserver.disablehttps](admin_r_vmargs_jobserver_disablehttps.htm)
