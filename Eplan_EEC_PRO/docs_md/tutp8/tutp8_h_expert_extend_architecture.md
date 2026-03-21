---
title: "Expanding the architecture"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_expert_extend_architecture.htm"
file: "tutp8_h_expert_extend_architecture"
category: "tutp8"
---

# Expanding the architecture

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Expanding the architecture In the architecture the Actuator and Sensor components represent the lowest level. Every other type therefore requires an extension of the architecture. To be able to expand the architecture flexibly, you now create a Function component that may be installed in itself and all other components. [Create the Function component](javascript:void\(0\);)
    1. Mark the Levelcomponents unit in the T_Mechatronic_Architecture library.
    2. Select [New > Object] from the popup menu.
    3. The New_Library_Object wizard opens.
    4. Navigate to Object > Component > MechatronicComponent.
    5. Click [Finish].
    6. The wizard is closed and you return to the editor for a new object.
    7. Enter Function in the Name field.
    8. Select the Level6.gif file in the Image field.
    9. Select the Abstract check box.
    10. Save the component.
    11. The architecture component Function is contained in the Levelcomponents unit.
[Extending the level configuration](javascript:void\(0\);)
    1. Open the new Function component.
    2. Switch to the Level configuration editor.
    3. Click  to open the Finder dialog.
    4. Click [Search].
    5. Highlight the Function component.
    6. Confirm with [OK].
    7. Save the component.
    8. Repeat Steps 1 to 7 for all other components.
    9. A component of the Function type is installed in all components and also in itself.
