---
title: "Modifying OB_Cycle.AWL"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task1_edit_ob_cycle.htm"
file: "tutstep7_h_task1_edit_ob_cycle"
category: "tutstep7"
---

# Modifying OB_Cycle.AWL

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Modifying OB_Cycle.AWL The program code must be changed according to Line 30:
    
        ORGANIZATION_BLOCK "OB_Cycle"
    TITLE = "Main Program Sweep (Cycle)"
    VERSION : 0.1
    
    
    VAR_TEMP
    OB1_EV_CLASS : BYTE ; //Bits 0-3 = 1 (Coming event), Bits 4-7 = 1 (Event class 1)
    OB1_SCAN_1 : BYTE ; //1 (Cold restart scan 1 of OB 1), 3 (Scan 2-n of OB 1)
    OB1_PRIORITY : BYTE ; //Priority of OB Execution
    OB1_OB_NUMBR : BYTE ; //1 (Organization block 1, OB1)
    OB1_RESERVED_1 : BYTE ; //Reserved for system
    OB1_RESERVED_2 : BYTE ; //Reserved for system
    OB1_PREV_CYCLE : INT ; //Cycle time of previous OB1 scan (milliseconds)
    OB1_MIN_CYCLE : INT ; //Minimum cycle time of OB1 (milliseconds)
    OB1_MAX_CYCLE : INT ; //Maximum cycle time of OB1 (milliseconds)
    OB1_DATE_TIME : DATE_AND_TIME ; //Date and time OB1 started
    END_VAR
    
    BEGIN
    
    NETWORK
    TITLE = Organisation
    
    CALL "FC_ASI_CopyInputs" ;
    CALL "FC_Org_Functions" ;
    
    NETWORK
    TITLE =Call Feeder
    
    (*{LOOP:dos}*)(*{Call}*)(*{END_LOOP}*)
    
    END_ORGANIZATION_BLOCK
