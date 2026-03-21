---
title: "Plug-Socket concept"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_plug_socket_concept.htm"
file: "concept_k_plug_socket_concept"
category: "concept"
---

# Plug-Socket concept

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Plug-Socket concept

The modularization of discipline-specific resources is accomplished via the **Plug -Socket concept**. The socket is viewed here as a receptacle that one or more plugs can plug into. For example, a fragment of a schematic may contain a socket where several other fragments can be positioned via plugs.

Sockets and plugs are defined more clearly in what follows:

     * Socket: A socket may be viewed as an electrical socket. Plugs can be plugged into these sockets. More than one plug can be plugged into a single socket. However, a plug can only be plugged into a single socket. Sockets also serve as graphical reference points, e.g. on a schematic page. Other elements, fragments, can be positioned relative to these reference points, e.g. on a schematic page (1:n relationship). These elements or fragments must be equipped with parameters of the Plug type.
     * Plug: ECAD objects with plug-type parameters are used to connect electro-technical elements to sockets. This involves a plug docking with the assigned socket on a schematic page. The assignment is made based on parameter values. It is also possible for more than one plug to reference a single socket (1:n relationship).

If the discipline components have to be installed in a specific sort order for a 1:n relationship, these have to be extended with the parameter for the sort order (see [Parameter name for the sort order](admin_r_modelvar_order_of_discipline_components.htm)).

The plug-socket concept can be applied in every discipline. It is a very powerful means for creating relationships between components, software function blocks, macros, text blocks, etc.

There are two strategies for the Plug-Socket concept:

     * Names are sockets In order to form the discipline structure a search is carried out for superordinate components whose names correspond to the values of plugs in subordinate components.  
[](../Pictures/2016070801.png)
     * Names do not define sockets: In order to form the discipline structure a search is carried out for superordinate components whose values of sockets correspond to the values of plugs in subordinate components.  
[](../Pictures/2016070802.png)

If no strategy is specified, the strategy Names do not define sockets is first applied. If no socket values can be determined that correspond to the plug values, the strategy Names are sockets is used in order to create a discipline structure.

### Note

The level hierarchy of the discipline components is taken into consideration in both strategies.
