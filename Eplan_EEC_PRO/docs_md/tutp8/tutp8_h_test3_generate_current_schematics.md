---
title: "Generating the current status of the schematic"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_test3_generate_current_schematics.htm"
file: "tutp8_h_test3_generate_current_schematics"
category: "tutp8"
---

# Generating the current status of the schematic

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Generating the current status of the schematic
    1. Generate the ECAD structure again.
    2. The structure now includes one page with 8 sensors, and one page with 2 sensors.
Now, the schematic can be viewed using Eplan Electric P8.
    1. Select WiringDiagram_Feeder_Feeder in the project explorer.
    2. Select Open schematic in the shortcut menu.
    3. The schematic is now created, and then Eplan Electric P8 is launched.
    4. The schematic consists of 2 pages where all sensors are available.
    5. Disable the Inspect function group by setting the Option_Inspect_available to false in the Feeder component.
    6. Generate the ECAD structure again.
    7. The first page contains only 5 sensors now.
    8. Generate and open the schematic again.
    9. The removal of sensors has created gaps on the first page.
This is caused by the fixed values for the plug parameters. To prevent such gaps, the values of the plug parameters have to be calculated by means of a formula.
