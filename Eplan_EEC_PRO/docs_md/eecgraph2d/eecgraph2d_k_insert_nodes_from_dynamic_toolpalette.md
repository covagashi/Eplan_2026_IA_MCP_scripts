---
title: "Inserting nodes from dynamic tool palette"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecgraph2d_k_insert_nodes_from_dynamic_toolpalette.htm"
file: "eecgraph2d_k_insert_nodes_from_dynamic_toolpalette"
category: "eecgraph2d"
---

# Inserting nodes from dynamic tool palette

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Inserting nodes from dynamic tool palette

If the project structure contains instances that still have to be inserted in the diagram, they can be collected in the palette by means of an appropriate configuration and can then be inserted from the palette into the diagram. The <nodeCreation> element creates a palette entry for each project component that can be specified by means of a formula for the entries attribute. Selecting the palette entry attaches the node to the mouse cursor, allowing it to be placed in the diagram via a left click.

If a node, which is determined by a formula of the attribute entries is deleted from the diagram, it is put back to the palette.

### [Example code](javascript:void\(0\);)

All the nodes of the project components of the BodyshellWork_Architecture.LevelComponents.Safety_circuit type are determined and those inserted into the palette that have not yet been placed in the âBodyshellâ work diagram.
    
        <paletteEntry id="SchutzkreisCreation"
    	group="Komponenten" text="=$Bezeichnung"  
    	
    	smallIcon="=type('Rohbau_Baukasten.Diagramm_Konfiguration.Planungs_Diagramm.  
    	Werkzeugpalette_Schutzkreis_Objekterstellung').getImage"  
    	
    	largeIcon="=type('Rohbau_Baukasten.Diagramm_Konfiguration.Planungs_Diagramm.  
    	Werkzeugpalette_Schutzkreis_Objekterstellung_24').getImage">  
    	
    	<nodeCreation entries="=rmos('Rohbau_Architektur.Ebenenkomponenten.  
    	Schutzkreis')"/>  
    </paletteEntry>

Result:
