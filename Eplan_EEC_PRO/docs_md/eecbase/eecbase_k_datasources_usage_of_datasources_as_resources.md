---
title: "Using data sources as resources"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_datasources_usage_of_datasources_as_resources.htm"
file: "eecbase_k_datasources_usage_of_datasources_as_resources"
category: "eecbase"
---

# Using data sources as resources

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Using data sources as resources

External databases (Oracle, SQL server, etc.) with large data volumes continue to be maintained externally. Frequently, though, there are transparent models, for example, simple tables, where wire cross-sections are specified, certain part data are managed, etc. For such data formats (CSV files, MDL files, etc.), it often makes sense to transfer management to EEC.

All data sources, except DatabaseDataSource (with a Connection URL), therefore, are integrated into EEC in a manner similar to a new discipline. This has the following advantages:

     * Data sources can be edited with the respective editors and are managed like discipline resources.
     * The editor to be used can be set in Eclipse via the file extensions.
     * The data can be internalized in the model.
     * Editing via Edit Resource is possible. Any open database connections will be closed automatically in the process.
     * As with other disciplines, a default resource folder can be defined in the settings:

The settings for the connection pool are listed in detail in the following table.

Parameter name | Default value | Description  
---|---|---  
Initial connection pool size | 1 | Number of connections to be captured at the start. This number should be greater than the minimum number, and less than the maximum size of the connection pool.  
Minimum size of the connection pool | 0 | Minimum number of connections that are served simultaneously.  
Maximum size of the connection pool | 3 | Maximum number of connections that are served simultaneously.  
Increment for pool increase | 2 | Number of connections that are added when the connection pool is exhausted.  
Maximum idle time of a connection in the pool | 300 | Time in seconds during which an unused connection remains in the pool until it is deleted.  
Maximum age of a connection in the pool | 28800 | Absolute time in seconds during which a connection exists in the pool before it is disconnected and deleted. Connections with few unused times are also removed. The maximum age is set to 0 by default.  
Retry attempts | 5 | Number of connection attempts before it is abandoned. If the attempt to connect is never to be abandoned, 0 must be entered.  
Pause between connection attempts | 1000 | Time in milliseconds between two connection attempts.
