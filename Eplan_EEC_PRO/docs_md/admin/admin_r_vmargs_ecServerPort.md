---
title: "com.mind8.ecserver.port"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_ecServerPort.htm"
file: "admin_r_vmargs_ecServerPort"
category: "admin"
---

# com.mind8.ecserver.port

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## com.mind8.ecserver.port

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dcom.mind8.ecserver.port=<Port number> |  Only for Web EEC  
**Annotation**  
Number of the port on which the Web EEC Server is listening. Example:
    
        -Dcom.mind8.ecserver.port=7171  
  
### Tip

Environment variables of Windows are supported for this specification. Environment variables are enclosed by percentage signs, e.g. %WINDIR%. A percentage sign is masked by %% and can be used as part of a path specification.

Environment variables that cannot be broken up are listed in the ec.log log file and EEC terminates.
