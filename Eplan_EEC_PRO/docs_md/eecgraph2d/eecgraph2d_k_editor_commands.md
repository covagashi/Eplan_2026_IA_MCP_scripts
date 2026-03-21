---
title: "Inserting and moving project components via commands"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecgraph2d_k_editor_commands.htm"
file: "eecgraph2d_k_editor_commands"
category: "eecgraph2d"
---

# Inserting and moving project components via commands

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Inserting and moving project components via commands

In the diagram configuration, the <command> tag can be used in connection with the following name-space expansions to define which components from the project tree may be inserted via drag and drop, which components from the palette may be instantiated, and which components may be moved from one superordinate component to another:

     * Command for inserting from the project:
    
        <command xsi:type="createNodeForInstance">

     * Command for inserting from the modular system:
    
        <command xsi:type="createNodeForClass">

     * Command for instantiating from the palette:
    
        <command xsi:type="instantiateAndCreateNode">

     * Command for moving a component from one superordinate component to another:
    
        <command xsi:type="changeInstanceParent">

     * which graphical objects may be dragged from one diagram into another (request="Change_parent" attribute).

### [Example code for the definition of an element that may be dragged into the diagram, creating a new instance in the process](javascript:void\(0\);)
    
        <command source="=isClassEO() and (absoluteName='Rohbau_Baukasten.Mechatronik.Schutzkreis')"
    	target="Diagram"
    	request="Drop_and_instantiate" />

### [Example code for the definition of an element that may be dragged into the diagram](javascript:void\(0\);)
    
        <command source="=isInstanceOf('Rohbau_Architektur.Ebenenkomponenten.Schutzkreis')"
    	target="Diagram"
    	request="Drop_at_target" />

### [Example code for the definition of an element that may be dragged from one diagram into another](javascript:void\(0\);)
    
        <command source="=isInstanceOf('Rohbau_Baukasten.Mechatronik.Roboter')"
    	target="=isInstanceOf('Rohbau_Architektur.Ebenenkomponenten.Schutzkreis')"
    	request="Change_parent" />
