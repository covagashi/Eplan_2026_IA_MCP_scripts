---
title: "Setting up remote debugging in Eclipse"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecscripting_k_debug_setup_remote_debugging.htm"
file: "eecscripting_k_debug_setup_remote_debugging"
category: "eecscripting"
---

# Setting up remote debugging in Eclipse

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Setting up remote debugging in Eclipse To set up remote debugging in the Eclipse development environment, the following steps are necessary:
    1. Open the debug configuration dialog by selecting Run > Debug Configurations....
    1. Double-click Remote Java Application.
    1. Enter a name for the configuration (here IncrementLength, any name can be entered).
    2. Select the new project (plug-in) (here de.eplan.example).
    3. Enter a host (here locahost).
    4. Enter a port number (here 8000). The specification of the port must match the entry in the initialization file (for example -agentlib:jdwp=transport=dt_socket,address=8000,server=y,suspend=n).
You have to create a RUN configuration to be able to start EEC from the Eclipse environment:
    1. Double-click Eclipse Application.
    2. Enter a name for the RUN configuration (here EEC).
    3. Select de.eplan.eec.product.main_product from the drop-down list for Run a product.
    4. Select the current JDK for Execution environment.
    5. Start debugging with [Debug].
Eclipse opens the Debug perspective and starts EEC. If EEC has been closed it can be called up at any time again:
