---
title: "de.eplan.eec.global.resourcePath"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_global_resourcePath_new.htm"
file: "admin_r_vmargs_global_resourcePath_new"
category: "admin"
---

# de.eplan.eec.global.resourcePath

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## de.eplan.eec.global.resourcePath

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dde.eplan.eec.global.resourcePath=<File name> |  Optional  
**Annotation**  
Specifies a resource path from which relative paths can be set for the individual disciplines in the settings. Example:
    
        -Dde.eplan.eec.global.resourcePath=C:\Users\Public\EPLAN\EngineeringConfiguration\2022_1\resources

In the settings, the resource path can be entered for each discipline, starting from this folder, e.g., \ECAD.  
  
### Tip

Environment variables of Windows are supported for this specification. Environment variables are enclosed by percentage signs, e.g. %WINDIR%. A percentage sign is masked by %% and can be used as part of a path specification.

Environment variables that cannot be broken up are listed in the ec.log log file and EEC terminates.
