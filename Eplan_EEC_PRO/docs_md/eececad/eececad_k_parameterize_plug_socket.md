---
title: "Parameterizing plugs and sockets"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_parameterize_plug_socket.htm"
file: "eececad_k_parameterize_plug_socket"
category: "eececad"
---

# Parameterizing plugs and sockets

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Parameterizing plugs and sockets

The lights in the example can contain up to 5 lamps, which is why the page defines 5 sockets. At each socket, a lamp can be docked via its plug. Each socket must have a name that is unique within the component (Lamp1 to Lamp6).

To place a lamp on the lighting, its plug called EP (=placeholder) must be set to the value of a socket, for example, Lamp1. The variant (A or B) is calculated with a if-then-else loop for the parameter of the same name.

The following image shows the mechatronic project components on top in which the calculation of the parameter values take place and the discipline-specific project component below that adopts the calculated parameter values.
