---
title: "Effective range for bus couplers"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_effective_range_for_bus_couplers.htm"
file: "concept_k_effective_range_for_bus_couplers"
category: "concept"
---

# Effective range for bus couplers

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Effective range for bus couplers

The effective ranges of the controller components in the machines illustrated in the [IO generation](concept_k_io_generation.htm) diagram are oriented by the grid that results from the division into stations and the distinction between upper and lower substations. The following six locations may be used in defining the effective ranges: 1-upper, 1-lower, 2-upper, 2-lower, 3-upper, and 3-lower.

Bus coupler A, together with its terminals, is installed in the lower area of the machine between station 1 and station 2, while bus coupler B is installed in the upper area between station 2 and station 3. In order to avoid having to run a cable through the machine, all sensors and actuators from stations 1 and 3 should be connected to bus couplers A and B, respectively. The middle station is divided in two: the sensors and actuators from the lower and upper substations should be connected with bus couplers A and B, respectively.

The effective range of bus coupler A therefore covers the locations 1-upper, 1-lower, and 2-lower, while bus coupler B covers 2-upper, 3-upper, and 3-lower.

A location can be used in more than one effective range, i.e. the effective ranges may overlap. In this case, it is up to the IO generator to decide which of the overlapping controller components should be connected to the connection points of the sensors and actuators.
