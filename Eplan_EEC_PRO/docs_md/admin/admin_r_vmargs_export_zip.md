---
title: "com.mind8.export.zip"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_export_zip.htm"
file: "admin_r_vmargs_export_zip"
category: "admin"
---

# com.mind8.export.zip

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## com.mind8.export.zip

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dcom.mind8.export.zip=<File name> |  Optional  
**Annotation**  
Through this argument, the XMLExportApplication learns the path and name of the file to which the model must be exported. Example:
    
        -Dcom.mind8.export.zip=exportedDB.zip  
  
### Tip

Environment variables of Windows are supported for this specification. Environment variables are enclosed by percentage signs, e.g. %WINDIR%. A percentage sign is masked by %% and can be used as part of a path specification.

Environment variables that cannot be broken up are listed in the ec.log log file and EEC terminates.
