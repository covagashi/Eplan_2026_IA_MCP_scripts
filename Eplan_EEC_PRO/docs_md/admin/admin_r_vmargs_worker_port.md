---
title: "de.eplan.eec.jobserver.worker.port"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_worker_port.htm"
file: "admin_r_vmargs_worker_port"
category: "admin"
---

# de.eplan.eec.jobserver.worker.port

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## de.eplan.eec.jobserver.worker.port

The following EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dde.eplan.eec.jobserver.worker.port=<Port number> |  Only for Worker  
**Annotation**  
Number of the port on which the Worker is listening. Example:
    
        -Dde.eplan.eec.jobserver.worker.port=8686
