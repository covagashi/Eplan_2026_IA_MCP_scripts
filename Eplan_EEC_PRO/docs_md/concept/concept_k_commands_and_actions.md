---
title: "Commands and actions"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_commands_and_actions.htm"
file: "concept_k_commands_and_actions"
category: "concept"
---

# Commands and actions

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Commands and actions

Commands are objects that have exactly one method, called an âexecuteâ method. A sequence of methods can be called by assembling a list of commands. Such a list is used, for example, in connection with SequenceSelectionActions.

The plug-ins of the system provide commands via system libraries:

[](../Pictures/commands.png)

Management tasks, e.g. activating and deactivating the formula cache (Start/StopFormulaCacheCommand) or saving changes (SaveObjectCommand), are provided as atomic commands. These are then assembled into a sequence to automate a workflow.

This fine-granular division into commands makes sense so as to provide options for performance optimization (e.g., use of an active formula cache for several commands, etc.).

Actions connect the user interface (UI) to the application logic.

[](../Pictures/editor_action.png)

The Action system object is the superclass for all future options that will be available when calling application-logic commands from the user interface.

Thus far, the types provided by the system are[SelectionActions](eecbase_k_methodology_selectionaction.htm), which always require selecting the object or objects for which an action is to be carried out. In the future, there may also be actions that donât require selection, and hence function âgloballyâ.

A SelectionAction takes a set of selected objects (selectedEOs, usually a multi-selection) and transfers it to its internal run method

[](../Pictures/editor_selectionaction.png)

SelectionActions have the following attributes:

     * **Image:** The icon shown here is displayed both in the popup menu and as a button on the toolbar when the Occurs In Project Toolbar option is enabled.
     * **Selected object:** Object within the classification hierarchy of the application model for which the action can be executed. For example, if the RTS24 object of the Pfuderer model is selected, the action will be displayed only in the popup menu for RTS24 objects (classes/instances).
     * **Visible in library/Visible in projects:** Specifies whether the action for classes (library) or instances (projects), or both, can be executed, for example, only for RTS24 instances in project configurations
     * **Number of selected objects:** Specifies how many objects can/must be selected in order for the action to be executed in a meaningful manner. Examples include 1, 1..2, 3..6, + (=1..n)  
Note: This specification is derived, for example, from boundary conditions of the implementation of the run method. This may be set up only for the processing of one object.
     * **Popup path:** Defines the path to the action within the popup menu. The individual path entries are separated by a forward slash. For example, menu/sub menu/create.
     * **Displayed Name:** Action name displayed in the popup menu.
     * **Occurs In Project Toolbar****:** A button that can be used to start the action is added to the toolbar in the project explorer view.

**Note:** To make this change visible, the view must be closed and re-opened (or EEC must be restarted).

Finding SelectionActions:

When modifying a pop-up structure that consists of many actions, it is important to ensure that it is possible to navigate from a pop-up entry to the corresponding action. This can be achieved by executing the action via the popup menu while holding down the [CTRL] key.

SelectionActions can be adjusted in any manner via scripts. But customizing the UI does require scripting expertise in this case. Scripts also have the disadvantage that the script code specifies when to call which commands, for example. The relationship between actions and commands is not modeled, and therefore cannot be navigated.

For defining simple actions, the system object SequenceSelectionAction has been defined. It allows for the specification in table form of a sequence of [Commands](refcommands_r_commands.htm).

[](../Pictures/folge.png)

The relationships between actions and commands are modeled for SequenceSelectionAction. This means that it is possible, for example, to use standard mechanisms (ALT+ mouse) to navigate from the table with commands (see the above screenshot) directly to the commands.

When a SequenceSelectionAction is executed, a script is created automatically from the modeled sequence of commands in the background, and then executed as a general SelectionAction.
