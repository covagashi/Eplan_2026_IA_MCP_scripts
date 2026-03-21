---
title: "de.eplan.eec.headless"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_headless.htm"
file: "admin_r_vmargs_headless"
category: "admin"
---

# de.eplan.eec.headless

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## de.eplan.eec.headless

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dde.eplan.eec.headless=<true/false> |  Only for Job Server  
**Annotation**  
The EEC argument is to be used optionally only for the Job Server. It is currently not approved for Worker! With this argument EEC is either executed with the interface (Value = false) or without the interface (Value = true). Without this EEC argument in the initialization file it is always executed with the interface. In the case of an execution without a user interface the specification of a license default settings file is mandatory (see [de.eplan.eec.licenseFile](admin_r_vmargs_licensefile.htm)). Possible values are true and false, meaning
    
        -Dde.eplan.eec.headless=true

or
    
        -Dde.eplan.eec.headless=false
