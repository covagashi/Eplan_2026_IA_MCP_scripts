---
title: "com.mind8.remote.server.repository.file"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_remoteServerRepositoryFile.htm"
file: "admin_r_vmargs_remoteServerRepositoryFile"
category: "admin"
---

# com.mind8.remote.server.repository.file

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## com.mind8.remote.server.repository.file

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dcom.mind8.remote.server.repository.file=<absolute path to session models folder> |  Only for Web EEC  
**Annotation**  
Specifies an absolute path to a folder in which the EOX files of the sessions are stored. Example:
    
        -Dcom.mind8.remote.server.repository.file=C:\SessionModels  
  
### Tip

Environment variables of Windows are supported for this specification. Environment variables are enclosed by percentage signs, e.g. %WINDIR%. A percentage sign is masked by %% and can be used as part of a path specification.

Environment variables that cannot be broken up are listed in the ec.log log file and EEC terminates.
