---
title: "Data sources"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_prefs_datasources.htm"
file: "admin_r_prefs_datasources"
category: "admin"
---

# Data sources

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Data sources

Path to the preferences:

Menu Window > Preferences

Dialog Preferences > Disciplines > Data sources

     * The Resources folder specifies which folder is initially searched for data files.

Default value: <EEC installation folder>\resources\DataSources

The absolute path is shown below the input field.

     * The Resources folder specifies which folder is initially searched for data files.
     * To allow the output of warnings of the OpenOffice Quickstarter, the Show OpenOffice Quickstarter warnings has to be marked. This option is enabled by default.
     * The Initial connection pool size indicates how many connections are allowed from the start of the EEC. The default is 1.
     * The specification of the Minimum size of the connection pool can be used to specify how many connections are allowed as a minimum. The default is 0.
     * To restrict the data traffic the specification of the Maximum size of the connection pool can be used to specify how many connections at a maximum can be permitted parallel. The default is 3.
     * If the number of connections has to be increased, this can be carried out in steps that are specified with the specification Increment for pool increase. The default is 2.
     * After the expiry of time for Maximum idle time of a connection in the pool (in seconds) the connection to a data source is closed. The default is 300.
     * After the expiry of time for Maximum age of a connection in the pool (in seconds) the connection to a data source is closed. The default is 28800.
     * After the indicated Number of connection attempts the resumption of a connection attempt is canceled and an error message output. The default is 5.
     * A Pause between connection attempts (in milliseconds) prevents a too rapid resumption of a connection attempt for connection problems. The default is 1000.
     * The option Protocoled SQL queries for quality feedback report activates the entry of warnings and errors in a protocol file to send these to Eplan. This option is not enabled by default.
