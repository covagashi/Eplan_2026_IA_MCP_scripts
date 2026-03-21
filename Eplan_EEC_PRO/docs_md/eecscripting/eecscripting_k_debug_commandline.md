---
title: "Debugging via a command line"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecscripting_k_debug_commandline.htm"
file: "eecscripting_k_debug_commandline"
category: "eecscripting"
---

# Debugging via a command line

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Debugging via a command line

The debugging can also be executed via the console.

To do this enter the following command in the console:
    
    
    jdb -connect com.sun.jdi.SocketAttach:hostname=localhost,port=8000htr

The specification of the port must match the entry in the initialization file (for example -agentlib:jdwp=transport=dt_socket,address=8000,server=y,suspend=n).
