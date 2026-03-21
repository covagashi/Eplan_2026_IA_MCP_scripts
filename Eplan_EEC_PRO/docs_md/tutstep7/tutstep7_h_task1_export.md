---
title: "Exporting SIMATIC STEP 7 program blocks"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task1_export.htm"
file: "tutstep7_h_task1_export"
category: "tutstep7"
---

# Exporting SIMATIC STEP 7 program blocks

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Exporting SIMATIC STEP 7 program blocks The following blocks are required for the program: Name | Block | Function  
---|---|---  
OB_Cycle | OB_Cycle.AWL | Organization of function blocks  
FC_Org_Functions | FC1.AWL |   
FC_ASI_CopyInputs | FC2.AWL |   
FB_Sequence | FB_Sequence.AWL |   
FB_Insert | FB_Insert.AWL | Controls the separator and checks the contents of the magazine  
FB_Move | FB_Move.AWL | Controls the X/Y-axes and the gripper  
FB_Inspect | FB_Inspect.AWL | Controls the workpiece position check  
Symbol table | Symboltable.sdf |   
FB_Errors | FB_Errors.AWL | Function block for error messages  
FR_Errors_Dec | FR_Errors_Dec.AWL | Fragment for error messages  
FR_Errors_NW | FR_Errors_NW.AEL | Fragment for error messages  
FR_SymbolsGeneral | FR_SymbolsGeneral.SDF | Fragment for symbol table  
FR_SymbolTable | FR_SymbolTable.SDF | Fragment for symbol table  
These blocks can be found in the zip file Tutorial_Step7.ZIP in the folder EC_Installationfolder\install\Tutorial\Step7. The block files must be unzipped in the folder EC_Installationfolder\resources\Tutorial\Step7.
