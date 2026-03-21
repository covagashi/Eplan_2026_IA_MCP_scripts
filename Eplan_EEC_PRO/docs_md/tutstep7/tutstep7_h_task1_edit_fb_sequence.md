---
title: "Modifying FB_Sequence.AWL (FB1)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task1_edit_fb_sequence.htm"
file: "tutstep7_h_task1_edit_fb_sequence"
category: "tutstep7"
---

# Modifying FB_Sequence.AWL (FB1)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Modifying FB_Sequence.AWL (FB1) The function block FB_Sequence.AWL must be changed according to the following program code:
    
        FUNCTION_BLOCK "FB_Sequence"
    TITLE =
    VERSION : 0.1
    
    
    VAR_OUTPUT
    DefaultPosition : BOOL ;
    END_VAR
    
    VAR
    (*{LocalVariables}*)
    SM0 : BOOL ;
    SM1 : BOOL ;
    SM2 : BOOL ;
    SM3 : BOOL ;
    SM4 : BOOL ;
    END_VAR
    
    BEGIN
    
    NETWORK
    TITLE =
    
    UN "E_BA_Automatic";
    SPB DONE;
    
    NETWORK
    TITLE =
    
    U #SM1;
    SPB SM1;
    
    NETWORK
    TITLE =
    
    U #SM2;
    SPB SM2;
    
    NETWORK
    TITLE =
    
    U #SM3;
    SPB SM3;
    
    NETWORK
    TITLE =
    
    U #SM4;
    SPB SM4;
    
    NETWORK
    TITLE =
    //Schritt 0: Wait for restart
    //
    U "Default_Position_Auto";
    U "E_Start";
    S #SM1;
    R #SM0;
    
    NETWORK
    TITLE =
    
    SPA DONE;
    
    NETWORK
    TITLE =.
    //Step 1: FB_Insert
    //
    SM1: U #SM1;
    U #FB_Insert.Ready;
    S #SM2;
    R #SM1;
    
    NETWORK
    TITLE =
    
    SPA DONE;
    
    NETWORK
    TITLE =
    // Step 2: FB_Move
    SM2: U #SM2;
    U #FB_Move.Ready;
    S #SM3;
    R #SM2;
    
    NETWORK
    TITLE =
    
    SPA DONE;
    
    NETWORK
    TITLE =
    //Step 3: FB_Inspect
    //
    SM3: U #SM3;
    (*{IF mroot.$Option_Inspect_available}*)
    U #FB_Inspect.Ready;
    (*{END_IF}*)
    S #SM4;
    R #SM3;
    
    NETWORK
    TITLE =
    
    SPA DONE;
    
    NETWORK
    TITLE =
    //Step 4: FB_Move
    SM4: U #SM4;
    U #FB_Move.Ready;
    S #SM0;
    R #SM4;
    
    NETWORK
    TITLE =
    
    SPA DONE;
    
    NETWORK
    TITLE =
    
    DONE: U #SM1;
    U "E_BA_Automatic";
    S "Part_is_OK";
    
    NETWORK
    TITLE =
    
    U #SM1;
    U "E_BA_Automatic";
    = #FB_Insert.Start;
    
    NETWORK
    TITLE =
    
    U #SM2;
    U "E_BA_Automatic";
    = #FB_Move.Pos1Pos2;
    
    NETWORK
    TITLE =
    
    (*{IF mroot.$Option_Inspect_available}*)
    U #SM3;
    U "E_BA_Automatic";
    = #FB_Inspect.Start;
    (*{END_IF}*)
    
    NETWORK
    TITLE =
    
    U #SM4;
    U "Part_is_OK";
    U "E_BA_Automatic";
    = #FB_Move.Pos2Pos4;
    
    NETWORK
    TITLE =
    
    U #SM4;
    UN "Teil_ist_OK";
    U "E_BA_Automatic";
    = #FB_Move.Pos2Pos3;
    
    NETWORK
    TITLE =
    
    U( ;
    #SM2;
    #SM4;
    ) ;
    U "E_BA_Automatic";
    = #FB_Move.Start;
    
    (*{LOOP:dos}*)
    
    NETWORK
    TITLE =
    
    (*{Call}*)(*{END_LOOP}*)
    
    NETWORK
    TITLE =Default Position for BA Automatic
    
    U #FB_Insert.DefaultPosition_Auto;
    (*{IF mroot.$Option_Inspect_available}*)
    U #FB_Inspect.DefaultPosition_Auto;
    (*{END_IF}*)
    U #FB_Move.DefaultPosition_Auto;
    = "DefaultPosition_Auto";
    
    NETWORK
    TITLE =Other Default Position in BA DefaultPositionMove
    
    U #FB_Insert.DefaultPosition_GF;
    (*{IF mroot.$Option_Inspect_available}*)
    U #FB_Inspect.DefaultPosition_GF;
    (*{END_IF}*)
    U #FB_Move.DefaultPosition_GF;
    = "DefaultPosition_GF";
    END_FUNCTION_BLOCK
