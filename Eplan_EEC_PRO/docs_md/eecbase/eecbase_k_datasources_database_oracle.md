---
title: "Oracle"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_datasources_database_oracle.htm"
file: "eecbase_k_datasources_database_oracle"
category: "eecbase"
---

# Oracle

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Oracle

In an Oracle database, the column names are by default case-insensitive, i.e., uppercase / lowercase spelling does not matter. Internally, Oracle enters the column names in uppercase letters â and this is how they are also received in the EEC.

In this mode, it does not matter for SQL requests whether column and table names are spelled with uppercase or lowercase letters. When accessing the requested data, all column names must be entered in uppercase letters.
    
        ...perform('select * from Artikel ').collect( x | x.ARTIKELNUMMER)

Oracle is also capable of stating column names as case-sensitive by placing them in quotes in the Create Table statements or by selecting the Maintain Case-Sensitivity check box in the object browser when creating tables.

In this case, all SQL requests must also be placed between apostrophes:
    
        ..perform('select "Artikelnummer" from "Artikel"').collect(x | x.Artikelnummer)
