---
title: "Enclosing discipline components in mechatronic components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutword_h_expert_encapsulate_discipline_comps.htm"
file: "tutword_h_expert_encapsulate_discipline_comps"
category: "tutword"
---

# Enclosing discipline components in mechatronic components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Enclosing discipline components in mechatronic components In the course of the tutorial discipline components were created once through a mass import. Then formulas (for example to calculate a plug) were entered for the parameter values. If a macro was changed, for example another parameter added and the discipline component synchronized with the changed macro, the parameter values were lost. For this reason each discipline component is enclosed (encapsulated) in a mechatronic component. In the mechatronic component the same parameters are created and the formulas inserted. The parameters of the discipline components then always reference the parameters (interface parameters) of the same name of the encapsulating mechatronic components. After a synchronization you then only have to insert the references on the interface parameter again. [Creating a unit for mechatronic components](javascript:void\(0\);) The encapsulating mechatronic components are to be created in a unit parallel to Word_Components.
    1. Select the T_Office_Word library.
    2. Select New > Unit in the shortcut menu.
    3. Specify the Wrapper name.
    4. Save the unit.
[Creating mechatronic components](javascript:void\(0\);) An encapsulating mechatronic component has to be created for each mechatronic component. Creating encapsulation for the discipline components
    1. Select the new Wrapper unit.
    2. In the popup menu select New > Mechatronics > Function.
    3. Specify the M_Body name.
    4. Switch to the Interfaces editor page.
    5. Click  to open the Finder dialog.
    6. Click [Search].
    7. Select the IBody.
    8. Confirm with [OK].
    9. Drag the Body discipline component into the component editor.
    10. Select the installed discipline component Body.
    11. Mark all parameters.
    12. Select Add interface temperature from the popup menu.
    13. Save the component.
    14. Repeat steps 1 to 13 with the names M_Chapter with the interface IChapter and the discipline component Chapter.
    15. Repeat steps 1 to 13 with the names M_Row with the interface IRow and the discipline component Row.
A reference to the parameter of the superior component (capsule) by the same name is now entered as the value. These parameters were inserted into the capsule during the same step. The parameter values are entered at a later step. [Adding plugs and sockets to discipline components](javascript:void\(0\);) To generate the Word discipline structure independent of the structure of the mechatronics, the discipline components have to be extended with plugs and sockets. This takes place in two steps:
    1. Extend the discipline components with the parameters Plug and Socket.
    2. Extend the encapsulating mechatronic components.
Extending Plugs and Sockets to discipline components:
    1. Open the component Body.
    2. Open the Parameters editor page.
    3. Drag the Socket parameter from the Word.Parameter unit in the editor.
    4. Repeat steps 1 to 3 for the Chapter component with the Plug and Socket parameters.
    5. Repeat steps 1 to 3 for the Row with the parameter Plug.
Extending encapsulating mechatronic components:
    1. Open the component M_Body.
    2. Select the installed Body discipline component.
    3. In the editor open the popup menu of the Socket parameter.
    4. Select Adding interface temperature.
    5. Save the editor.
    6. Repeat steps 1 to 5 for the M_Chapter and M_Row components with the newly added Plug and Socket parameters.
