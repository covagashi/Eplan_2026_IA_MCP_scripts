---
title: "Creating the Caller parameter"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task1_create_caller.htm"
file: "tutstep7_h_task1_create_caller"
category: "tutstep7"
---

# Creating the Caller parameter

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating the Caller parameter As shown in the section [Creating a STEP 7 program for Feeder](tutstep7_h_task1_generate_code.htm), the plug-socket principle will be used to insert the FB_Insert, FB_Move, and FB_Inspect function blocks in the FB_Sequence function block. The plug parameter for the STEP 7 discipline is always assigned the name Caller. As a value, the plug parameter contains the name of the block in which the call is to take place. In this example, this is FB_Sequence. TheCaller parameter is created in the Parameter unit. 1\. Select the Parameter unit.
    1. From the shortcut menu, select New > Parameter.
    2. Enter Caller in the Name field.
    3. In the Type field, enter the text Plug.
The new parameter is listed in the Parameter unit once it has been saved.
