---
title: "Configuring connections"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutgraph2d_h_connections_configuration.htm"
file: "tutgraph2d_h_connections_configuration"
category: "tutgraph2d"
---

# Configuring connections

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Configuring connections The following configurations show two concepts for connections:
    1. Direct connections between nodes (persons and devices).
    2. Indirect connections between the slave nodes of the Master (devices among one another)
A connection is defined by the entry of the respective participating components in a parameter, for example, personal connection (see the following figure). The person (Worker) in the example is connected with the room components PC and Telephone. That is why the parameter WorkerConnection of Worker contains a list with the values <<PC>> and <<Telephone>> and the parameter WorkerConnection of PC, or Telephone contains the value <<Worker>>. For the complete configuration of the connections, three sub-aspects must be fulfilled:
    1. There must be at least one router configured, the ID of which the graphical depiction can reference.
    2. How the components to be connected reference each other must be configured.
    3. A graphical depiction of the connections should be configured.
