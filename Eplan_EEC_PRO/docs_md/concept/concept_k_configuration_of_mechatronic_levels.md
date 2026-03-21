---
title: "Configuration of mechatronic levels"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_configuration_of_mechatronic_levels.htm"
file: "concept_k_configuration_of_mechatronic_levels"
category: "concept"
---

# Configuration of mechatronic levels

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Configuration of mechatronic levels

Starting position:

The functional structure of a machine or facility is hierarchical. The levels comprising this hierarchy are variously defined, depending on the industry or company. In mechanical engineering the following hierarchy levels are standard: Machine, function group, function. In the auto body industry, for example, the standard levels are factory, segment, plant, operation, function, etc.

From the perspective of a plant manufacturer, hierarchy levels are often specific to the order and are specified by the customer, so that the builderâs employees have to work with different architectures simultaneously, if they are working on several projects at the same time. Rules are connected with these hierarchy levels, for example, the rule that only function groups, not functions, are permitted below the level of a machine.

Requirements:

     * Hierarchy levels must be configurable in a company-specific manner
     * It must be possible to define rules connected with hierarchy levels
     * EEC must ensure that the rules are observed during both modular system development and configuration.
     * It must be possible to manage multiple hierarchy-level specifications within a single model.
     * Concept:

The modeling of hierarchy levels takes place inside libraries. The basis for this is the concept of level configuration, which is illustrated by the following example:

[](../Pictures/2007011203.png)

Subcomponents of MechatronicComponent are automatically **LevelComponents**. A permissible sub-level relationship can be created between level components. In this example, level components are defined for machine, station, and function. Stations can be installed in machines, and functions can be installed in stations. Functions, in turn, can be installed in functions. However, level configuration does not permit functions to be incorporated directly into a machine.

Components that are derived from levelcomponents (relationship is one) are automatically modular components. This means that within the inheritance hierarchy levelcomponents can only be found directly below the MechatronicComponent component!

Level configuration provides the rules for developing the modular system. Level configuration ensures that only permissible composition relationships are built when nesting mechatronical components.

The rules of level configuration prevent a modular-system developer from, for example, integrating the âtransportâ function directly into Machine RTS24.

Furthermore, level configuration also validates the instantiation of modular system components in a project. It is permissible, for example, to install the âinsertingâ station in Component RTS24_1 of type RTS24, because the level configuration allows stations to be installed in machines. However, the gripper may not be installed directly under Component RTS24_1.
