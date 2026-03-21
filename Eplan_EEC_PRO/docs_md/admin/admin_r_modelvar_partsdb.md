---
title: "Parts database"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_modelvar_partsdb.htm"
file: "admin_r_modelvar_partsdb"
category: "admin"
---

# Parts database

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Parts database

Path to model variable:

Disciplines > ECAD > Eplan Electric P8 > Parts database

In order to work with Eplan Pro Panel, it must be possible to access the parts database. There are corresponding methods for this in the formula language, as well as model variables.

The advantage of the model variables is that the required data is not only determined during the generation.

### Note

These model variables are not assigned to parameter names, but the required values are directly entered.

### Note

Changes to the model variables for the parts database do not become effective until after a restart of the EEC because they are read in during the start. When P8 or Pro Panel is started, the model variables are transferred to the P8 or Pro Panel application respectively.

Model variable  
---  
SQL user name  
SQL catalog  
SQL password  
SQL Server  
  
### Note

If there is no specification for the model variables, the parts database that is specified in the options of P8 under User > Management > Parts is accessed.

Access to the database can be carried out either by a database user who has to carry out corresponding specifications for authorizations, or by a user who authorizes themselves through their Windows login. The following tables show which specifications are required respectively (values are only examples).

The following specifications are required in the case of a Windows authorization:

Model variable | Value  
---|---  
SQL user name |   
SQL catalog | DataBaseName  
SQL password |   
SQL Server | ServerName\SQLEXPRESS  
  
The following specifications are required in the case of an SQL Server Authentication:

Model variable | Value  
---|---  
SQL Username | LoginName  
SQL catalog | DataBaseName  
SQL password | ***  
SQL Server | ServerName\SQLEXPRESS  
  
The password is displayed represented by asterisks.
