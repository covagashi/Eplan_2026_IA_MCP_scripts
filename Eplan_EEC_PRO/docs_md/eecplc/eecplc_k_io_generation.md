---
title: "IO generation"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_io_generation.htm"
file: "eecplc_k_io_generation"
category: "eecplc"
---

# IO generation

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## IO generation

The conceptual application of IO generation is discussed in the chapter on [IO generation](concept_k_io_generation.htm). In the following passage, the depiction of this concept in EEC is explained.

The IO generator is a collection of predefined actions and related concepts for addressing connections to the controller and for connecting sensors and actuators to them. Implementation in EEC, e.g. what values should be set for what parameters, is described in what follows.

The structure of the first four subsections is based on the order in which a controller is compiled for a given facility or machine.

    1. Creating controller and controller topology: Applications for controller components in the functional view, along with their internal bus connections.
    2. Modeling sensors and actuators: Describes which sensor and actuator settings are preferable or possible.
    3. Modeling controller components On the controller side, connections are modeled and address specifications are made.
    4. Specifying effective ranges: Optionally, controller components can be coordinated spatially to machine components. This requires that specifications be provided for sensors and actuators, as well as for connection terminals.

The section on [IO generator actions](eecplc_k_io_generator_actions.htm) lists and explains the functions made available by the IO generator.
