---
title: "Create different variants of an object"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutmechatronic_h_create_different_forms_of_one_object.htm"
file: "tutmechatronic_h_create_different_forms_of_one_object"
category: "tutmechatronic"
---

# Create different variants of an object

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Create different variants of an object In the sample station Feeder, two types of position sensors are required that differ in their functions: optical position sensors, and sensors that detect the position by means of inductance. Different variants are created through inheritance:
    1. Open the Positionsensor (double-click) and set it to Abstract by activating the check box of the same name to prevent a general position sensor being instantiated incorrectly.
    2. In the Sensors unit, create two sensors with the names Positionsensor_optical and Positionsensor_inductive.
    3. Open the two components just created, and in the Super class field, enter Positionsensor in each case.
If no separate symbol is assigned for a component, it will inherit the one from its super class. Since images can be assigned only to components of the architecture library, the new components display the symbols inherited from the architecture library. The modular system with all mechatronic components should now look like this: If a wrong symbols appears, then the wrong super class was selected. To correct this, double-click the respective components to open it, and in Super class select the correct abstract component (click [..] in the input box). After saving ( or [Ctrl] + [S]) and updating ([F5]), the modifications become visible. Level components and units can also be sorted by alphabet (see [Preferences for Unit Explorer](admin_r_prefs_unit_explorer.htm)).
