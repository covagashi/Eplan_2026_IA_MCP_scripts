---
title: "SequenceSelectionActions"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_methodology_sequenceselectionaction.htm"
file: "eecbase_k_methodology_sequenceselectionaction"
category: "eecbase"
---

# SequenceSelectionActions

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## SequenceSelectionActions

SelectionActions can be adjusted in any manner via scripts (see [SCRIPTING]()). But customizing the UI does require scripting expertise in this case. Scripts also have the disadvantage that the script code specifies when to call which commands, for example. The connection between actions and commands is not modeled, and therefore cannot be navigated either.

For the definition of simple actions, the system object SequenceSelectionAction has been defined. It allows for the specification in table form of a sequence of [Commands](refcommands_r_commands.htm).

The connections between actions and commands are modeled for SequenceSelectionAction, i.e., it is possible, for example, to use standard mechanisms ([Alt] \+ mouse) to navigate from the table with commands (see the above figure) directly to the commands.

When a SequenceSelectionAction is executed, a script is created automatically from the modeled sequence of commands in the background, and then executed as a general SelectionAction.

The command [Engineering.AbortExecutionIfErrorCommand]() is inserted in order to, in the event of an error that occurs during the execution of a command, to end the execution of the following commands.
