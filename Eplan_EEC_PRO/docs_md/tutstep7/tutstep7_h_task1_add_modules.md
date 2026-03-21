---
title: "Adding the program blocks and preassembled symbol table"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task1_add_modules.htm"
file: "tutstep7_h_task1_add_modules"
category: "tutstep7"
---

# Adding the program blocks and preassembled symbol table

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Adding the program blocks and preassembled symbol table You need to create components for the symbol table and program blocks. The files supplied are to be used for this purpose. Create the OB_Cycle program block.
    1. Select the Step7 unit.
    2. From the popup menu, select New > STEP 7 > Source > Program.
    3. In the Resource location panel, click Import.
The Open dialog now appears.
    1. Select the file OB_Cycle.AWL.
    2. Confirm with [Open].
The OB_Cycle name is automatically imported. The STEP 7-STL (STEP 7-LD) language of the block is also automatically detected.
    1. Select the Parameters editor.
The Number parameter has already been entered.
    1. Enter the number 1 in the Value column.
    2. Repeat steps 1 and 7 for the following symbol table and blocks. Use the specified values for the Number parameter:
New > STEP 7 > Source > Function: FC_Org_Functions.AWL, Number = 1 New > STEP 7 > Source > Function: FC_ASI_CopyInputs.AWL, Number = 2 New > STEP 7 > Source > Function block: FB_Sequence.AWL, Number = 1 New > STEP 7 > Source > Function block: FB_Insert.AWL, Number = 20 New > STEP 7 > Source > Function block: FB_Move.AWL, Number = 21 New > STEP 7 > Source > Function block: FB_Inspect.AWL, Number = 22 New > STEP 7 > Source > Symbol Table: Symboltable.SDF The results should look as follows: The parameters of the imported blocks are listed in the Parameter unit that is automatically created.
