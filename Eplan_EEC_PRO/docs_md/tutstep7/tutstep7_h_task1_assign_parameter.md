---
title: "Assigning the âCallerâ parameter to the function blocks"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task1_assign_parameter.htm"
file: "tutstep7_h_task1_assign_parameter"
category: "tutstep7"
---

# Assigning the âCallerâ parameter to the function blocks

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Assigning the âCallerâ parameter to the function blocks The Caller parameter must be assigned to all function blocks that call or are called.
    1. Open the FB_Sequence function block.
    2. Select the Parameters editor.
    3. Drag the Caller parameter from the Parameter unit into the editor.
    1. Enter the text OB_Cycle for the Caller parameter in the Value column:
    2. Repeat steps 1 and 7 for the FB_Insert, FB_Move and FB_Inspect function blocks. Enter the FB_Sequence text in the Value column.
