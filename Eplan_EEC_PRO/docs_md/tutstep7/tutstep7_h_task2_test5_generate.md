---
title: "Test 5 - Creating input and output addresses"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task2_test5_generate.htm"
file: "tutstep7_h_task2_test5_generate"
category: "tutstep7"
---

# Test 5 - Creating input and output addresses

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Test 5 - Creating input and output addresses This test is intended to check whether all of the addresses can be allocated for the inputs and outputs with reference to the parameter values and formulas that were entered in the previous sections. Importing the T_IOGenerator_UI library adds commands for creating (GenerateFieldbusCommand), resetting (ResetFieldbusCommand), and updating (UpdateFieldbusCommand) to the mechatronic module. The commands are called up by means of the popup menu for the mechatronic root object of the project, here Mechatronic.
    1. Select the project component Mechatronic.
    2. Select the item IO_Generator > GenerateFieldbusCommand from the popup menu.
The correct allocation of the addresses can be checked by opening all of the project components of type Actuator and Sensor. The following figure shows the address allocated to the project component Feeder.Mechatronic.Feeder.Insert.Separator.Cylinder.Valve_1: The project component Feeder.Mechatronic.Feeder.Insert.Separator.Cylinder.Valve_1 is after the Cylinder the second actuator in the project structure and is thus given the address O0.1.
