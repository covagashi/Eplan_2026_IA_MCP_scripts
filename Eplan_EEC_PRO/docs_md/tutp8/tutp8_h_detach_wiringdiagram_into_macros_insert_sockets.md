---
title: "Insert sockets in page"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_detach_wiringdiagram_into_macros_insert_sockets.htm"
file: "tutp8_h_detach_wiringdiagram_into_macros_insert_sockets"
category: "tutp8"
---

# Insert sockets in page

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Insert sockets in page You must insert Sockets to ensure that the sensors can be placed by EEC when generating the page. Each socket defines a place on which a sensor (with plug) can be positioned. A macro can contain several sockets, but no more than one plug.
    1. Select the following commands: Tab Home > Command group Text > Insert.
    2. Enter the following text for the socket:
    
        #<Socket:Input1>

    1. Confirm with [OK].
    2. Position the text on the right above the PLC input, as shown in the following figure:
    1. Repeat the steps 1 o 5 for each further PLC input, and use ascending numbers for the socket (<Socket:Input2>, <Socket:Input3>, etc.). Alternatively you can copy the existing text via the commands Edit > Copy and Edit > Insert or paste it multiple times and adapt the texts.
