---
title: "General recommendation for the choice of column and table names"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_datasources_recommendations.htm"
file: "eecbase_k_datasources_recommendations"
category: "eecbase"
---

# General recommendation for the choice of column and table names

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## General recommendation for the choice of column and table names

The following recommendations refer to cases where the database is to be optionally changeable.

If all table and column names are only in uppercase letters, the SQL requests sent to most databases (exception: PostgreSQL) are compatible, without having to place table and column names in quotes.

Alternative:

Table and column names are always placed in quotes in SQL requests. This is compatible also with most databases. In the case of Oracle, however, keep in mind that the table was set up with uppercase / lowercase letters.

If in future there is to be a switch only between Microsoft products (Access and Microsoft SQL Server), there is no special style to be observed when choosing table and column names, because their behavior is identical.
