---
title: "de.eplan.eec.jobserver.private.aliasurl"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_jobserver_privatealiasurl.htm"
file: "admin_r_vmargs_jobserver_privatealiasurl"
category: "admin"
---

# de.eplan.eec.jobserver.private.aliasurl

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## de.eplan.eec.jobserver.private.aliasurl

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dde.eplan.eec.jobserver.private.aliasurl=<URL> |  Only for Job Server and Worker  
**Annotation**  
Installation of Job Server and Job Server Worker on the same computer: The EEC argument is to be specified both for Job Server and for Job Server Worker. Installation of Job Server and one or more Job Server Workers on different computers: The EEC argument only has to be specified for the Job Server Worker. **Entered in the initialization file of a Job Server:** Address of a Job Server where it can be reached by Workers. Worker can register automatically at startup at this address. If the EEC argument -Dde.eplan.eec.jobserver.private.aliasurl is not specified, Job Server Workers automatically register themselves during the start at the address that is specified with the EEC argument -Dde.eplan.eec.jobserver.aliasurl. Example:
    
        -Dde.eplan.eec.jobserver.private.aliasurl=http://jobserverstation:8686

**Entered in the initialization file of Job Server Worker:** Job Server Workers register themselves during the start at this address. Job Server Workers make the created files available at this address. Example:
    
        -Dde.eplan.eec.jobserver.private.aliasurl=http://jobserverstation:8686  
  
### Tip

Environment variables of Windows are supported for this specification. Environment variables are enclosed by percentage signs, e.g. %WINDIR%. A percentage sign is masked by %% and can be used as part of a path specification.

Environment variables that cannot be broken up are listed in the ec.log log file and EEC terminates.
