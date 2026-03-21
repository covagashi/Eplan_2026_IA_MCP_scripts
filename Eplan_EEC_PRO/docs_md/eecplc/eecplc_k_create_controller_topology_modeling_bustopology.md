---
title: "Modeling bus topology"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_create_controller_topology_modeling_bustopology.htm"
file: "eecplc_k_create_controller_topology_modeling_bustopology"
category: "eecplc"
---

# Modeling bus topology

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Modeling bus topology

The controller components are hierarchically connected via buses. Starting from the controller, a bus leads to a series of bus couplers or directly to the terminals. The bus coupler directs the controller signal from the incoming bus through the outgoing bus to terminals and/or other bus couplers.

A bus is created between controller and bus coupler when the OutgoingBus parameter is available to the controller, the IncomingBus parameter is available to the bus coupler, and both have the same value. Likewise, for a connection between a bus coupler and a terminal, it is necessary to set the OutgoingBus parameter for the bus coupler, the IncomingBus parameter for the terminals that the coupler connects to, and the bus type. The following diagram presents an example of the modeling of a bus topology.

If the (Model > Model variables menu) Disciplines > Fieldbus > Define device names outgoing buses model variable is set to true, then the controller components do not require the OutgoingBus parameter, because in this case a bus with the names of the control components will be depicted.

Controller components without incoming-bus parameters are assigned to the so-called standard bus by the IO generator. The standard bus is set up automatically by the user, independently of the modeling.

The names of the OutgoingBus and IncomingBus parameters can be changed via the (Model > Model variables menu) Disciplines > Fieldbus > Name of the parameter for the outgoing bus  or the Name of the parameter for the incoming bus  model variables.
