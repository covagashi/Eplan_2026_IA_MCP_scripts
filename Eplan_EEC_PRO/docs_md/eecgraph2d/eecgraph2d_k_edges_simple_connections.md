---
title: "Simple connections"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecgraph2d_k_edges_simple_connections.htm"
file: "eecgraph2d_k_edges_simple_connections"
category: "eecgraph2d"
---

# Simple connections

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Simple connections

Simple connections serve to depict 1:1 references between two nodes, e.g. parent-child references.

This is illustrated using the example of two roller conveyors in the âBodyshell workâ demo model. In the planning diagram, a reference from parent SK1RLB1 (1) to child SK1RLB2 (2) is represented by a green arrow.

The parent node stores a reference to the child node in the Child parameter, and the child node stores a reference to the parent node in the Parent parameter (see [connection](refgraph2d_r_connection.htm)).

### [Example code](javascript:void\(0\);)
    
        <reference id="ReihenfolgeReferenz" type="connectable" src="=isInstanceEO()
    	and isInstanceOf('Rohbau_Architektur.Ebenenkomponenten.Funktion')"
    	target="=isInstanceEO() and
    	isInstanceOf('Rohbau_Architektur.Ebenenkomponenten.Funktion')">
    	<forward multiplicity="*" connector="=getParameter('Nachfolger')"/>
    	<backward multiplicity="*" connector="=getParameter('VorgÃ¤nger')"/>
    </reference>
    <connection id="Reihenfolge" reference="ReihenfolgeReferenz"
    	width="3" style="1" color="17,240,70"
    	sourceDeco="empty"
    	targetDeco="filled-arrow"/>

Connections between nodes can be created both manually and automatically.

Creating connections manually:

    1. Select a palette entry for âConnectionsâ (Order in the above screenshot)
    2. Click the first node.
    3. Click the second node.

Connections can be created continuously by simultaneously holding down [SHIFT].

Creating connections automatically:

If the ordering of the nodes derives, for example, from the ordering of the corresponding project components in the model structure, the connections are automatically inserted into the diagram.
