---
title: "Modularization of controller software"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_modularization_of_controller_software.htm"
file: "concept_k_modularization_of_controller_software"
category: "concept"
---

# Modularization of controller software

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Modularization of controller software

With the aid of the PLC modular system, plant-specific software elements can be created for a very broad range of programming systems. This includes the automatic generation of program calls, instance blocks, and symbol tables.

Depending on the target platform (Siemens, CoDeSys, Phoenix, etc.) it is also possible to automatically import the code into the target system and, in some cases, even compile it automatically.

When creating documents, the first step is to create discipline-specific structures from the functional, mechatronic plant structure. This means that all objects belonging to the selected PLC discipline are assembled in accordance with the rules of that discipline. The second step is to create and, if necessary, to compile the code for the target system using these discipline-specific structures.
