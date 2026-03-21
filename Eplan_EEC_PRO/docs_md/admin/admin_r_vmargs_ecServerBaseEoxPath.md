---
title: "com.mind8.ecserver.baseEOXPath"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_ecServerBaseEoxPath.htm"
file: "admin_r_vmargs_ecServerBaseEoxPath"
category: "admin"
---

# com.mind8.ecserver.baseEOXPath

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## com.mind8.ecserver.baseEOXPath

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dcom.mind8.ecserver.baseEOXPath=<absolute path to base models folder> |  Only for Web EEC  
**Annotation**  
Specifies an absolute path to a folder in which the result of a configuration is stored as a session model. Example:
    
        -Dcom.mind8.ecserver.baseEOXPath=C:\base\EOX  
  
### Tip

Environment variables of Windows are supported for this specification. Environment variables are enclosed by percentage signs, e.g. %WINDIR%. A percentage sign is masked by %% and can be used as part of a path specification.

Environment variables that cannot be broken up are listed in the ec.log log file and EEC terminates.
