---
title: "Modifying the EEC initialization file"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecscripting_k_debug_edit_initializing_file.htm"
file: "eecscripting_k_debug_edit_initializing_file"
category: "eecscripting"
---

# Modifying the EEC initialization file

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Modifying the EEC initialization file The initialization file (for example ec.ini) of the EEC to be debugged has to be added with the following rows below the row -vmargs:
    
        -agentlib:jdwp=transport=dt_socket,address=8000,server=y,suspend=n
    -Xmx1024m

Once the initialization file has been modified, EEC has to be restarted.
