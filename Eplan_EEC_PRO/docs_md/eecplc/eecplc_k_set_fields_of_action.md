---
title: "Specifying effective ranges:"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_set_fields_of_action.htm"
file: "eecplc_k_set_fields_of_action"
category: "eecplc"
---

# Specifying effective ranges:

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Specifying effective ranges:

The effective ranges are defined in the following steps:

    1. Modeling of the installation location for sensors and actuators.
    2. Modeling of effective ranges for controller components.

The installation location for sensors and actuators is determined using the parameter for the location. The classification scheme applied here is often based on location designations for resource identification.

The effective range of the controller components is set using the parameter for the locations. If the effective range covers several locations, these locations are registered as a collection in the Locations parameter (see the below diagram).

If the controller component has only one location as its effective range, this can be entered as a character string (see the below diagram).

The name of the parameter for defining the effective range can be changed via the (Model > Model variables menu) Disciplines > Fieldbus > Parameter for the location and Parameter for the locations model variables.
