---
title: "Entering symbol names into the parameters of installed Function units"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task3_insert_symbolnames.htm"
file: "tutstep7_h_task3_insert_symbolnames"
category: "tutstep7"
---

# Entering symbol names into the parameters of installed Function units

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Entering symbol names into the parameters of installed Function units The Function units installed in Function groups contain parameters for allocating symbols that must be entered in the following step.
    1. Open the Insert Function group.
    2. Select the installed Separator component.
    3. Enter the following values for the parameters:
Parameter | Value  
---|---  
Symbol_Cylinder | O_Separator  
Symbol_Position_1 | I_Separator_Pos_1  
Symbol_Position_2 | I_Separator_Pos_2  
    1. Repeat steps 2 and 3 for the installed Stack component.
Parameter | Value  
---|---  
Symbol_Position_1 | I_Stack_Part_In_Pos  
    1. Repeat steps 1 to 3 for the following installed Function groups:
Functiongroup | Installed Function unit | Parameter | Value  
---|---|---|---  
Inspect | Orientationinspector | Symbol_Position_1 | I_Inspect_Orientation  
Move | X_Axis | Symbol_Cylinder | O_XAxis  
Symbol_Position_1 | I_XAxis_Position_1  
Symbol_Position_2 | I_XAxis_Position_2  
Symbol_Position_3 | I_XAxis_Position_3  
Symbol_Position_4 | I_XAxis_Position_4  
Y_Axis | Symbol_Cylinder | O_YAxis  
Symbol_Position_1 | I_YAxis_Position_1  
Symbol_Position_2 | I_YAxis_Position_2  
Symbol_Position_3 | I_YAxis_Position_3  
Symbol_Position_4 | I_YAxis_Position_4  
Gripper | Symbol_Valve | O_Gripper  
Symbol_Pressuresensor | I_Gripper_Pressure
