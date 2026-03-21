---
title: "Entering formulas for the structure parameters of the installed actuators and sensors"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task2_insert_formulas2.htm"
file: "tutstep7_h_task2_insert_formulas2"
category: "tutstep7"
---

# Entering formulas for the structure parameters of the installed actuators and sensors

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Entering formulas for the structure parameters of the installed actuators and sensors The installed actuators and sensors obtain the values for the structure parameters IO_Place, IO_Places, and IO_IncomingBus from their parent mechatronic component, here the Function unit.
    1. Open the Axis Functionunit.
    2. Select the installed Cylinder component.
The editor for the parameters of the installed Cylinder component will be displayed.
    1. Select the parameters IO_Place, IO_Places and IO_IncomingBus.
    2. Select the Add Interface Parameter item from the popup menu.
The parameter values are then filled with the formulas =mc.$IO_IncomingBus, =mc.$IO_Place, and =mc.$IO_Places.
    1. Repeat Steps 1 to 4 for the installed sensors of this Function unit and for all other sensors and actuators installed in Function units.
