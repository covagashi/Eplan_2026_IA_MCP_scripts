---
title: "Configuring palette entries"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutgraph2d_h_configuration_of_palette_entries.htm"
file: "tutgraph2d_h_configuration_of_palette_entries"
category: "tutgraph2d"
---

# Configuring palette entries

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Configuring palette entries So far, only the components present in the project could be dragged into the diagram. In this step of the configuration, the palette is extended with entries for instancing new components and for creating new connections.  
    1. Add the following lines below the node with id="LAN_Path".
        
                <!-- Palette items -->
        <!-- Group "Building" -->
        <paletteEntry id="Floorplanning" group="Building" text="Floor" smallIcon="=type('IT_ModularSystem.Images.Floor').getImage" largeIcon="=type('IT_ModularSystem.Images.Floor').getImage">
        	<eoCreation command="create_Floor" />
        </paletteEntry>
        <paletteEntry id="Roomplanning" group="Building" text="Room" smallIcon="=type('IT_ModularSystem.Images.Room').getImage" largeIcon="=type('IT_ModularSystem.Images.Room').getImage">
        	<eoCreation command="create_Room" />
        </paletteEntry>
        <!-- Group "Devices" -->
        <paletteEntry id="Socketplanning" group="Devices" text="2way LAN Jack" smallIcon="=type('IT_ModularSystem.Images.2wayLANJack16').getImage" largeIcon="=type('IT_ModularSystem.Images.2wayLANJack16').getImage">
        	<eoCreation command="create_2wayLANJack" />
        </paletteEntry>
        <paletteEntry id="PCplanning" group="Devices" text="PC" smallIcon="=type('IT_ModularSystem.Images.PC16').getImage" largeIcon="=type('IT_ModularSystem.Images.PC16').getImage">
        	<eoCreation command="create_PC" />
        </paletteEntry>
        <paletteEntry id="Telephoneplanning" group="Devices" text="Telephone" smallIcon="=type('IT_ModularSystem.Images.Telephone16').getImage" largeIcon="=type('IT_ModularSystem.Images.Telephone16').getImage">
        	<eoCreation command="create_Telephone" />
        </paletteEntry>
        <paletteEntry id="Printerplanning" group="Devices" text="Printer" smallIcon="=type('IT_ModularSystem.Images.Printer16').getImage" largeIcon="=type('IT_ModularSystem.Images.Printer16').getImage">
        	<eoCreation command="create_Printer" />
        </paletteEntry>
        <paletteEntry id="Switchplanning" group="Devices" text="Switch" smallIcon="=type('IT_ModularSystem.Images.Switch16').getImage" largeIcon="=type('IT_ModularSystem.Images.Switch16').getImage">
        	<eoCreation command="create_5waySwitch" />
        </paletteEntry>
        <!-- Group "Worker" -->
        <paletteEntry id="Workerplanning" group="Worker" text="Worker" smallIcon="=type('IT_ModularSystem.Images.Worker16').getImage" largeIcon="=type('IT_ModularSystem.Images.Worker16').getImage">
        	<eoCreation command="create_Worker" />
        </paletteEntry>
        <!-- Group "Connections" -->
        <paletteEntry id="Worker" group="Connections" text="Worker connection" smallIcon="=type('IT_ModularSystem.Images.LAN_Connection').getImage" largeIcon="=type('IT_ModularSystem.Images.LAN_Connection').getImage">
        	<connectionCreation connection="Worker_Path" />
        </paletteEntry>
        <paletteEntry id="LAN" group="Connections" text="LAN connection" smallIcon="=type('IT_ModularSystem.Images.LAN_Connection').getImage" largeIcon="=type('IT_ModularSystem.Images.LAN_Connection').getImage">
        	<connectionCreation connection="LAN_Path" />
        </paletteEntry>

[Explanation](javascript:void\(0\);) The IDs of the palette entries are self-explanatory, but they are not referenced. The attribute group="Building" creates a group in the palette, or inserts a palette entry in the group of the same name. With the attribute text="Floor", a freely selectable text is assigned to the palette entry. The attributes smallIcon="=type('IT_ModularSystem.Images.Floor').getImage" and smallIcon="=type('IT_ModularSystem.Images.Floor').getImage" assign to the palette entry an image for the depiction of one large and one small icon. In the menu of the palette, it is possible to select whether the palette entries are to be displayed with or without text and with small or large icons. The tag <eoCreation command="create_Floor" /> specifies which command is to be executed if the palette element is inserted in the diagram. The tag <connectionCreation connection="Worker_Path" /> is used to reference the ID of a connection, when a connection is inserted.
