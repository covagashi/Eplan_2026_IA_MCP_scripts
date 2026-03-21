---
title: "Commands for moving the nodes"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutgraph2d_h_commands_to_move_nodes.htm"
file: "tutgraph2d_h_commands_to_move_nodes"
category: "tutgraph2d"
---

# Commands for moving the nodes

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Commands for moving the nodes To end the Tutorial for the Graph2D diagram, commands are to be added to be able to move the rooms between floors, and devices and persons between the rooms.
    1. Extend the configuration for the commands with the following lines.
    
        <!-- Commands to move nodes between rooms and rooms between floors -->
    <command xsi:type="changeInstanceParent" src="=isInstanceOf('IT_ModularSystem.Buildingcomponents.Room')" id="move_Room" />
    <command xsi:type="changeInstanceParent" src="=isInstanceOf('IT_ModularSystem.Roomcomponents.PC')" id="move_PC" />
    <command xsi:type="changeInstanceParent" src="=isInstanceOf('IT_ModularSystem.Roomcomponents.Telephone')" id="move_Telephone" />
    <command xsi:type="changeInstanceParent" src="=isInstanceOf('IT_ModularSystem.Roomcomponents.5waySwitch')" id="move_5waySwitch" />
    <command xsi:type="changeInstanceParent" src="=isInstanceOf('IT_ModularSystem.Roomcomponents.Printer')" id="move_Printer" />
    <command xsi:type="changeInstanceParent" src="=isInstanceOf('IT_ModularSystem.Roomcomponents.Worker')" id="move_Worker" />
    <command xsi:type="changeInstanceParent" src="=isInstanceOf('IT_ModularSystem.Roomcomponents.2wayLANJack')" id="move_2way_LANJack" />

    1. Save the diagram configuration ([Ctrl] \+ [S]).
[Explanation](javascript:void\(0\);) The command is determined with the xsi-type; here, the value changeInstanceParent is used, since for the relevant node, the parent project component is changed. The attribute src="=isInstanceOf(' IT_ModularSystem.Buildingcomponents.Room')" determines the type of the node whose parent project component may change. The ID is not referenced here. [This is what the configuration now looks like](javascript:void\(0\);)
    
        <?xml version="1.0" encoding="UTF-8"?>
    <diagramEditor xmlns="http://www.mind8.com/Diagram"
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="diagram"
    	xmlns:formui="http://www.mind8.com/Diagram/Formui" title="IT_SolutionMap"
    	packageable="=isInstanceOf('IT_ModularSystem.Buildingcomponents.Building')"
    	router="ShortestPath" version="1" acceptedChildren="Floor">
    	<!-- Router -->
    	<!-- Router for connecting worker and device -->
    	<router id="Bendpoint" class="com.mind8.graph2d.router.Bendpoint" />
    	<!-- Router for connecting slave and device -->
    	<router id="ShortestPath" class="com.mind8.graph2d.router.ShortestPath" />
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
    	<node id="Floor" super="abstract_Buildingcomponent" valid="=isInstanceEO() and isInstanceOf('IT_Architecture.Levelcomponents.Floor')" acceptedChildren="Room">
    		<figurePolygon figure="com.mind8.graph2d.figure.container.Polygon">
    			<configuration>
    				<editRequestHandler xsi:type="formui:formui-handler" />
    				<editRequestHandlerInfo xsi:type="formui:formui-handler-info"refId="GSD" showMenu="true" />
    			</configuration>
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
    	<node id="Room" super="abstract_Buildingcomponent"valid="=isInstanceEO() and isInstanceOf('IT_Architecture.Levelcomponents.Room')"acceptedChildren="abstract_Roomcomponent">
    		<figurePolygon figure="com.mind8.graph2d.figure.container.Polygon">
    			<configuration>
    				<editRequestHandler xsi:type="formui:formui-handler" />
    				<editRequestHandlerInfo xsi:type="formui:formui-handler-info"refId="RD" />
    			</configuration>
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
    	<!-- Node of room components -->
    	<!-- Room component with common properties which is referenced multiple -->
    	<node id="Component">
    		<figureImage figure="com.mind8.graph2d.figure.Image">
    			<configuration>
    				<editRequestHandler xsi:type="formui:formui-handler" />
    				<editRequestHandlerInfo xsi:type="formui:formui-handler-info"refId="Data" resizable="true" movable="true" showMenu="true" />
    			</configuration>
    			<properties>
    				<property id="tooltip">
    					<read value="=$Tooltip" />
    				</property>
    			</properties>
    		</figureImage>
    	</node>
    	<!-- Slave -->
    	<node id="LAN_Jack" valid="=isInstanceOf('IT_ModularSystem.Basic.LAN_Jack')">
    		<figureLabel figure="com.mind8.graph2d.figure.Label">
    			<properties>
    				<property id="text">
    					<read value="=$Name" />
    				</property>
    				<property id="showIcon">
    					<read value="false" />
    				</property>
    			</properties>
    		</figureLabel>
    	</node>
    	<!-- Relation of Master (PC/Printer/Telephone/5waySwitch/2wayLANJack) to Slave (LAN_Jack) and Label -->
    	<node id="abstract_Roomcomponent" super="Component"slaveNodes="=rmos('IT_ModularSystem.Basic.LAN_Jack').append(this)">
    		<slaveNode id="SN_LAN_Jack" node="LAN_Jack" layout="outsideEdged"direction="=$Direction" parent="=mc">
    			<movement direction="WEST SOUTH EAST NORTH" rotate="NO" />
    		</slaveNode>
    		<slaveNode id="SNLabel"valid="=isInstanceEO() and isInstanceOf('IT_Architecture.Levelcomponents.RoomComponent')"layout="outsideEdged" direction="NORTH" parent="=this">
    			<figureLabel figure="com.mind8.graph2d.figure.Label">
    				<properties>
    					<property id="text">
    						<read value="=$Tooltip" />
    					</property>
    					<property id="prefWidth">
    						<read value="100" />
    					</property>
    					<property id="prefHeight">
    						<read value="30" />
    					</property>
    					<property id="showIcon">
    						<read value="false" />
    					</property>
    				</properties>
    			</figureLabel>
    			<property id="showLabel">
    				<read value="true" />
    			</property>
    			<movement rotateWithMaster="NO" rotate="NO" />
    		</slaveNode>
    	</node>
    	<!-- Master -->
    	<node id="Master" super="abstract_Roomcomponent" valid="=isInstanceOf('IT_Architecture.Levelcomponents.RoomComponent')">
    		<property id="img">
    			<read value="=type('IT_ModularSystem.Images.Imageregister').image(this.type)" />
    		</property>
    	</node>
    	<!-- Connections -->
    	<!-- Relation of Worker to Device -->
    		<reference id="Worker_Reference" type="connectable" src="=isInstanceEO() and isInstanceOf('IT_ModularSystem.Basic.SinglewayComponent')" target="=isInstanceEO() and isInstanceOf('IT_ModularSystem.Basic.SinglewayComponent')">
    			<forward multiplicity="1" connector="=getParameter('WorkerConnection')" />
    			<backward multiplicity="*" connector="=getParameter('WorkerConnection')" />
    		</reference>
    	<!-- Relation of Slave to Slave -->
    	<reference id="LAN_Reference" type="connectable" src="=isInstanceEO() and isInstanceOf('IT_ModularSystem.Basic.LAN_Jack')" target="=isInstanceEO() and isInstanceOf('IT_ModularSystem.Basic.LAN_Jack')">
    		<forward multiplicity="1" connector="=getParameter('Connection')" />
    		<backward multiplicity="1" connector="=getParameter('Connection')" />
    	</reference>
    	<!-- Connection of Worker to Device -->
    	<connection id="Worker_Path" reference="Worker_Reference" router="Bendpoint" width="2" style="1" color="0,255,0" sourceDeco="empty" targetDeco="empty" tooltip="=if not src.$Name.isNull then src.$Name else if not src.$Number.isNull then src.$Number else 'Enter data' endif endif + ' | ' + if not (target.$Name.isNull) then target.$Name else if not (target.$Number.isNull) then target.$Number else 'Enter data' endif endif" />
    	<!-- Connection of Slave to Slave -->
    	<connection id="LAN_Path" reference="LAN_Reference" width="2" style="1" color="255,0,0" sourceDeco="empty" targetDeco="empty" tooltip="=src.getName() + ' of ' + if not src.mc.$Name.isNull then src.mc.$Name else if not src.mc.$Number.isNull then src.mc.$Number else 'Enter data' endif endif + ' | ' + target.getName() + ' of ' + if not target.mc.$Name.isNull then target.mc.$Name else if not target.mc.$Number.isNull then target.mc.$Number else 'Enter data' endif endif" />
    	<!-- Palette items -->
    	<!-- Group "Building" -->
    	<paletteEntry id="Floorplanning" group="Building" text="Floor" smallIcon="=type('IT_ModularSystem.Images.Floor').getImage" largeIcon="=type('IT_ModularSystem.Images.Floor').getImage">
    		<eoCreation command="create_Floor" />
    	</paletteEntry>
    	<paletteEntry id="Roomplanning" group="Building" text="Room"smallIcon="=type('IT_ModularSystem.Images.Room').getImage" largeIcon="=type('IT_ModularSystem.Images.Room').getImage">
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
    	<!-- Commands to create nodes out of the palette -->
    	<command xsi:type="instantiateAndCreateNode" src="=isClassEO() and isAssignableTo('IT_ModularSystem.Buildingcomponents.Floor')" eoClassPath="IT_ModularSystem.Buildingcomponents.Floor" id="create_Floor" />
    	<command xsi:type="instantiateAndCreateNode" src="=isClassEO() and isAssignableTo('IT_ModularSystem.Buildingcomponents.Room')" eoClassPath="IT_ModularSystem.Buildingcomponents.Room" id="create_Room" />
    	<command xsi:type="instantiateAndCreateNode" src="=isClassEO() and isAssignableTo('IT_ModularSystem.Basic.LAN_Jack')" eoClassPath="IT_ModularSystem.Basic.LAN_Jack" id="create_LAN_Jack" />
    	<command xsi:type="instantiateAndCreateNode" src="=isClassEO() and isAssignableTo('IT_ModularSystem.Roomcomponents.2wayLANJack')" eoClassPath="IT_ModularSystem.Roomcomponents.2wayLANJack" id="create_2wayLANJack" />
    	<command xsi:type="instantiateAndCreateNode" src="=isClassEO() and isAssignableTo('IT_ModularSystem.Roomcomponents.PC')" eoClassPath="IT_ModularSystem.Roomcomponents.PC" id="create_PC" />
    	<command xsi:type="instantiateAndCreateNode" src="=isClassEO() and isAssignableTo('IT_ModularSystem.Roomcomponents.Telephone')" eoClassPath="IT_ModularSystem.Roomcomponents.Telephone" id="create_Telephone" />
    	<command xsi:type="instantiateAndCreateNode" src="=isClassEO() and isAssignableTo('IT_ModularSystem.Roomcomponents.Printer')" eoClassPath="IT_ModularSystem.Roomcomponents.Printer" id="create_Printer" />
    	<command xsi:type="instantiateAndCreateNode" src="=isClassEO() and isAssignableTo('IT_ModularSystem.Roomcomponents.5waySwitch')" eoClassPath="IT_ModularSystem.Roomcomponents.5waySwitch" id="create_5waySwitch" />
    	<command xsi:type="instantiateAndCreateNode" src="=isClassEO() and isAssignableTo('IT_ModularSystem.Roomcomponents.Worker')" eoClassPath="IT_ModularSystem.Roomcomponents.Worker" id="create_Worker" />
    	<!-- Commands to move nodes between rooms and rooms between floors -->
    	<command xsi:type="changeInstanceParent" src="=isInstanceOf('IT_ModularSystem.Buildingcomponents.Room')" id="move_Room" />
    	<command xsi:type="changeInstanceParent" src="=isInstanceOf('IT_ModularSystem.Roomcomponents.PC')" id="move_PC" />
    	<command xsi:type="changeInstanceParent" src="=isInstanceOf('IT_ModularSystem.Roomcomponents.Telephone')" id="move_Telephone" />
    	<command xsi:type="changeInstanceParent" src="=isInstanceOf('IT_ModularSystem.Roomcomponents.5waySwitch')" id="move_5waySwitch" />
    	<command xsi:type="changeInstanceParent" src="=isInstanceOf('IT_ModularSystem.Roomcomponents.Printer')" id="move_Printer" />
    	<command xsi:type="changeInstanceParent" src="=isInstanceOf('IT_ModularSystem.Roomcomponents.Worker')" id="move_Worker" />
    	<command xsi:type="changeInstanceParent" src="=isInstanceOf('IT_ModularSystem.Roomcomponents.2wayLANJack')" id="move_2way_LANJack" />
    </diagramEditor>
