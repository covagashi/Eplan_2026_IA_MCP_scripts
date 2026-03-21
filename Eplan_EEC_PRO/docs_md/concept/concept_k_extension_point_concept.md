---
title: "Extension point concept"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_extension_point_concept.htm"
file: "concept_k_extension_point_concept"
category: "concept"
---

# Extension point concept

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Extension point concept

In modern programming languages (Java, C#) there is an extension point concept that applies to interfaces. Its purpose is to formally specify the interfaces of a component independently of its implementation. Components can implement several interfaces, which makes multiple interface inheritance possible.

The inheritance concept itself already allows for parameters of components to be standardized (the AbstractStation component of the Pfuderer model, for example, defines the parameters StationNumber, Location, Plant, and FunctionText, which are inherited by the components Inserting, Magazine, etc.). But it is both the interface (selection of parameters) and implementation (formulas, methods) that are inherited by child classes.

The extension point concept makes it possible to use components to define interfaces and/or interface hierarchies independently of their implementation.

The ILocation interface represented in the diagram begins by defining, independently of the implementation, that a component that implements this interface must have the Place and StationNumber components. This interface can then be assigned, for example, to the AbstractStation and TurningPlate components.

This example shows that interfaces can be used to define additional classifications: Using the ILocation interface, all components are selected that have the parameters required for adequately specifying the location, namely the Place and StationNumber parameters.
