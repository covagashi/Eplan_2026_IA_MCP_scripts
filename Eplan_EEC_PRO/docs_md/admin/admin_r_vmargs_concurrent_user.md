---
title: "com.mind8.eobroker.concurrent.user"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_concurrent_user.htm"
file: "admin_r_vmargs_concurrent_user"
category: "admin"
---

# com.mind8.eobroker.concurrent.user

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## com.mind8.eobroker.concurrent.user

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dcom.mind8.eobroker.concurrent.user=<User name> |  Optional  
**Annotation**  
Statement of the user name. By default, the login name of the operating system is used.  
  
### Tip

Environment variables of Windows are supported for this specification. Environment variables are enclosed by percentage signs, e.g. %WINDIR%. A percentage sign is masked by %% and can be used as part of a path specification.

Environment variables that cannot be broken up are listed in the ec.log log file and EEC terminates.
