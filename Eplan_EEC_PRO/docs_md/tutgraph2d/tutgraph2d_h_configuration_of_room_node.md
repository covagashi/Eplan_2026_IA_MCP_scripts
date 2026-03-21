---
title: "Configuring the node for Room"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutgraph2d_h_configuration_of_room_node.htm"
file: "tutgraph2d_h_configuration_of_room_node"
category: "tutgraph2d"
---

# Configuring the node for Room

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Configuring the node for Room The node for Room should be a container for nodes of type Roomcomponent and should likewise be depicted as a polygon. To distinguish it from the node Floor, which is drawn with a dash-dot line, the room should be depicted with a solid line (see property-id="boLineStyle").
    1. Below the configuration of the node Floor, insert the following lines for the node Room.
    
        <!-- Inherits properties of "abstract_Buildingcomponent" -->
    <node id="Room" super="abstract_Buildingcomponent" valid="=isInstanceEO() and isInstanceOf('IT_Architecture.Levelcomponents.Room')">
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

    1. Save the diagram configuration ([Ctrl] \+ [S]).
[Explanation](javascript:void\(0\);) The ID of the node is Room; it is referenced by the node for Floor in the attribute acceptedChildren. The configuration of the parent node is referenced with the attribute super="abstract_Buildingcomponent" to inherit its properties. The valid="=isInstanceEO() and isInstanceOf(âIT_Architecture.Levelcomponents.Room')" attribute determines whether the entity in question is an existing project component (isInstanceEO) and specifies what type the project component must conform to in order to be added as a Room (isInstanceOf). The room is also a container, but the attribute acceptedChildren is only added after the subordinate nodes have also been configured. Otherwise, there would be an error message because there are no corresponding node configurations available for the references. The tag figurePolygon determines that Room is also added in the diagram as a polygon. All the other properties are then configured, provided this has not already been done through the parent node. The configuration of the properties of figurePolygon is followed by properties for the node Room itself. The tag property id="text" configures a label that is displayed at the top left of the polygon.
