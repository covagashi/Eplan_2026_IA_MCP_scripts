---
title: "Expanding the architecture"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutword_h_expert_extend_architecture.htm"
file: "tutword_h_expert_extend_architecture"
category: "tutword"
---

# Expanding the architecture

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Expanding the architecture In the architecture the Actuator and Sensor components represent the lowest level. Every other type therefore requires an extension of the architecture. To be able to expand the architecture flexibly, you now create a Function component that may be installed in itself and all other components. [Creating the Function component](javascript:void\(0\);)
    1. Mark the Levelcomponents unit in the T_Mechatronic_Architecture library.
    2. In the popup menu select New > Object.
    3. Navigate to Object > Component > MechatronicComponent in the Create new library object dialog.
    4. Click [Finish].
    5. Enter Function in the Name field.
    6. Select the Level6.gif file in the Image field.
    7. Select the Abstract check box.
    8. Save the component.
[Expanding level configurations](javascript:void\(0\);)
    1. Open the new Function component.
    2. Switch to the Level configuration editor.
    3. Click  to open the Finder dialog.
    4. Click [Search].
    5. Highlight the Function component.
    6. Confirm with [OK].
    7. Save the component.
    8. Repeat Steps 1 to 7 for all other level components.
    9. This way a component of the Function type can be installed in all components and also in itself.
