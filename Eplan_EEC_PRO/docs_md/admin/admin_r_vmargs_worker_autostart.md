---
title: "de.eplan.eec.jobserver.worker.autostart"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_worker_autostart.htm"
file: "admin_r_vmargs_worker_autostart"
category: "admin"
---

# de.eplan.eec.jobserver.worker.autostart

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## de.eplan.eec.jobserver.worker.autostart

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dde.eplan.eec.jobserver.worker.autostart=<true/false> |  Only for Worker  
**Annotation**  
If the value is true (case insensitive) the Worker starts automatically on start and opens the Job Server perspective. If all conditions for execution of a job are met, the job execution starts immediately. Example:
    
        -Dde.eplan.eec.jobserver.worker.autostart=true
