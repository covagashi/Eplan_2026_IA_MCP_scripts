---
title: "Parameterizing connection point designations"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_parameterize_connections.htm"
file: "eececad_k_parameterize_connections"
category: "eececad"
---

# Parameterizing connection point designations

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Parameterizing connection point designations

The connection point designations of a macro are controlled by means of a variable in the placeholder object.

To this purpose the user has to agree a variable for the <20038> Connection point designations (all) property in P8.

The value for the connection point designation is specified by using the syntax ='Connection point1;Connection point2;Connection pointX'.

The following table shows how a variable is agreed for the <20038> Connection point designations (all) property in P8 using a relay coil as an example:

Row | Property | Current value | Variable  
---|---|---|---  
19 | <20038> Connection point designations (all) | A1;A2 | <ConnectionPointDesignation>  
  
As a result the macro with this placeholder object has the parameter ConnectionPointDesignation.

In the schematic the value ='A3;A4' results in a symbol with the connection points A3 and A4:
