---
title: "Inserting formulas into the parameters of installed components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task3_insert_formulas.htm"
file: "tutstep7_h_task3_insert_formulas"
category: "tutstep7"
---

# Inserting formulas into the parameters of installed components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Inserting formulas into the parameters of installed components Formulas must also be inserted for the parameters of the installed components:
    1. Open the Axis Functionunit.
    2. Select the installed Cylinder component.
    3. Enter the following formula for the Symbol parameter:
    
        =mc.$Symbol_Cylinder

    1. Repeat steps 2 and 3 with the following data:
Installed component | Parameter | Value  
---|---|---  
Position_1 | Symbol | =mc.$Symbol_Position_1  
Position_2 | Symbol | =mc.$Symbol_Position_2  
Position_3 | Symbol | =mc.$Symbol_Position_3  
Position_4 | Symbol | =mc.$Symbol_Position_4  
    1. Repeat steps 1 and 3 for the following Function units:
Functionunit | Installed component | Parameter | Value  
---|---|---|---  
Gripper | Valve | Symbol | =mc.$Symbol_Valve  
Pressuresensor | Symbol | =mc.$Symbol_Pressuresensor  
Orientationinspector | Positionssensor_optical | Symbol | =mc.$Symbol_Position_1  
Separator | Cylinder | Symbol | =mc.$Symbol_Cylinder  
Position_1 | Symbol | =mc.$Symbol_Position_1  
Position_2 | Symbol | =mc.$Symbol_Position_2  
Stack | Positionssensor_optical | Symbol | =mc.$Symbol_Position_1
