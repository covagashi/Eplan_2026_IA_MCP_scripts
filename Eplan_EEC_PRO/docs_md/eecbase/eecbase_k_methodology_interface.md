---
title: "Interface"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_methodology_interface.htm"
file: "eecbase_k_methodology_interface"
category: "eecbase"
---

# Interface

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Interface

In modern programming languages (Java, C#), there is a concept known as interfaces. Its purpose is to formally specify the interfaces of a component independently of its implementation. Components can implement several interfaces, which makes multiple interface inheritance possible.

The inheritance concept itself already allows for parameters of components to be standardized (the AbstractStation component of the Pfuderer model, for example, defines the parameters StationNumber, Location, Plant, and FunctionText, which are inherited by the components Inserting, Magazine, etc.) But it is both the interface (selection of parameters) and implementation (formulas, methods) that are inherited by child classes.

Thanks to the interface concept, it is now possible to define interfaces and / or interface hierarchies independently of their implementation by way of components.

the ILocation interface represented in the graphic at first defines, in an implementation-neutral manner, that a component that implements this interface must have the parameters Place and StationNumber. For example, this interface can then be assigned to the components AbstractStation and TurningPlate.

This example shows that interfaces can be used to define additional classifications: Using the ILocation interface, all components are selected that have the required parameters for sufficiently specifying the location, Place and StationNumber.

Using interfaces

     * Fieldbus linking:

So far, the algorithm for fieldbus linking has been able to detect control components of a configuration only indirectly on the basis of their containing control hardware components of a PLC discipline.

The current implementation of fieldbus linking now defines interfaces (IController, ICoupler, ITerminal) that can be used to highlight control components explicitly (Marker Interfaces).

     * Better performing formula requests:

rmos requests can generally be accelerated considerably through selective searches for a type and the definition of an rmos index.

But often it is not a specific type that is looked for, but, for example, all objects with the parameters A and B. Before these requests were formulated with a general rmos request, followed by a select Statement, which required a lot of computing capacity.

Here, interfaces allow for an additional classification and thus a better performing request: An interface is defined with parameters A and B, and assigned to all relevant component classes. The rmos request is now limited by means of the interface, instead of a type. An index can also be defined for interfaces.

Overall, interfaces allow for better, more expressive modeling. As the screenshot shows, interfaces can be extended (inherited), which means that interfaces hierarchies can be defined.

Note:

Similar to the Eclipse programming standard, we always precede interfaces with a capital âIâ.
