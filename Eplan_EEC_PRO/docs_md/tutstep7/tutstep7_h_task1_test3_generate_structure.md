---
title: "Test 3 - Creating the structure using the inserted discipline components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task1_test3_generate_structure.htm"
file: "tutstep7_h_task1_test3_generate_structure"
category: "tutstep7"
---

# Test 3 - Creating the structure using the inserted discipline components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Test 3 - Creating the structure using the inserted discipline components The complete structure should now be created.
    1. Select Mechatronic in the Project Catalog in the Feeder project.
    2. Select STEP 7 > Generate structure in the popup menu.
The function blocks that were previously inserted can also now be found in the structure. The next test is designed to show that the FB_Inspect function block is not displayed in the structure if the Inspect function group is disabled via disabler. For this purpose, the Option_Inspect_available parameter is set to false in the project explorer for the Feeder.
    1. Open the project component Feeder in the Project Catalog.
    2. Set the Option_Inspect_available parameter to false.
    3. Generate the STEP 7 structure again.
The FB_Inspect function block can be inserted and removed using the Option_Inspect_available parameter. The change does not take effect until the structure has been created again.
