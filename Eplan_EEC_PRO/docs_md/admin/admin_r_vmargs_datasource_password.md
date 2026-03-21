---
title: "de.eplan.eec.datasource.password"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_datasource_password.htm"
file: "admin_r_vmargs_datasource_password"
category: "admin"
---

# de.eplan.eec.datasource.password

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## de.eplan.eec.datasource.password

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dde.eplan.eec.datasource.<absolute path to datasource object>.password=<password> |  Optional  
**Annotation**  
By means of EEC arguments for the runtime environment the entries Connection URL, User, Password and Default table for a database component of the DatabaseDataSource type could be overruled. The user password for the database is specified by the EEC argument de.eplan.eec.datasource.<absolute path to datasource object>.password. Example: The password to access the database of the datasource component Databases.SQL.PartsDB should be altered.
    
        -Dde.eplan.eec.datasource.Databases.SQL.PartsDB.password=xvfs45hj2N_7d  
  
### Tip

Environment variables of Windows are supported for this specification. Environment variables are enclosed by percentage signs, e.g. %WINDIR%. A percentage sign is masked by %% and can be used as part of a path specification.

Environment variables that cannot be broken up are listed in the ec.log log file and EEC terminates.
