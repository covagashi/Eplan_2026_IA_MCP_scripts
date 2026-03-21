---
title: "Instantiating nodes from the tool palette and inserting them into the diagram"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecgraph2d_k_insert_nodes_as_instance_from_toolpalette.htm"
file: "eecgraph2d_k_insert_nodes_as_instance_from_toolpalette"
category: "eecgraph2d"
---

# Instantiating nodes from the tool palette and inserting them into the diagram

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Instantiating nodes from the tool palette and inserting them into the diagram

In addition to standard elements, the tool palette can also contain nodes and edges. When a palette entry is selected and the mouse cursor is moved over the diagram, a command is simultaneously run to determine which placeholder or extension point can receive the new project component. The appearance of the mouse cursor changes accordingly to indicate where the new node may be inserted.

The new node is positioned in the diagram via a left click, and the project component is simultaneously inserted at the specified placeholder.

### [Example code](javascript:void\(0\);)

A palette entry and a command for instantiating from the tool palette:
    
        <paletteEntry id="RoboterCreation" group="Komponenten" text="Roboter"
    	smallIcon="=type('Rohbau_Baukasten.Diagramm_Konfiguration.
    	Planungs_Diagramm.Werkzeugpalette_Roboter_Objekterstellung').getImage"
    	largeIcon="=type('Rohbau_Baukasten.Diagramm_Konfiguration.
    	Planungs_Diagramm.Werkzeugpalette_Roboter_Objekterstellung_24').getImage">
    	<eoCreation command="command3"/>
    </paletteEntry>
    <command xsi:type="instantiateAndCreateNode" src="=isClassEO() and  
    	(absoluteName='Rohbau_Baukasten.Mechatronik.Roboter')"  
    	eoClassPath="Rohbau_Baukasten.Mechatronik.Roboter" id="command3"/>

Result:
