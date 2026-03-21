---
title: "Configuring a router"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutgraph2d_h_connections_configuration_router_configuration.htm"
file: "tutgraph2d_h_connections_configuration_router_configuration"
category: "tutgraph2d"
---

# Configuring a router

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Configuring a router The persons (workers) are to be connected to the devices (PC, Telephone) by means of polylines, which can have any number of bend points, and the LAN jacks (LAN_Jack) of the devices (PC, Telephone, Printer, 2way_LANJack, 5waySwitch) between one another through direct lines.
    1. Replace the configuration of the router <router id="router"> with the following lines.
    
        <!-- Router -->
    <!-- Router for connecting worker and device -->
    <router id="Bendpoint" class="com.mind8.graph2d.router.Bendpoint" />
    <!-- Router for connecting slave and device -->
    <router id="ShortestPath" class="com.mind8.graph2d.router.ShortestPath" />

    1. In the tag <diagramEditor>, change the attribute router=ârouterâ to router="ShortestPath".
[Explanation](javascript:void\(0\);) The ID of the first router is Bendpoint, that of the second is ShortestPath. The types of router are specified by the same respective class names. For more types, see the section [router](refgraph2d_r_router.htm) in the Reference chapter. Since the ID router has been replaced, the reference to the ID of the router in the tag <diagramEditor> has to be changed. The default router should be the one with the ID ShortestPath.
