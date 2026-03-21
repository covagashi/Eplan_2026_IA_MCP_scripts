---
title: "Commands for inserting Floor and Room from the project tree"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutgraph2d_h_commands_to_isnert_floor_and_room_from_projecttree.htm"
file: "tutgraph2d_h_commands_to_isnert_floor_and_room_from_projecttree"
category: "tutgraph2d"
---

# Commands for inserting Floor and Room from the project tree

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Commands for inserting Floor and Room from the project tree The project already contains all the components that are to be inserted in the diagram. For every node that represents a project component, a command is required, which is executed upon dragging a component from the project tree into the diagram.
    1. Under the configuration of the node for Room, add the following lines for the commands.
    
        <!-- Commands -->
    <!-- Commands to create nodes out of the project tree -->
    <command xsi:type="createNodeForInstance" src="=isInstanceOf('IT_ModularSystem.Buildingcomponents.Floor')" id="add_Floor" />
    <command xsi:type="createNodeForInstance" src="=isInstanceOf('IT_ModularSystem.Buildingcomponents.Room')" id="add_Room" />

    1. Save the diagram configuration ([Ctrl] \+ [S]).
[Explanation](javascript:void\(0\);) The command is determined with the xsi-type; here, the value createNodeForInstance is used, since an instance is added in the diagram as a node. As a type of the instances, the attribute src="=isInstanceOf('IT_ModularSystem.Buildingcomponents.Floor')" is used to determine the instance of a floor and src="=isInstanceOf('IT_ModularSystem.Buildingcomponents.Room')", to determine the instance of a room. Since all the configuration elements need an ID, our first commands are assigned the IDs add_Floor and add_Room. [This is what the configuration looks like up to now](javascript:void\(0\);)
    
        <?xml version="1.0" encoding="UTF-8"?>
    <diagramEditor xmlns="http://www.mind8.com/Diagram"
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="diagram"
    	title="IT_SolutionMap" packageable="=isInstanceOf('IT_ModularSystem.Buildingcomponents.Building')"
    	router="router" version="1" acceptedChildren="Floor">
    <router id="router">
    	<routerClass xsi:type="baseRouters"
    	class="com.mind8.graph2d.router.ShortestPath" />
    </router>
    <!-- Nodes -->
    <!-- Nodes of building components which inherit their properties -->
    <node id="abstract_Buildingcomponent">
    	<figureContainer figure="com.mind8.graph2d.figure.Container">
    		<properties>
    			<property id="resizable">
    				<read value="true" />
    			</property>
    			<property id="showScrollBars">
    				<read value="false" />
    			</property>
    			<property id="showLabel">
    				<read value="true" />
    			</property>
    			<property id="boLineStyle">
    				<read value="4" />
    			</property>
    			<property id="boWidth">
    				<read value="4" />
    			</property>
    			<property id="boColor">
    				<read value="62,12,144" />
    			</property>
    			<property id="selectedBoColor">
    				<read value="255,0,10" />
    			</property>
    			<property id="fColor">
    				<read value="50,50,50" />
    			</property>
    			<property id="selectedFColor">
    				<read value="10,36,106" />
    			</property>
    			<property id="bColor">
    				<read value="255,255,255" />
    			</property>
    			<property id="transparency">
    				<read value="80" />
    			</property>
    			<property id="tooltip">
    				<read value="=$Tooltip" />
    			</property>
    		</properties>
    	</figureContainer>
    </node>
    <!-- Inherits properties of "abstract_Buildingcomponent" -->
    <node id="Floor" super="abstract_Buildingcomponent"
    	valid="=isInstanceEO() and isInstanceOf('IT_Architecture.Levelcomponents.Floor')" acceptedChildren="Room">
    	<figurePolygon figure="com.mind8.graph2d.figure.container.Polygon">
    		<properties>
    			<property id="prefWidth">
    				<read value="2000" />
    			</property>
    			<property id="prefHeight">
    				<read value="2000" />
    			</property>
    			<property id="bendpointsCount">
    				<read value="4" />
    			</property>
    			<property id="bendpointsModifiable">
    				<read value="true" />
    			</property>
    		</properties>
    	</figurePolygon>
    	<property id="text">
    		<read value="=$Tooltip" />
    		<write key="value" receiver="=parameter('Number')" />
    	</property>
    </node>
    <!-- Inherits properties of "abstract_Buildingcomponent" -->
    <node id="Room" super="abstract_Buildingcomponent"
    	valid="=isInstanceEO() and isInstanceOf('IT_Architecture.Levelcomponents.Room')">
    	<figurePolygon figure="com.mind8.graph2d.figure.container.Polygon">
    		<properties>
    			<property id="boLineStyle">
    				<read value="1" />
    			</property>
    			<property id="prefWidth">
    				<read value="400" />
    			</property>
    			<property id="prefHeight">
    				<read value="400" />
    			</property>
    			<property id="bendpointsCount">
    				<read value="4" />
    			</property>
    			<property id="bendpointsModifiable">
    				<read value="true" />
    			</property>
    		</properties>
    	</figurePolygon>
    	<property id="text">
    		<read value="=$Tooltip" />
    	</property>
    </node>
    <!-- Commands -->
    <!-- Commands to create nodes out of the project tree -->
    <command xsi:type="createNodeForInstance" src="=isInstanceOf('IT_ModularSystem.Buildingcomponents.Floor')" id="add_Floor" />
    <command xsi:type="createNodeForInstance" src="=isInstanceOf('IT_ModularSystem.Buildingcomponents.Room')" id="add_Room" />
    </diagramEditor>
