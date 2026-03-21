---
title: "Test 7 - Generating input and output addresses, structure and STEP 7 code"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task4_test7_generate.htm"
file: "tutstep7_h_task4_test7_generate"
category: "tutstep7"
---

# Test 7 - Generating input and output addresses, structure and STEP 7 code

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Test 7 - Generating input and output addresses, structure and STEP 7 code This test is intended to check whether the structure and the STEP 7 code with the fragments of the interrupt messages can be generated with reference to the parameter values and formulas that were entered in the previous sections.
    1. Select the root object Mechatronic in the project.
    2. Select IO_Generator > GenerateFieldbusCommand from the popup menu.
    3. Select STEP 7 > Generate Structure from the popup menu.
Then check whether the addresses for the inputs and outputs have been correctly assigned (see [Test 5 - Creating input and output addresses](tutstep7_h_task2_test5_generate.htm)). The result of the discipline structure should look as follows: All fragments FR_Errors_Dec and FR_Errors_NW are arranged under the function block FB_Errors.
