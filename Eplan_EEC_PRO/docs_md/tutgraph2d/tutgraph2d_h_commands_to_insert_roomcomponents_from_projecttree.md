---
title: "Commands for inserting room components (RoomComponent) from the project tree"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutgraph2d_h_commands_to_insert_roomcomponents_from_projecttree.htm"
file: "tutgraph2d_h_commands_to_insert_roomcomponents_from_projecttree"
category: "tutgraph2d"
---

# Commands for inserting room components (RoomComponent) from the project tree

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Commands for inserting room components (RoomComponent) from the project tree For every device and the person, a command is required in each case, which is executed upon dragging a component from the project tree into the diagram.
    1. Extend the configuration for the commands with the last seven lines.
    
        <!-- Commands -->
    <!-- Commands to create nodes out of the project tree -->
    <command xsi:type="createNodeForInstance" src="=isInstanceOf('IT_ModularSystem.Buildingcomponents.Floor')" id="add_Floor" />
    <command xsi:type="createNodeForInstance" src="=isInstanceOf('IT_ModularSystem.Buildingcomponents.Room')" id="add_Room" />
    <command xsi:type="createNodeForInstance" src="=isInstanceOf('IT_ModularSystem.Roomcomponents.PC')" id="add_PC" />
    <command xsi:type="createNodeForInstance" src="=isInstanceOf('IT_ModularSystem.Basic.LAN_Jack')" id="add_LAN_Jack" />
    <command xsi:type="createNodeForInstance" src="=isInstanceOf('IT_ModularSystem.Roomcomponents.Telephone')" id="add_Telephone" />
    <command xsi:type="createNodeForInstance" src="=isInstanceOf('IT_ModularSystem.Roomcomponents.Printer')" id="add_Printer" />
    <command xsi:type="createNodeForInstance" src="=isInstanceOf('IT_ModularSystem.Roomcomponents.2wayLANJack')" id="add_2wayLANJack" />
    <command xsi:type="createNodeForInstance" src="=isInstanceOf('IT_ModularSystem.Roomcomponents.5waySwitch')" id="add_5waySwitch" />
    <command xsi:type="createNodeForInstance" src="=isInstanceOf('IT_ModularSystem.Roomcomponents.Worker')" id="add_Worker" />

    1. Save the diagram configuration ([Ctrl] \+ [S]).
