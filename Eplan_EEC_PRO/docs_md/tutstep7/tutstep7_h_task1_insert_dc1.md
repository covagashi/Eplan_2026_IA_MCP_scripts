---
title: "Adding discipline components to mechatronic components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task1_insert_dc1.htm"
file: "tutstep7_h_task1_insert_dc1"
category: "tutstep7"
---

# Adding discipline components to mechatronic components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Adding discipline components to mechatronic components In the next step, you need to link the existing discipline-specific components to the functional components of the mechatronic model. This allows the STEP 7 structure to be automatically created from the mechatronic configuration. Use Drag & Drop to add the STEP 7 components SiemensCPU, OB_Cycle, FB_Sequence, and SymbolTable of the Feeder station as components.
    1. In T_Mechatronic_ModularSystem, open the Feeder station.
    1. Select the STEP 7 components SiemensCPU, OB_Cycle, FB_Sequence and SymbolTable.
    2. Drag & drop the STEP 7 components as a group in the Components field.
During instantiation, the inserted components are not arranged in a hierarchical level but according to the level configuration specified in the STEP 7 discipline library (see [Creating a STEP 7 program for Feeder](tutstep7_h_task1_generate_code.htm)).
