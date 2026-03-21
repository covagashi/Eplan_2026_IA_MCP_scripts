---
title: "Division between on and off during an emergency stop"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_division_between_on_and_off_during_an_emergency_stop.htm"
file: "concept_k_division_between_on_and_off_during_an_emergency_stop"
category: "concept"
---

# Division between on and off during an emergency stop

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Division between on and off during an emergency stop

In order to make it possible for certain actuators to have their power cut off during an emergency-stop event, while other actuators, e.g. the gripper, continue to receive power, two bus types, on_for_emergency_stop and off_for_emergency_stop, are introduced. Depending on which outgoing bus is registered at a terminal, the connection will either continue to receive power in an emergency-off situation or not.

In this example, the different bus wirings are denoted with different colors.

The names of the bus types are written on the connections.
