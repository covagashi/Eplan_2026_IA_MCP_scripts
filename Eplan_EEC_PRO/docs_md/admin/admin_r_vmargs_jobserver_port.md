---
title: "de.eplan.eec.jobserver.port"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_jobserver_port.htm"
file: "admin_r_vmargs_jobserver_port"
category: "admin"
---

# de.eplan.eec.jobserver.port

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## de.eplan.eec.jobserver.port

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dde.eplan.eec.jobserver.port=<Port number> |  Only for Job Server  
**Annotation**  
Number of the port on which the Job Server is listening. This specification is only valid for connections using the http protocol. Example:
    
        -Dde.eplan.eec.jobserver.port=8686
