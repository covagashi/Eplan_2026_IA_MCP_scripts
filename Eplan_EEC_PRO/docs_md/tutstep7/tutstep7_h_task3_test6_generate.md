---
title: "Test 6 - Generating the symbol table and input and output addresses"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task3_test6_generate.htm"
file: "tutstep7_h_task3_test6_generate"
category: "tutstep7"
---

# Test 6 - Generating the symbol table and input and output addresses

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Test 6 - Generating the symbol table and input and output addresses This test is intended to check whether all of the addresses can be allocated for the inputs and outputs and whether the symbol table can be created with reference to the parameter values and formulas that were entered in the previous sections. Creating:  
    1. Select the root object Mechatronic in the Feeder project.
    2. Select IO-Generator > GenerateFieldbusCommand from the popup menu.
    3. Select STEP 7 > Generate Structure from the popup menu.
Then check whether the addresses for the inputs and outputs have been correctly assigned (see [Test 5 - Creating input and output addresses](tutstep7_h_task2_test5_generate.htm)). The result of the discipline structure should look as follows: Then check the created symbol table:
    1. Open the SymbolTable symbol table in the project.
    2. Open the File editor.
