---
title: "Sequence of controller components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_modeling_sensors_actuators_order.htm"
file: "eecplc_k_modeling_sensors_actuators_order"
category: "eecplc"
---

# Sequence of controller components

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Sequence of controller components

In some cases, it is desirable to base the sequence in which addresses are assigned by the IO generator on certain sensor or actuator properties (e.g. first all cam switches, then all pressure switches, etc.). This is accomplished via the parameter for the sequence. All sensors and actuators that have this parameter are sorted alphabetically based on the parameter value. Sensors and actuators that do not have this parameter are processed based on their order within the mechatronic structure after sensors and actuators with the sequence parameter.

The designation of the sequence parameter can be changed via the (Model > Model variables menu) Disciplines > Fieldbus > Name of the parameter for the sequence.
