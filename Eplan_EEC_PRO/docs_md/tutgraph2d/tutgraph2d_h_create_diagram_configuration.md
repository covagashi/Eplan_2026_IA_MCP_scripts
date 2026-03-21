---
title: "Create new diagram configuration"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutgraph2d_h_create_diagram_configuration.htm"
file: "tutgraph2d_h_create_diagram_configuration"
category: "tutgraph2d"
---

# Create new diagram configuration

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Create new diagram configuration The unit Diagramconfigurations is already present in the library IT_ModularSystem. The new diagram configuration is to be created in this unit:
    1. Select the unit Diagram configurations.
    2. In the context menu, select New > Diagram definition.
    3. Input the name IT_SolutionMap.
    4. The modifications can be adopted by clicking the disk icon at the top left (or using the shortcut key [Ctrl] \+ [S]).
The new diagram configuration is then added in the unit Diagramconfigurations. In the following, it is assumed that you save your modifications by the time you open the next object (disk icon top left or using the shortcut key [Ctrl] \+ [S]), and if not, by the time you see the prompt and click Yes. The diagram configuration is edited in the Editor Configuration:
    1. Click Configuration to open the Editor.
    2. Click the Source tab to display the XML source text.
The diagram definition is filled with the following XML tags immediately after creation: Tag name | Description  
---|---  
<?xml> | The XML version used and the character coding  
</diagramEditor> | The stored schema, ID of the diagram and standard router. Encloses all the other tags of the definition  
<router> | Encloses the specific description of the router in <routerClass>  
<routerClass> | Specific description of the router that is given in <diagramEditor> (see also [Configuring connections](tutgraph2d_h_connections_configuration.htm)).  
<node> | Encloses the specific description of a node
