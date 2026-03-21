---
title: "SelectionActions"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_methodology_selectionaction.htm"
file: "eecbase_k_methodology_selectionaction"
category: "eecbase"
---

# SelectionActions

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## SelectionActions

A SelectionAction takes a set of selected objects (selectedEOs, usually a multi-selection) and transfers it to its internal run method

SelectionActions have the following attributes:

     * Image: The symbol here is displayed both in the context menu and as a button in the toolbar if the option Project explorer toolbar button is enabled.
     * Selected object: Object within the classification hierarchy of the application model for which the action can be executed. For example, if RTS24 of the Pfuderer model is selected, the action will be displayed only in the context menu for RTS24 objects (classes / instances).
     * Visible in library/Visible in projects: Specifies whether the action for classes (library) or instances (projects), or both, can be executed, for example, only for RTS24 instances in project configurations
     * Number of selected objects: Specifies the number of objects that can / must be selected so that the action can be executed in a meaningful manner. Examples include 1, 1..2, 3..6, + (=1..n)

Note: This specification is derived, for example, from boundary conditions of the implementation of the run method. This may be set up only for the processing of one object.

     * Popup path: Defines the path to the action within the context menu. The individual path entries are separated by a forward slash. For example, menu/sub menu/create.
     * Displayed Name: Action name displayed in the context menu.
     * Occurs In Project Toolbar: A button is added to the toolbar in the Project Explorer view, which is used to start the action.

Note: To make this change visible, the view must be closed and re-opened (or EEC must be restarted).

Finding SelectionActions:

When adjusting an pop-up structure that consists of many actions, it is important to ensure that it is possible to navigate from a pop-up entry to the corresponding action. This can be achieved by executing the action via the context menu, while keeping the [CTRL] key pressed.
