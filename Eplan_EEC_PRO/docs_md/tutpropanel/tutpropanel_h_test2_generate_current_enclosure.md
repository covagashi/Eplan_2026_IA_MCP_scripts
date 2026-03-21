---
title: "Generating the finished state of the enclosure"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutpropanel_h_test2_generate_current_enclosure.htm"
file: "tutpropanel_h_test2_generate_current_enclosure"
category: "tutpropanel"
---

# Generating the finished state of the enclosure

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Generating the finished state of the enclosure Generate the enclosure.
    1. Open the Feeder.Mechatronic.Feeder project component in the Project Explorer.
    2. Open the Parameter editor.
    3. Set the Option_Inspect_available value to true.
    4. Save the project component.
    5. Select Feeder.Mechatronic in the Project Explorer.
    6. In the popup menu, select ECAD > Generate Eplan ProPanel Structure.
The following structure should exist in the Project Explorer:
    1. On the TS35_7_5_Top_Feeder mounting rail the ECAD structure contains a power supply, a PLC and 7 digital input modules. On the TS35_7_5_Bottom mounting rail it contains 4 terminal end blocks, 3 terminal clamps for the power supply and 30 terminal clamps for the sensors.
    2. In the Project Explorer mark the Feeder.ECAD.Schematic_Feeder component.
    3. In the popup menu, select Generate and Open Eplan ProPanel.
The Eplan Electric P8 application opens.
    1. Double-click the LayoutSpace_Feeder element to open it in the layout space.
    2. The created enclosure is displayed in the editor area.
    3. All of the discipline components are available and properly arranged.
    4. Close Eplan Electric P8.
Disable the Inspect function group by setting the Option_Inspect_available to false in the Feeder component. Generate the ECAD structure again. The following structure should exist in the Project Explorer:
    1. On the TS35_7_5_Top_Feeder mounting rail the ECAD structure contains a power supply, a PLC and 5 instead of 7 digital input modules and on the TS35_7_5_Bottom mounting rail 4 terminal end blocks, 3 terminal clamps for the power supply and 20 terminal clamps for the sensors.
The Eplan Electric P8 application opens.
    1. You have reached the goal of the tutorial.
