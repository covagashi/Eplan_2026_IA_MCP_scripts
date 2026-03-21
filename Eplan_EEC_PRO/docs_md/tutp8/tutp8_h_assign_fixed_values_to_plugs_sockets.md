---
title: "Assign fixed values for plugs and sockets to Eplan Electric P8 components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_assign_fixed_values_to_plugs_sockets.htm"
file: "tutp8_h_assign_fixed_values_to_plugs_sockets"
category: "tutp8"
---

# Assign fixed values for plugs and sockets to Eplan Electric P8 components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Assign fixed values for plugs and sockets to Eplan Electric P8 components For the structure of the ECAD discipline to be created without errors, values have to be assigned to the parameters for Plug and Socket. In the following steps the parameters of the plugs for all sensors occurring in the mechatronics structure are numbered beginning at I0.0 (notation for STEP 7).  
    1. In the Project Catalog, open the Mechatronics tree.
Tip If the tree structure does not indicate the sensors as in the below illustration, please check the settings for the filter. Uncheck the box for the ECAD option, if necessary.
    1. Open Sensor_optical.
    2. Open the Parameter editor.
    3. For the IP parameter, enter the value I0.0.
    4. Repeat Steps 2 to 4 for all further sensors and enter I0.1 to I0.7, I1.0 and I1.1 in the process.
    5. Then enter the values I0.0 to I0.7 and I1.0 to I1.7 for the socket parameters of the pages.
    6. Open the PLC_Sensors_1_8 page.
    7. Click Parameters in the editor.
    1. For the parameters Input1 to Input8, enter the values I0.0 to I0.7.
    2. Repeat steps 1 to 3 for the PLC_Sensors_9_16 page, and enter the values I1.0 to I1.7.
