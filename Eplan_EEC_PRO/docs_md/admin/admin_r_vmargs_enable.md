---
title: "com.mind8.script.debug.modus.enable"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_enable.htm"
file: "admin_r_vmargs_enable"
category: "admin"
---

# com.mind8.script.debug.modus.enable

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## com.mind8.script.debug.modus.enable

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dcom.mind8.script.debug.modus.enable=<true/false> |  Optional  
**Annotation**  
Activates/deactivates the script debug mode. Possible values are true and false.
    
        -Dcom.mind8.script.debug.modus.enable=true

Activates the script debug mode.
    
        -Dcom.mind8.script.debug.modus.enable=false

Deactivates the script debug mode.  
  
### Tip

Environment variables of Windows are supported for this specification. Environment variables are enclosed by percentage signs, e.g. %WINDIR%. A percentage sign is masked by %% and can be used as part of a path specification.

Environment variables that cannot be broken up are listed in the ec.log log file and EEC terminates.
