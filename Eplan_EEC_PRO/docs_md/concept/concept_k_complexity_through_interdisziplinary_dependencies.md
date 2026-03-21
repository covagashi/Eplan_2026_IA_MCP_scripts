---
title: "Complexity through interdisciplinary dependencies"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_complexity_through_interdisziplinary_dependencies.htm"
file: "concept_k_complexity_through_interdisziplinary_dependencies"
category: "concept"
---

# Complexity through interdisciplinary dependencies

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Complexity through interdisciplinary dependencies

The following diagram illustrates that even small changes, such as the decision to accomplish the reset movement of a gripper using a valve or a spring, generally affect the project documents for all of the involved disciplines:

The possible variants of return movements for the gripper in this example (valve/spring) lead to different entries in the mechanics BOM. If the variant 'return movement via valve' is chosen, then the valves must be documented in fluid diagrams. The control of the valves must be considered in the schematics diagram. And the PLC software must be extended by the valve control as well.

Already this little example shows the impact on all disciplines by one possible variant in a sub function of a machine.

The example illustrates the following problems:

     * Employees from **different specialist disciplines** within mechanical engineering are involved in the development of reusable components. **Complex components** arise that require **project documents** from different disciplines: Wiring diagrams, mechanical drawings, control programs, hydraulic and pneumatic plans, documentation, etc.
     * Existing **IT systems** are used in a manner that varies with the discipline and department. An overarching comparison between the systems is lacking (**isolated solutions**). The realities of this situation make it difficult to implement modular approaches in practice.
