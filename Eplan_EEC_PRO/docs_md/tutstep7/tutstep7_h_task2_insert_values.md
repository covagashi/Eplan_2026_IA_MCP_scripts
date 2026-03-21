---
title: "Entering values for structure parameters IO_Place, IO_Places, and IO_IncomingBus in Function groups"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task2_insert_values.htm"
file: "tutstep7_h_task2_insert_values"
category: "tutstep7"
---

# Entering values for structure parameters IO_Place, IO_Places, and IO_IncomingBus in Function groups

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Entering values for structure parameters IO_Place, IO_Places, and IO_IncomingBus in Function groups Previously, formulas were entered for the structure parameters for the installed actuators and sensors. By means of these formulas, these actuators and sensors obtain their values from the parent Function unit. The Function units obtain these values, in turn, from their corresponding parent Function group. First, the formulas are entered into all installed Function units:
    1. Open the Insert Function group.
    2. Select the installed Separator Function unit.
    3. Select the parameters IO_IncomingBus, IO_Place, and IO_Places.
    4. Select the Add Interface Parameter item from the popup menu.
    5. Repeat steps 1 to 4 for the installed Stack Function unit.
    6. Open the Parameter editor of the Insert Function group.
    7. For the IO_IncomingBus parameter, enter the value IO.
    8. For the IO_Place and IO_Places parameters, enter the value PLC.
    9. Repeat steps 1 to 8 for the Inspect Function group with the installed Orientationinspector Function unit and for the Move Function group with the installed X_Axis, Y_Axis, and Gripper Function units.
