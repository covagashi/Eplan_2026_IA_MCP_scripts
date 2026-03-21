---
title: "Adding plugs and sockets to Text discipline components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tuttext_h_generate_nonfunctional_structure_extend_text_components_with_plugs_sockets.htm"
file: "tuttext_h_generate_nonfunctional_structure_extend_text_components_with_plugs_sockets"
category: "tuttext"
---

# Adding plugs and sockets to Text discipline components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Adding plugs and sockets to Text discipline components Using the corresponding sockets for chapters and plugs for lines, it is now possible to assign the lines to the correct chapters:
    1. Open the text component Chapter in the ListOfComponents unit.
    2. Switch to the Parameter editor page.
    3. Click the Add parameter symbol and select the Socket parameter in the Finder. Alternatively, you can also use Drag & Drop to add the Socket parameter.
    4. Repeat Steps 1 to 3 with the text component Line and the parameter Plug.
    1. Double-click to open the component Feeder in the T_Mechatronic_ModularSystem library in the Stations unit.
    2. Click to mark the ActuatorsChapter component. The corresponding parameter table now opens.
    3. Enter Actuators as the value for the Socket parameter.
    4. Repeat the previous two steps to add the Sensors value to the SensorsChapter.
    1. Repeat steps 5 to 7 with Valve and Cylinder for the installed component Line with the plug parameter value Actuators.
    1. Repeat steps 5 to 7 with Pressuresensor, Positionsensor_optical and Positionsensor_inductive for the installed component Line with the plug parameter value Sensors.
