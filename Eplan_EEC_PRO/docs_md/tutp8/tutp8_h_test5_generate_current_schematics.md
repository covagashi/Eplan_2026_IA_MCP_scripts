---
title: "Generating the finished schematic"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_test5_generate_current_schematics.htm"
file: "tutp8_h_test5_generate_current_schematics"
category: "tutp8"
---

# Generating the finished schematic

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Generating the finished schematic  
    1. In the Feeder of the project, set the Option_Inspect_available parameter to the value true.
    2. Generate the ECAD structure once again.
    3. The schematic consists again of 2 pages that contain 8 and/or 2 sensors.
    4. Open the schematic.
    5. The detailed view of the schematic shows that both the device tag as well as the function texts are entered correctly.
The final test is now to show that the second page is not created if the Option_Inspect_available parameter is set to false.
    1. In the Feeder of the project, set the Option_Inspect_available parameter to the value false.
    2. Generate the ECAD structure again.
    3. Open the schematic again.
    4. The sensors are now arranged in the schematic without gaps, and the empty second page has been removed.
    5. Thus, the goal of the Eplan Electric P8 discipline task has been accomplished.
