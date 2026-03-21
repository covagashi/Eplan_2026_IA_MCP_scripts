---
title: "Creating resource files"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task4_create_resource_files.htm"
file: "tutstep7_h_task4_create_resource_files"
category: "tutstep7"
---

# Creating resource files

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating resource files Three resource files are needed that can be created with any editor.
    1. Create the file FB_Errors.AWL in the folder ..\installation folder\resources\Step7\.
    2. Write the following content into the file:
    
        FUNCTION_BLOCK "FB_Errors"
    TITLE =
    VERSION : 0.1
    VAR
    (*{LOOP:dos('FR_Errors_Dec')}*)(*{Call}*)(*{END_LOOP}*)
    END_VAR
    BEGIN
    (*{LOOP:dos('FR_Errors_NW')}*)(*{Call}*)(*{END_LOOP}*)
    END_FUNCTION_BLOCK

    1. Save and close the file.
    2. Create the file FB_Errors_Dec.AWL in the folder ..\installation folder\resources\Step7\.
    3. Write the following content into the file:
    
        FRAGMENT "FR_Errors_Dec"
    VAR
    END_VAR
    BEGIN
    Error_M8B_ErrorNumber_M8E : BOOL;
    TON_Error_M8B_ErrorNumber_M8E : "TON";
    END_FRAGMENT

    1. Save and close the file.
    2. Create the file FB_Errors_NW.AWL in the folder ..\installation folder\resources\Step7\.
    3. Write the following content into the file:
    
        FRAGMENT "FR_Errors_NW"
    VAR
    END_VAR
    BEGIN
    NETWORK
    TITLE -Error M8B_ErrorNumber_M8E Part 1/2
    (*{IF $Output_2}*)
    (*{1 Output, 2 Input}*)
    U( ,
    U M8B_Output_1_M8E;
    UN M8B_Input_1_M8E;
    O ,
    UN M8B_Output_1_M8E;
    UN M8B_Input_2_M8E;
    O ,
    U M8B_Input_1_M8E;
    U M8B_Input_2_M8E;
    O ,
    UN M8B_Input_1_M8E;
    UN M8B_Input_2_M8E;
    ) ,
    (*{ELSE}*)
    (*{IF mc.$Sensor.size -1}*)
    (*{2 Output, 1 Input}*)
    U( ,
    U M8B_Output_1_M8E;
    UN M8B_Input_1_M8E;
    O ,
    U M8B_Output_2_M8E;
    U M8B_Input_1_M8E;
    ) ,
    (*{ELSE}*)
    (*{2 Output, 2 Input}*)
    U( ,
    U M8B_Output_1_M8E;
    UN M8B_Input_1_M8E;
    O ,
    U M8B_Output_2_M8E;
    UN M8B_Input_2_M8E;
    O ,
    U M8B_Input_1_M8E;
    U M8B_Input_2_M8E;
    O ,
    UN M8B_Input_1_M8E;
    UN M8B_Input_2_M8E;
    ) ,
    (*{END_IF}*)
    (*{END_IF}*)
    - L 0.0,
    BLD 103,
    CALL #TON_Error_M8B_ErrorNumber_M8E (
    IN :- L 0.0,
    PT :- T#500MS),
    NOP 0,
    NETWORK
    TITLE -Error M8B_ErrorNumber_M8E Part 2/2
    U #TON_Error_M8B_ErrorNumber_M8E.0,
    - #Error_M8B_ErrorNumber_M8E,
    END_FRAGMENT

    1. Save and close the file.
