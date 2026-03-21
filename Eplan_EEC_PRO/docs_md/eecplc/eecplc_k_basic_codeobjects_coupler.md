---
title: "Couplers"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_basic_codeobjects_coupler.htm"
file: "eecplc_k_basic_codeobjects_coupler"
category: "eecplc"
---

# Couplers

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Couplers

A coupler represents the junctions between communication channels of all types. A coupler does not define a protocol, but rather the logic distribution of the hardware by bus couplers and/or communication modules. By means of a subdivision of the same communication channel you can, for example, combine signals that belong to different emergency-off areas into separate logic channels that physically form a single bus point.

### Note

You have to equip the Coupler object with the parameters for structure formation and must implement the ICoupler interface so that the IO generator for address calculation can work error-free.

### Read more

     * [Specifying effective ranges:](eecplc_k_set_fields_of_action.htm)
     * [Modeling bus topology](eecplc_k_create_controller_topology_modeling_bustopology.htm)
     * [Create controller components](eecplc_k_create_controller_topology_create_controller_components.htm)
     * [Synchronization of CoDeSys components](eecplc_k_create_controller_topology_synchronize_codesys_components.htm)
