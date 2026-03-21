---
title: "Commands"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_methodology_command.htm"
file: "eecbase_k_methodology_command"
category: "eecbase"
---

# Commands

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Commands

Commands are objects that have exactly one method, called an execute method. This way, a sequence can be called from methods by compiling a list of commands. Such a list is used, for example, in connection with [SequenceSelectionActions](eecbase_k_methodology_sequenceselectionaction.htm).

The plug-ins of the system provide commands via system libraries:

Management tasks, for example, enabling and disabling the formula cache (Start/StopFormulaCacheCommand) or saving of changes (SaveObjectCommand, are provided as atomic command operations. These are used to compile a sequence to automate a workflow (also see [Commands](refcommands_r_commands.htm)).

This fine-granular division into commands makes sense so as to provide options for performance optimization (e.g., use of an active formula cache for several commands, etc.).
