---
title: "hsqldb"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_datasources_database_hsqldb.htm"
file: "eecbase_k_datasources_database_hsqldb"
category: "eecbase"
---

# hsqldb

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## hsqldb

User name and password must always be provided in uppercase letters so as to allow for access from the EEC.

Table and column names are always converted to uppercase letters for SQL requests. If this is not desired, they will have to be placed in quotes (").

Examples:

'select PartNumber from Parts' does not function: Error message: Table 'PARTS' does not exist.

'select PartNumber from "Parts'" does not function: Error message: Column 'PARTNUMBER' does not exist.

'select "PartNumber" from "Part"' works.

'select SupplierNumber from Suppliers' works.

'select SupplierNumber from Suppliers' works.

The column names in the query results are case-sensitive, i.e., they must be precisely as stated in the database:
    
        ...perform('select "Artikelnummer" from "Artikel"').collect(x|x.Artikelnummer)
    ...perform('select Lieferantennummer from Lieferanten').collect(x|x.LIEFERANTENNUMMER)

### Note

OpenOffice Base behaves exactly like hsqldb in the case of SQL requests.
