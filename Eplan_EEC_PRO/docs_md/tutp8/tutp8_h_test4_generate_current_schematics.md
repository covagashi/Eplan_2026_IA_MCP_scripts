---
title: "Generating the current status of the schematic"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_test4_generate_current_schematics.htm"
file: "tutp8_h_test4_generate_current_schematics"
category: "tutp8"
---

# Generating the current status of the schematic

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Generating the current status of the schematic This test shows that by determining the values for the plugs and sockets by way of the formulas, all sensors can initially be placed again. If the Inspect function group is deactivated, there must not be any gaps between the sensors.
    1. Generate the ECAD structure again.
    2. The structure consists of 2 pages that contain 8 or 2 sensors.
    3. Open the schematic again.
    4. The schematic consists of 2 pages where all sensors are available.
    5. The pages now have names.
    6. Close P8 and disable again the Inspect function group by setting the Option_Inspect_available to false.
    7. Generate the ECAD structure once again.
    8. The schematic consists of the PLC_Sensors_1_8_Feeder page that contains 7 sensors, and the PLC_Sensors_9_16_Feeder page that does not contain any sensors.
    9. Open the schematic again.
    10. On the first page of the schematic, one can see that the PLC inputs are now assigned without any gaps. On the second page, all PLC inputs are unconnected. Thus, the second page is not required, and is to be disabled by means of a formula in the next step.
Upon closer inspection, one can see that the device tags and function texts are still represented by <null>. For these elements, too, formulas must still be entered.
