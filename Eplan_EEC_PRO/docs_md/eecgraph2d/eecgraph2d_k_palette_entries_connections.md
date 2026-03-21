---
title: "Palette entries for connections"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecgraph2d_k_palette_entries_connections.htm"
file: "eecgraph2d_k_palette_entries_connections"
category: "eecgraph2d"
---

# Palette entries for connections

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Palette entries for connections

Components that are to be connected together manually in a diagram require a palette entry that creates both a connection line in the diagram and a reference between the components to be connected.

The following code snippet begins by describing which project components (instances of Function) can be connected by means of parameters (Child and Parent).

### [Example code](javascript:void\(0\);)
    
        <reference id="ReihenfolgeReferenz" type="connectable"
    	src="=isInstanceEO() and
    		isInstanceOf('Rohbau_Architektur.Ebenenkomponenten.Funktion')"
    	target="=isInstanceEO() and	
    		isInstanceOf('Rohbau_Architektur.Ebenenkomponenten.Funktion')">
    	<forward multiplicity="*" connector="=getParameter('Nachfolger')"/>
    	<backward multiplicity="*" connector="=getParameter('VorgÃ¤nger')"/>
    </reference>

This code snippet, which is also referenced, specifies how the connections are to be displayed:

### [Example code](javascript:void\(0\);)
    
        <connection id="Reihenfolge"
    	reference="ReihenfolgeReferenz"
    	width="3"
    	style="1"
    	color="17,240,70"
    	sourceDeco="empty"
    	targetDeco="filled-arrow"/>

The palette entry references the code fragment for displaying the connections. The Order text is displayed as a palette entry, along with either a small icon (smallIcon) or a large one (largeIcon), depending on the setting.

### [Example code](javascript:void\(0\);)
    
        <paletteEntry id="ReihenfolgeVerbindung"
    	group="Verbindungen"
    	text="Reihenfolge"
    	smallIcon="=type('Rohbau_Baukasten.Diagramm_Konfiguration.Planungs_Diagramm.
    		Werkzeugpalette_Reihenfolge_Verbindung').getImage"
    	largeIcon="=type('Rohbau_Baukasten.Diagramm_Konfiguration.Planungs_Diagramm.
    		Werkzeugpalette_Reihenfolge_Verbindung_24').getImage">
    	<connectionCreation connection="Reihenfolge"/>
    </paletteEntry>

Result:
