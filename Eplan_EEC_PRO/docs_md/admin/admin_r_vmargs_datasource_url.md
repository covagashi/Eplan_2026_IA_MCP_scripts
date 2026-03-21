---
title: "de.eplan.eec.datasource.url"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_datasource_url.htm"
file: "admin_r_vmargs_datasource_url"
category: "admin"
---

# de.eplan.eec.datasource.url

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## de.eplan.eec.datasource.url

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dde.eplan.eec.datasource.<absolute path to datasource object>.url=<URL> |  Optional  
**Annotation**  
By means of EEC arguments for the runtime environment the entries Connection URL, User, Password and Default table for a database component of the DatabaseDataSource type could be overruled. With the EEC argument de.eplan.eec.datasource.<absolute path to datasource object>.url an altered connection URL to the database is given. Example: A different connection URL to the database of the datasource component Databases.SQL.PartsDB should the assigned.
    
        -Dde.eplan.eec.datasource.Databases.SQL.PartsDB.url=jdbc:jtds:sqlserver://db-server-1/PartsDatabase  
  
### Tip

Environment variables of Windows are supported for this specification. Environment variables are enclosed by percentage signs, e.g. %WINDIR%. A percentage sign is masked by %% and can be used as part of a path specification.

Environment variables that cannot be broken up are listed in the ec.log log file and EEC terminates.

### Further information

     * [de.eplan.eec.datasource.defaultTable](admin_r_vmargs_datasource_defaulttable.htm)
     * [de.eplan.eec.datasource.user](admin_r_vmargs_datasource_user.htm)
     * [de.eplan.eec.datasource.password](admin_r_vmargs_datasource_password.htm)
