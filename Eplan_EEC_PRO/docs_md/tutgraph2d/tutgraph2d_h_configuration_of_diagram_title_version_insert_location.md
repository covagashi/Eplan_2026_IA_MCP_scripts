---
title: "Determining the title, version and insertion location for the diagram"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutgraph2d_h_configuration_of_diagram_title_version_insert_location.htm"
file: "tutgraph2d_h_configuration_of_diagram_title_version_insert_location"
category: "tutgraph2d"
---

# Determining the title, version and insertion location for the diagram

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Determining the title, version and insertion location for the diagram The attributes in the tag <diagramEditor> are used to define what the name of a newly created diagram in the project will be (attribute title), at what location within a project a new diagram can be inserted (attribute insertion location) and the default version that is assigned to the newly inserted diagram (attribute Version). Note The version can be any string of characters; its value is not incremented automatically when changes are made to the diagram configuration. The title for a freshly added diagram should be IT_SolutionMap:
    1. For the title attribute input the value IT_SolutionMap.
The first node to be inserted in the diagram should be a floor. Since the corresponding component is located under the component Building, it should be possible to insert the diagram below Building and above Floor (see [Task: Creating a configuration diagram for office infrastructure](tutgraph2d_h_task_configuration_diagram_for_office_structure.htm)) Determine insertion location:
    1. For the attribute packageable, input the value =isInstanceOf('IT_ModularSystem.Buildingcomponents.Building').
The version is given the value 1:
    1. For the attribute version, input the value 1.
    2. Save the diagram configuration ([Ctrl] \+ [S]).
[This is what the configuration looks like up to now](javascript:void\(0\);)
    
        <?xml version="1.0" encoding="UTF-8"?>
    <diagramEditor
    	xmlns="http://www.mind8.com/Diagram"
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    	id="diagram"
    	title="IT_SolutionMap"
    	packageable="=isInstanceOf('IT_ModularSystem.Buildingcomponents.Building')"
    	router="router"
    	version="1">
    <router id="router">
    	<routerClass xsi:type="baseRouters" class="com.mind8.graph2d.router.ShortestPath" />
    </router>
    <node id="node">
    </node>
    </diagramEditor>
