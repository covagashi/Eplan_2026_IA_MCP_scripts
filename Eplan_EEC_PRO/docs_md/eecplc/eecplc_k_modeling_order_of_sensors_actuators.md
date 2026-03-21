---
title: "Order of actuators and sensors"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_modeling_order_of_sensors_actuators.htm"
file: "eecplc_k_modeling_order_of_sensors_actuators"
category: "eecplc"
---

# Order of actuators and sensors

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Order of actuators and sensors

In some cases, it is desirable to base the sequence in which addresses are assigned by the IO generator on certain properties of controller components (e.g. first all 8-bit cards, then all 16-bit cards, etc.). This is accomplished via the parameter for the sequence. All controller components that dispose of this parameter are sorted alphabetically based on the parameter value. Controller components that do not have this parameter are processed based on their order within the mechatronic structure after controller components that have the sequence parameter.

The designation of the sequence parameter can be changed via the model variable (Model > Model variables menu) Disciplines > Fieldbus > Name of the parameter for the sequence.
