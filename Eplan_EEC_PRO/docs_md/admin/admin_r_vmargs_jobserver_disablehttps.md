---
title: "de.eplan.eec.jobserver.disablehttps"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_jobserver_disablehttps.htm"
file: "admin_r_vmargs_jobserver_disablehttps"
category: "admin"
---

# de.eplan.eec.jobserver.disablehttps

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## de.eplan.eec.jobserver.disablehttps

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dde.eplan.eec.jobserver.disablehttps=<true/false> |  Only for Job Server  
**Annotation**  
Activates/deactivates support of the https protocol for the project. Possible values are true and false.
    
        -Dde.eplan.eec.jobserver.disablehttps=true

Deactivates the support of the https protocol, the http protocol is used.
    
        -Dde.eplan.eec.jobserver.disablehttps=false

Activates support for the https protocol.  
  
### Read more

     * [de.eplan.eec.jobserver.httpsPort](admin_r_vmargs_jobserver_httpsport.htm)
