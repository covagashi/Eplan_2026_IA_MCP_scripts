---
title: "de.eplan.eec.jobserver.worker.jobdefinitionsfolder"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_worker_jobdefinitionsfolder.htm"
file: "admin_r_vmargs_worker_jobdefinitionsfolder"
category: "admin"
---

# de.eplan.eec.jobserver.worker.jobdefinitionsfolder

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## de.eplan.eec.jobserver.worker.jobdefinitionsfolder

The following EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dde.eplan.eec.jobserver.worker.jobdefinitionsfolder=<Path name (UNC)> |  Only for Worker  
**Annotation**  
The file folder where job definitions for this Worker are stored. The folder can also be specified as a UNC path. Example:
    
        -Dde.eplan.eec.jobserver.worker.jobdefinitionsfolder=\\myShare\jobserver\jobdefinitions  
  
### Tip

Environment variables of Windows are supported for this specification. Environment variables are enclosed by percentage signs, e.g. %WINDIR%. A percentage sign is masked by %% and can be used as part of a path specification.

Environment variables that cannot be broken up are listed in the ec.log log file and EEC terminates.
