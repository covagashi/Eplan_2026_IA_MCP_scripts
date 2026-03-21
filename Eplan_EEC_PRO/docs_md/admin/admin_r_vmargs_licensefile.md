---
title: "de.eplan.eec.licenseFile"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_licensefile.htm"
file: "admin_r_vmargs_licensefile"
category: "admin"
---

# de.eplan.eec.licenseFile

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## de.eplan.eec.licenseFile

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dde.eplan.eec.licenseFile=<absolute path to license file> |  Only for Job Server  
**Annotation**  
The EEC argument is to be used optionally only for the Job Server. In the case of the execution of the Job Server without a user interface the specification of a license default settings file is mandatory. Example:
    
        -Dde.eplan.eec.licenseFile=C:/Users/Public/EPLAN/2_7_4_20180621_2041/license.lis  
  
### Tip

Environment variables of Windows are supported for this specification. Environment variables are enclosed by percentage signs, e.g. %WINDIR%. A percentage sign is masked by %% and can be used as part of a path specification.

Environment variables that cannot be broken up are listed in the ec.log log file and EEC terminates.
