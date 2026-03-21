---
title: "Properties of connection points"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_properties_of_connection_points.htm"
file: "concept_k_properties_of_connection_points"
category: "concept"
---

# Properties of connection points

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Properties of connection points

Every connection point is modeled by a parameter and can be one or more bits wide. Formulas are used to calculate the addresses of the connection points, beginning with the terminalâs start address. This makes it possible to implement any and all company guidelines for addressing. When connecting, the IO generator registers the addresses of the connection points for wiring the sensors and actuators.

The IO generator joins the terminalâs connection points with those of the sensors and actuators, provided their properties coincide. These properties are:

    1. Connection point type: Connection point types classify the mechanical (e.g. plug face), electrical (e.g. voltage, current), and controller-oriented (e.g. input or output) properties of the connection points. Each connection is modeled by a parameter, with the parameter type specifying the type of connection point (e.g. IX24V for a binary 24V input).

    2. Bus type: Functional requirements may stipulate that sensors and actuators be connected via different buses. For example, actuators that continue to receive power during an emergency-stop situation are connected to a different bus than those that are switched off during such a situation. Buses are modeled by parameters that name the incoming and outgoing bus type, thus categorizing the buses (e.g. on_for_emergency_stop and off_for_emergency_stop  (see the figure for the differentiation of bus types). If only one bus type is needed, there is no need to decide the bus type or to specify the bus type during the modeling process.

    3. Effective range: Controller components can be defined in such a way that only the sensors and actuators of a machine or plant that are installed at certain locations can be connected. In order to ensure, for example, that cables are as short as possible and do not run through the machine (see the diagram on Effective rage) , effective ranges can be defined. If all of a projectâs controller components have the same effective range (e.g. in a plant that employs a central control technique), there is no need to model the effective range.
