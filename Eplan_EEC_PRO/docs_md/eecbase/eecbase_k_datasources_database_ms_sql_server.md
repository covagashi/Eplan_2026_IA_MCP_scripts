---
title: "Microsoft SQL Server"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_datasources_database_ms_sql_server.htm"
file: "eecbase_k_datasources_database_ms_sql_server"
category: "eecbase"
---

# Microsoft SQL Server

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Microsoft SQL Server

When Microsoft SQL Server is used, all tables and column names are handled case-insensitively. The table and column names can be in uppercase or lowercase letters.

Contrary to the spelling used in the database, the column names are supplied in the result in the same way as in the SQL statement:
    
        ..perform('select ARTIKELNUMMER from ARTIKEL').collect(x | x.ARTIKELNUMMER)
    ..perform('select Artikelnummer from Artikel').collect(x | x.Artikelnummer)

As for requests with an asterisk, all column names are supplied as specified in the database:
    
        ..perform('select * from Artikel').collect( x | x.Artikelnummer)

### Note

Microsoft Access behaves with SQL requests identically to Microsoft SQL Server.
