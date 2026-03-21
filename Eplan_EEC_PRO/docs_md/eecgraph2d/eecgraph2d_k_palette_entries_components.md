---
title: "Palette entries for components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecgraph2d_k_palette_entries_components.htm"
file: "eecgraph2d_k_palette_entries_components"
category: "eecgraph2d"
---

# Palette entries for components

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Palette entries for components

Components that are to be inserted into the diagram via a palette entry, thus creating an instance in the project, must have the following attributes and sub-elements:

     * id attribute: a unique name for the palette entry.
     * group attribute: Name of the group in which the palette element is incorporated.
     * text attribute: Text displayed in the palette.
     * smallIcon attribute: Icon that is displayed when the Use large icons setting is deactivated (size 16 x 16 pixels).
     * largeIcon attribute: Icon that is displayed when the Use large icons setting is activated (size 24 x 24 pixels).
     * eoCreation sub-element, command attribute: unique name of the command for instantiating the component.

The following sample code presents a complete definition for an individual palette entry. The definition of the command is also included, to illustrate the connection between the two definitions.

### [Example code](javascript:void\(0\);)
    
        <paletteEntry
    	id="Abschluss"
    	group="Bauteile"
    	text="HausabschlÃ¼sse"
    	smallIcon="=type('Wasserversorgung_Baukasten.Diagramm_Konfiguration.Bilder.abschlussSmallIcon').getImage"
    	largeIcon="=type('Wasserversorgung_Baukasten.Diagramm_Konfiguration.Bilder.abschlussLargeIcon').getImage">
    	<eoCreation command="command9"/>
    </paletteEntry>
    <command xsi:type="instantiateAndCreateNode"
    	src="=isClassEO() and (absoluteName='Wasserversorgung_Baukasten.Bauteile.Abschluss')"
    	eoClassPath="Wasserversorgung_Baukasten.Bauteile.Abschluss"
    	id="command9"/>

Result:

The following screenshot shows the palette entry with a large icon (right) and a small icon (left).
