---
title: "Data source objects"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_datasources_datasourceobjects.htm"
file: "eecbase_k_datasources_datasourceobjects"
category: "eecbase"
---

# Data source objects

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Data source objects

Data sources are, like disciplines (ECAD, PLC, etc.), are integrated into the system by way of a separate system library:

To use data sources, the DataSource system library must be imported into the modular system.

The following figure shows the inheritance hierarchy:

The base object DataSource becomes specialized in CSV sources and relational sources. In the case of relational sources, one distinguishes between any relational databases (DatabaseDataSource) and specific data sources (OpenOffice).

The methods for access to external data sources are documented in the formula collection (see chapter [Data source objects]()).

The special characteristics of the individual data source objects are described in the following subsections
