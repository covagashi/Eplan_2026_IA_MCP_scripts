---
title: "Generating the STEP 7 Program"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task1_test4_generate_code.htm"
file: "tutstep7_h_task1_test4_generate_code"
category: "tutstep7"
---

# Generating the STEP 7 Program

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Generating the STEP 7 Program This test is designed to show how to generate the STEP 7 program on the basis of the generated structure. Before you start, reset the Option_Inspect_available parameter to true.
    1. Generate the STEP 7 structure again.
    2. Select the Step7 root component.
    3. Select STEP 7 > Generate code in the popup menu.
The created files are stored in the following folder:
    
        EC-Installationsordner\workspace\Feeder\Step7\SiemensCPU

    1. Use the navigator view to view the folder contents:
    2. Open the navigator view.
The symbol table and AWL files of all blocks have been created. The test with the Option_Inspect_available parameter set to false creates the following results: The file FB_Inspect.AWL is no longer available. Double-click on an AWL file to open this in an internal EC editor. In the figure, you can see the created calls that have been inserted for the FB_Insert and FB_Move function blocks.
