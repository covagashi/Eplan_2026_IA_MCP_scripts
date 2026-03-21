---
title: "Representation in the functional structure"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_representation_in_the_funtional_structure.htm"
file: "concept_k_representation_in_the_funtional_structure"
category: "concept"
---

# Representation in the functional structure

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Representation in the functional structure

The machine contains three stations that are controlled by two bus couplers. Because the bus couplers cannot be assigned to any station, central modeling is the recommended approach (cf. [Representing the controller in the functional structure](concept_k_representing_the_controller_in_the_functional_structure.htm): Central modeling). Thus, in the functional view, the machine contains a control computer, which in turn contains two bus couplers, which themselves contain a series of terminals.

During the configuration process, different variants and forms of the machine can be created. Depending on the variant, the controller must make the required connection points available so that any existing sensors and actuators can connect to them. During the modeling process, bus couplers should be assigned as many terminals as necessary to ensure that enough connection points are available for every conceivable variant. Terminals that are not needed in a given configuration variant are deactivated by means of disabler formulas.
