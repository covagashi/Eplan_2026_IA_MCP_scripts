---
title: "A single lamp and its terminals"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_example_single_lamp_with_terminals.htm"
file: "eececad_k_example_single_lamp_with_terminals"
category: "eececad"
---

# A single lamp and its terminals

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## A single lamp and its terminals

Since the lamps are displayed in two variants you require two macros with the same name for the ECAD object but different specifications of the variant. The multiple use is realized through multiple instantiation in EEC. The lamp needs a plug in order to connect the macro graphic with a socket in the basic wiring diagram. In addition, a placeholder object (anchor symbol) is needed for the definition of the parameters â here: Terminal1, Terminal2 and DT \- required. The window macros for the lamp in the variants A (right) and B (left) look as follows:

Via the EP plug, the lamp is connected with a socket from the basic wiring diagram. The parameters DT, Terminal1 and Terminal2, as well as the page number and index of the lamp, are filled with project-specific values in EEC.

The rule for the use of variant A or B is specified as a formula in the Variant parameter so that the lamps from 1 to 4 are placed as variant A and the lamp 5 as variant B.
