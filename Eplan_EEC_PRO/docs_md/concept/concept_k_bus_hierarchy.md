---
title: "Bus hierarchy"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_bus_hierarchy.htm"
file: "concept_k_bus_hierarchy"
category: "concept"
---

# Bus hierarchy

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Bus hierarchy

There are three distinct types of controller components that can be used to model controller topology:

    1. Terminals offer one or more connection points for sensors and/or actuators.
    2. Bus couplers can have terminals or other bus couplers connected to them. Like terminals, bus couplers can also have connection points (e.g. diagnostic inputs).
    3. Controllers have the same properties as bus couplers, i.e. they can have connection points (e.g. fast on-board IOs) and connected bus couplers. In addition, however, they have a CPU that runs control programs.

Regardless of the actual structure of the subnetwork topologies (e.g. ASI-line or SERCOS ring structure), all bus structures are modeled hierarchically during the functional configuration process (**bus hierarchy**).
