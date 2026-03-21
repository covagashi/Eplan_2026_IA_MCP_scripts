---
title: "de.eplan.eec.rest.service.projectsfolder"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_rest_service_projectsfolder.htm"
file: "admin_r_vmargs_rest_service_projectsfolder"
category: "admin"
---

# de.eplan.eec.rest.service.projectsfolder

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## de.eplan.eec.rest.service.projectsfolder

The following EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dde.eplan.eec.rest.service.projectsfolder=<Path to projects folder> |  Only for eeLide  
**Annotation**  
Specifies the temporary folder for storing the configuration on the server's file system. Example:
    
        -Dde.eplan.eec.rest.service.projectsfolder=C:\TEMP\MyProjects  
  
### Tip

Environment variables of Windows are supported for this specification. Environment variables are enclosed by percentage signs, e.g. %WINDIR%. A percentage sign is masked by %% and can be used as part of a path specification.

Environment variables that cannot be broken up are listed in the ec.log log file and EEC terminates.
