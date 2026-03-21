---
title: "Inserting and configuring the parameter in the new function block and fragments"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task4_insert_parameter2.htm"
file: "tutstep7_h_task4_insert_parameter2"
category: "tutstep7"
---

# Inserting and configuring the parameter in the new function block and fragments

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Inserting and configuring the parameter in the new function block and fragments The fragments FR_Error_Dec and FR_Errors_NW, as well as the function block FB_Errors, also require the parameter Caller to be integrated in the discipline structure by means of the Plug-Socket principle. The function block FB_Errors also requires the parameter DiscipineName. These parameters are immediately provided with values. Inserting the parameters:
    1. Open the fragment FR_Errors_Dec.
    2. Open the Parameter editor.
    3. Drag the Caller parameter from the Parameter unit into the editor.
    4. For the Caller parameter, enter the value FB_Errors.
    5. Repeat steps 3 and 4 for the parameter ErrorNumber with the value =dc.dos('FR_Errors_Dec').indexOf(this)+1
    6. Repeat steps 1 to 5 for the fragment FR_Errors_NW with the following parameters:
Parameter | Value  
---|---  
Caller | FB_Errors  
ErrorNumber | =dc.dos('FR_Errors_NW').indexOf(this)+1  
Output_1 | =mc.$Actuator.first  
Output_2 | =if mc.relRef('Cylinder').$Option_Two_Valves then mc.$Actuator.at(1) else false endif  
Input_1 | =mc.$Sensor.first  
Input_2 | =if mc.$Sensor.size>1 then mc.$Sensor.at(1) else false endif  
    1. Repeat steps 1 to 5 for the function block FB_Errors with the following parameters:
Parameter | Value  
---|---  
Caller | FB_Errors  
DisciplineName | =name+'DB'  
Number | 2
