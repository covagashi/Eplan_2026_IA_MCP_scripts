---
title: "Inserting and configuring Actuator and Sensor parameters into the Axis and Separator Function units"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task4_insert_parameter1.htm"
file: "tutstep7_h_task4_insert_parameter1"
category: "tutstep7"
---

# Inserting and configuring Actuator and Sensor parameters into the Axis and Separator Function units

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Inserting and configuring Actuator and Sensor parameters into the Axis and Separator Function units The Actuator and Sensor parameters are now installed in the Axis and Separator Function units, in order to determine lists of symbols of all sensors and actuators therein. Installing the Actuator and Sensor parameters in Axis providing them with parameter values:  
    1. Open the Axis Functionunit.
    2. Open the Parameter editor.
    3. Drag the parameters Actuator and Sensor from the Step7.Parameter unit into the editor.
    4. Enter the following formulas for the parameters:
Parameter | Value  
---|---  
Actuator | =rmos('Valve').$Symbol  
Sensor | =rmos('Sensor').$Symbol  
    1. Repeat steps 1 to 4 for the Separator Function unit.
