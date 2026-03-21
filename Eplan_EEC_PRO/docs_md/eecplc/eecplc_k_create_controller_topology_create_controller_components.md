---
title: "Create controller components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_create_controller_topology_create_controller_components.htm"
file: "eecplc_k_create_controller_topology_create_controller_components"
category: "eecplc"
---

# Create controller components

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Create controller components

A controller can consist of at least one controller, several bus couplers and any number of terminals. In the functional view, they are created as mechatronic components. In existing machines, they can be positioned either centrally or in a distributed manner (cf. the section on [Representing the controller in the functional structure](concept_k_representing_the_controller_in_the_functional_structure.htm)).

By assigning interfaces, each controller component is designated as either a controller, a bus coupler or a terminal. Because the interfaces required for this purpose are found in the PLC system library (Programmable Logic Controller), this library has to be imported from the library in which the controller components are compiled.

As illustrated in the sample chart provided above, each controller component has to be added to one of the following three interfaces:

    1. Controller (IController interface): Each machine has exactly one controller that controls all connections via an arbitrarily complex, hierarchical bus topology.
    2. Bus coupler (ICoupler interface): Connects the controller with a series of terminals or additional bus couplers via a bus.
    3. Terminal (ITerminal interface): A terminal has connections across which the sensors and actuators are connected and controlled.

In very simple cases, it is possible to do without terminals and/or bus couplers, because a controller also contains the functionality of a bus coupler and a terminal and because a bus coupler can take on the function of a terminal.
