---
title: "Creating a STEP 7 program for Feeder"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task1_generate_code.htm"
file: "tutstep7_h_task1_generate_code"
category: "tutstep7"
---

# Creating a STEP 7 program for Feeder

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating a STEP 7 program for Feeder The task is to create a STEP 7 program based on the functional, mechatronic configuration Feeder. **** As shown in the following figure, the plug-socket principle will be used to insert the FB_Insert, FB_Move, and FB_Inspect function blocks into the FB_Sequence function block. The parameter for the STEP 7 discipline always has the name Caller assigned to it. The parameter value is the same as the name of the block where the socket is located, i.e., FB_Sequence for purposes of this tutorial. Because the optional Inspect function group is installed in the mechatronic, it should be possible to create two different programs.
     * With FB_Inspect
     * Without FB_Inspect
Information: A symbol file is prepared for the first task. The structure of the components is stored internally in the STEP 7 discipline. The following levels exist:
