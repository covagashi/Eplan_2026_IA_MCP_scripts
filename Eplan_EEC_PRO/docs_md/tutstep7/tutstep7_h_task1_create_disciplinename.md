---
title: "Creating the DisciplineName parameter and assigning FB_Sequence"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task1_create_disciplinename.htm"
file: "tutstep7_h_task1_create_disciplinename"
category: "tutstep7"
---

# Creating the DisciplineName parameter and assigning FB_Sequence

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating the DisciplineName parameter and assigning FB_Sequence The DisciplineName parameter must be created and assigned to FB_Sequence.
    1. Select the Parameter unit.
    2. Select New > Parameter in the shortcut menu.
    3. Enter DisciplineName in the Name field.
    4. In the Type field, enter the data type String.
    5. Open the FB_Sequence function block.
    6. Select the Parameters editor.
    7. Add the parameter DisciplineName.
    8. Enter the following formula in the Value column:
    
        =name+'DB'
