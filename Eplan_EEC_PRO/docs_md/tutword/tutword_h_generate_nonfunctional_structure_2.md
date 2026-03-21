---
title: "Adding plugs and sockets to Word components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutword_h_generate_nonfunctional_structure_2.htm"
file: "tutword_h_generate_nonfunctional_structure_2"
category: "tutword"
---

# Adding plugs and sockets to Word components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Adding plugs and sockets to Word components The discipline component Row is installed (pre-instantiated) in the mechatronic components for sensors and actuators. So that the fragment documents are inserted correctly in the sections ActuatorsTable and SensorsTable when generating the ListOfComponents, these sections have to be extended with a parameter of the type Socket with the values Actuators and Sensors. The discipline components Row are to be expanded with a parameter of the type Plug. Depending on whether these discipline components are installed in an actuator or a sensor, the values Actuators or Sensors are to be entered for the parameters. Extend the discipline components ActuatorsTable and SensorsTable with the parameter Socket:
    1. Open the component Chapter.
    2. Open the Parameters editor page.
    3. Drag & Drop the Socket parameter into the parameter editor.
    4. Save the component.
    5. Open the Feeder component.
    6. Select the installed ActuatorsTable discipline component.
    7. Enter Actuators as the value for the Socket parameter.
    8. Repeat steps 5 to 7 for the SensorsTable and for the value Sensors.
Expand the discipline components Cylinder and Valve with the parameter Plug:
    1. Open in the component Row.
    2. Open the Parameters editor page.
    3. Drag & Drop the Plug parameter into the parameter editor.
    4. Save the component.
    5. Open in the component Cylinder.
    6. Select the installed Row discipline component.
    7. Enter Actuators as the value for the Plug parameter.
    8. Save the component.
    9. Repeat the steps 5 to 8 for the Valve component.
Extend the discipline components Positionsensor_inductive, Positionsensor_optical and Pressuresensor with the parameter Plug:
    1. Open in the Positionsensor_inductive component.
    2. Select the installed Row discipline component.
    3. Enter Actuators as the value for the Plug parameter.
    4. Save the component.
    5. Repeat Steps 1 to 4 for the Positionsensor_optical and Pressuresensor components.
