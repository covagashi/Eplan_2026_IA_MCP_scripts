---
title: "PostgreSQL"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_datasources_database_postgresql.htm"
file: "eecbase_k_datasources_database_postgresql"
category: "eecbase"
---

# PostgreSQL

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## PostgreSQL

All table and column names are converted to lowercase letters: i.e., all table and column names are then expected in lowercase letters by the database as well.

If uppercase letters are to be supported as well, all SQL requests must be placed in quotes.

The style of the column names in the results corresponds to the table definition.

âselect customernumber from customerâ works.

âselect PartNumber from Partsâ does not function.

âselect âPartNumberâ from âPartsââ works.
