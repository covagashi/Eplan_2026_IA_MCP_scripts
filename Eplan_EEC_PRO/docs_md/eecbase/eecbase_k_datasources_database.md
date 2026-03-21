---
title: "DatabaseDataSource"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_datasources_database.htm"
file: "eecbase_k_datasources_database"
category: "eecbase"
---

# DatabaseDataSource

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## DatabaseDataSource

A relational database is accessed via DatabaseDataSource:

The connection with a database is established via the Connection URL, also called URL connection string.

For access to external databases, explicit input fields are available for the user name and password. The password is saved in encrypted form; this way, it is not visible to users at any time.

### Note

Connections entered in the Connection URL field, including user name and password, represent a security risk, because these data appear in clear text in the log file! Use the user name and password only in the input fields of the same name.

### Note

The use of the jTDS JDBC driver for Microsoft SQL database connections allows authentication via Windows Authentication. To this purpose the specification of the useNTLMv2=true parameter is required (see <http://jtds.sourceforge.net/faq.html#urlFormat>).

### Note

As of EEC Version 2024 an updated Microsoft SQL database driver is provided by the EEC. Unlike the previous Microsoft SQL database driver, the updated driver encrypts the communication by default.

If the communication has been processed without encryption since then and if this is to be continued, the encryption=false option has to be inserted in the URL.

### Note

As of EEC Version 2023 a native Microsoft SQL database driver is provided by the EEC. The new Microsoft SQL database driver supports the TLS 1.2 encryption protocol. After the installation of the new Microsoft SQL database driver, the encryption protocol TLS 1.2 is activated by default.

The previously used database driver JDBC/jTDS only supports the connection to the Microsoft SQL Server with the encryption protocol TLS 1.0 and TLS 1.1.

The following table shows connection URLs for common databases with specification of the user and the password since this form is valid as well.

Database | TLS | Connection URL  
---|---|---  
1.0 | 1.1 | 1.2  
Microsoft SQL Server |  x | x | â |  jdbc:jtds:sqlserver://localhost:1433/databasename;user=username;password=password  
â | â | x |  jdbc:sqlserver://<Server name>:<Port number>;databaseName=<Database name>;  
Microsoft SQL Server with instance |  x | x | â | jdbc:jtds:sqlserver://localhost:1433/databasename;instance=instancename;user=username;password=password  
hsqldb | x | x | x | jdbc:hsqldb:hsql://localhost/xdb;user=user;password=password  
Oracle | x | x | x | jdbc:oracle:thin:username/password@localhost:1521/orcl  
PostgreSQL | x | x | x | jdbc:postgresql://localhost:5432/databasename?user=postgres&password=postgres  
  
### Note

Unicode support is available only for URLs that point to native JDBC drivers. The JDBC-ODBC bridge does not support Unicode.

If the Connection URL is written without stating the user name and password, no semicolon has to be added at the end.

In this case, the Connection URL for hsqldb is then, for example, jdbc:hsqldb:hsql://localhost/xdb.

The results of requests to external relational databases are returned as strings by default. Using the option Convert Integer, Double and Boolean, DatabaseDataSource can be set in such a way that the database column types of the external relational databases are converted to the primitive EEC data types Integer, Double and Boolean.

Depending on the database, there are special points to note:

The JDBC standard specifies the SQL types and a standard mapping on Java types. The respective JDBC driver specifies the mapping of native database types on the JDBC types. Finally, it depends on the database and the JDBC driver whether the primitive type conversion works 100%.

An example is the definition of the data type Bool in PostgreSQL: The Boolean data type is mapped to java.sql.Types.CHAR via the PostgreSQL-ODBC driver so that a conversion to the Boolean primitive type does not work.

Further information on SQL requests of various databases:

The different supported databases exhibit special characteristics in handling the uppercase / lowercase spelling of column and table names, which are shown below for each database. This is followed at the end by a recommendation concerning the choice of column / table names if there is to be an option to change databases.

The examples are based on a table called Parts with a column PartNumber, a table called SUPPLIERS with a column SUPPLIERNUMBER, and a table called Customers with a column CustomerNumber.

### [TLS support](javascript:void\(0\);)

### [Example](javascript:void\(0\);)
    
        jdbc:sqlserver;//DataServer_01:8085;databaseName=PartsDataBase;

You enter the values for the user and password in the editor for the data source object because these specifications are no longer supported in the connection URL.

The new drivers also support the sign-in via Windows authentication. To do this, add integratedSecurity=true to the connection URL.

### [Example](javascript:void\(0\);)
    
        jdbc:sqlserver;//DataServer_01:8085;databaseName=PartsDataBase;integratedSecurity=true;

If the Microsoft SQL server is configured accordingly, the specifications for

name and password of the signed-in user apply.

### [Microsoft SQL Server Express](javascript:void\(0\);)

The Microsoft SQL Server Express is created as an instance.

Syntax of the URL:
    
        jdbc:jtds:sqlserver://<Server name>/<Database name>;instance=SQLEXPRESS

### Note

Upper-case / lower-case differentiation is not relevant for the <Database name> specification.

The following settings are carried out by means of SQL Server Configuration Manager:

     * For the SQL Server activate the TCP/IP protocol.
     * For the SQL Native Clients activate the TCP/IP protocol.
     * Start the services SQL Server Browser and SQL Server (SQLEXPRESS).

The following settings have to be carried out by using the Microsoft SQL Server Management Studio:

     * Activate the Windows identifier.
     * Activate SQL-Login.

### [Microsoft SQL Server with instance](javascript:void\(0\);)

A local SQL login has to be specified for the login process.

You have to observe upper-case / lower-case spelling at both the server and the instance name.

There can be several instances of a Microsoft SQL Server database on a server. For such instances, the URL addresses must be extended to include additional properties. For more information on possible scenarios, visit the following web address:

<http://jtds.sourceforge.net/faq.html#urlFormat>

### Note

The entries for Connection URL, Default table, User and Password could be overwritten by means of EEC arguments. The EEC arguments are given in the initialization file (e.g.ec.ini).

### Read more

     * [de.eplan.eec.datasource.url](admin_r_vmargs_datasource_url.htm)
     * [de.eplan.eec.datasource.defaultTable](admin_r_vmargs_datasource_defaulttable.htm)
     * [de.eplan.eec.datasource.user](admin_r_vmargs_datasource_user.htm)
     * [de.eplan.eec.datasource.password](admin_r_vmargs_datasource_password.htm)
