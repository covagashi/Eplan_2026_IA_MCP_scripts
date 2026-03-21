---
title: "Inserting and configuring the Symbol parameter in actuators and sensors"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task3_insert_parameter_symbol.htm"
file: "tutstep7_h_task3_insert_parameter_symbol"
category: "tutstep7"
---

# Inserting and configuring the Symbol parameter in actuators and sensors

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Inserting and configuring the Symbol parameter in actuators and sensors The parameter Symbol, whose value is determined by formula from the installed components of the previous step, must still be inserted into the components Valve, Cylinder, and Position sensor and provided with formulas. Installing the Symbol parameter in actuators and sensors:  
    1. Open the component Valve in the Actuators unit.
    2. Open the Parameter editor.
    3. Drag the parameter Symbol from the Parameter unit into the editor.
    4. Enter the following formula for the parameters:
    
        =mc.$Symbol+'_'+name

    1. Repeat steps 1 to 4 for the components Cylinder, Positionsensor and Pressuresensor with the parameter Symbol and the following formula:
    
        =mc.$Symbol
