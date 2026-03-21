---
title: "de.eplan.eec.jobserver.aliasurl"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_jobserver_aliasurl.htm"
file: "admin_r_vmargs_jobserver_aliasurl"
category: "admin"
---

# de.eplan.eec.jobserver.aliasurl

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## de.eplan.eec.jobserver.aliasurl

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dde.eplan.eec.jobserver.aliasurl=<URL> |  Only for Job Server and Worker  
**Annotation**  
The EEC argument is to be used optionally both for Job Server and for Worker. **Entered in the initialization file of a Job Server:** Reference to the address of the Job Server where it can be reached. Workers can register themselves automatically during the start at this address if the EEC argument -Dde.eplan.eec.jobserver.private.aliasurl is not specified. The user interface of the Job Server is represented under the specified address. Example:
    
        -Dde.eplan.eec.jobserver.aliasurl=http://jobserverstation:8686

If the EEC argument -Dde.eplan.eec.jobserver.aliasurl is not specified, the name of the computer is used. The name of the computer can reference an official name via DNS. **Entered in the initialization file of Workers:** Workers register themselves during the start at this address if the EEC argument -Dde.eplan.eec.jobserver.private.aliasurl is not specified. Only the EEC argument -Dde.eplan.eec.jobserver.private.aliasurl should be used for new installations!  
  
### Tip

Environment variables of Windows are supported for this specification. Environment variables are enclosed by percentage signs, e.g. %WINDIR%. A percentage sign is masked by %% and can be used as part of a path specification.

Environment variables that cannot be broken up are listed in the ec.log log file and EEC terminates.
