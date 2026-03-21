---
title: "de.eplan.eec.datasource.defaultTable"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_datasource_defaulttable.htm"
file: "admin_r_vmargs_datasource_defaulttable"
category: "admin"
---

# de.eplan.eec.datasource.defaultTable

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## de.eplan.eec.datasource.defaultTable

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dde.eplan.eec.datasource.<absolute path to datasource object>.defaultTable=<default table> |  Optional  
**Annotation**  
By means of EEC arguments for the runtime environment the entries Connection URL, User, Password and Default table for a database component of the DatabaseDataSource type could be overruled. By means of the EEC argument de.eplan.eec.datasource.<absolute path to datasource object>.defaultTable the name of the default table is given. Example: A different table name for the datasource component Databases.SQL.PartsDB should be used.
    
        -Dde.eplan.eec.datasource.Databases.SQL.PartsDB.defaultTable=Parts  
  
### Tip

Environment variables of Windows are supported for this specification. Environment variables are enclosed by percentage signs, e.g. %WINDIR%. A percentage sign is masked by %% and can be used as part of a path specification.

Environment variables that cannot be broken up are listed in the ec.log log file and EEC terminates.
