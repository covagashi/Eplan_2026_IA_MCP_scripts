---
title: "Insert sensor macros in mechatronic components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_insert_p8_components_into_mechatronic_components.htm"
file: "tutp8_h_insert_p8_components_into_mechatronic_components"
category: "tutp8"
---

# Insert sensor macros in mechatronic components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Insert sensor macros in mechatronic components Add as components via Drag & Drop the discipline components Sensor_Pressure, Sensor_Inductive and Sensor_Optical to all non-abstract sensors that are under T_Mechatronic_ModularSystem.Sensors:
     * Pressuresensor contains Sensor_Pressure
     * Positionsensor_inductive contains Sensor_Optical
     * Positionsensor_optical contains Sensor_Inductive
Then create the ECAD structure again. An error message will appear, because components cannot be assigned according to the plug-socket principle.
