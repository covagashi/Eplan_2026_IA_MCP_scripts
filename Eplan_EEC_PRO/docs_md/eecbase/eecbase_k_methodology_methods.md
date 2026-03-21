---
title: "Methods"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_methodology_methods.htm"
file: "eecbase_k_methodology_methods"
category: "eecbase"
---

# Methods

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Methods

In analogy to the object-based programming languages, it is possible to define for any objects not only parameters, but also methods.

Methods have

     * a name (e.g., execute),
     * arguments (e.g., List selectedEOS), as well as
     * a return type (e.g., Engineering.Object or no return type).

Generally, methods are used to navigate or modify model objects. These objects are known as EngineeringObject (EO). The EOs relevant to a method are typically selected by the user in a view. Frequently, these selected EOs are transferred as a list (selectedEOs, see screenshot).

A method can be implemented in Groovy (script), Native Java (plug-in) or through a sequence:

     * Groovy:

Due to the object-based integration of scripts into the application model, there are approved management options for scripts (see [SCRIPTING](refscripting_r_scripting.htm)).

     * Native Java:

Fully typed and with the option of remote debugging (see [SCRIPTING](refscripting_r_scripting.htm))

     * Sequence:

Table-format specification of a sequence (see [SequenceSelectionActions](eecbase_k_methodology_sequenceselectionaction.htm)).
