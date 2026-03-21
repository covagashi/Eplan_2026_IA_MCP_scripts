---
title: "Assign parameter to components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutmechatronic_h_assign_parameter_to_component.htm"
file: "tutmechatronic_h_assign_parameter_to_component"
category: "tutmechatronic"
---

# Assign parameter to components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Assign parameter to components The new parameters must now be added to the components Feeder, Axis and Cylinder:
    1. Open the Feeder component (double-click Feeder in the library T_Mechatronic_ModularSystem)
    2. Switch to the Parameter editor page.
    3. Insert the Option_Inspect_available parameter.
A parameter is added by clicking on  or via Drag & Drop.
    1. Repeat the steps 1 to 3 for the Axis function unit, and insert the parameters Sensor_2_available, Sensor_3_available, and Sensor_4_available.
A default axis is to have four sensors. The default, that is the value, that is used when there are no other configurations must, therefore, be true:
    1. In the Value column, select for the parameter Sensor_2_available, Sensor_3_available, and Sensor_4_available true from the drop-down list.
    2. Mark the Cylinder actuator and insert the parameter Option_Two_Valves.
    3. In the Value column, select for the parameter Option_Two_Valve false from the drop-down list.
