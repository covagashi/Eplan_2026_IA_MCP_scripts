---
title: "Grouping palette entries"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecgraph2d_k_palette_entries_groups.htm"
file: "eecgraph2d_k_palette_entries_groups"
category: "eecgraph2d"
---

# Grouping palette entries

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Grouping palette entries

In addition to selection tools (Select and Marquee) and note-taking tools (Sticky Note and Sticky note connection) for planning diagrams, the palette can also contain any number of entries for instantiating components and creating connections between them.

To distinguish these entries visually, they are assigned to groups, as illustrated in the following sample code. The symbol definition has been left out of the code to make the example clearer.

### [Example code](javascript:void\(0\);)
    
        <paletteEntry id="Rohrverbindung" group="Verbindungen" text="Rohrverbindung" ...>
    	<connectionCreation connection="Wasserstrom"/>
    </paletteEntry>
    <paletteEntry id="Abschluss" group="Bauteile" text="HausabschlÃ¼sse" ...>
    	<eoCreation command="command9"/>
    </paletteEntry>
    <paletteEntry id="Behaelter" group="Bauteile" text="BehÃ¤lter" ...>
    	<eoCreation command="command8"/>
    </paletteEntry>
    <paletteEntry id="Rohre" group="Bauteile" text="Rohr" ...>
    	<eoCreation command="command10"/>
    </paletteEntry>

Result:
