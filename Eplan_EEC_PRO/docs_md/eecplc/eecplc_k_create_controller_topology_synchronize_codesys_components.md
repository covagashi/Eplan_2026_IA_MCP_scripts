---
title: "Synchronization of CoDeSys components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_create_controller_topology_synchronize_codesys_components.htm"
file: "eecplc_k_create_controller_topology_synchronize_codesys_components"
category: "eecplc"
---

# Synchronization of CoDeSys components

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Synchronization of CoDeSys components

Out of the resources of the CoDeSys components, automatically parameters for the corresponding components are to be created. Assigning a resource to a component of the type Controller is optional, but for all others it is mandatory.

If the resource of a component is changed or deleted, this can be synchronized to adapt the parameters of the component automatically.

For components of the Source type for each parameter the property VarType exists, which among others, identifies the origin of the parameter. If this is set to SYSTEM, it is not taken into account for synchronization. However, the parameter remains in any case.

If the source of a component of the Controller type is deleted and synchronized subsequently, this will delete all parameters of the component.
