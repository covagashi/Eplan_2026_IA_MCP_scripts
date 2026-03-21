---
title: "Configuring the node for Floor"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutgraph2d_h_configuration_of_floor_node.htm"
file: "tutgraph2d_h_configuration_of_floor_node"
category: "tutgraph2d"
---

# Configuring the node for Floor

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Configuring the node for Floor The node for Floor should be a container for nodes of type Room and be depicted as a Polygon.
    1. Insert the following lines under the configuration of abstract_Buildingcomponent for the node Floor. Do not save after inserting, because the statement acceptedChildren="Room" would still lead to a validation error.
    
        <!-- Inherits properties of "abstract_Buildingcomponent" -->
    <node id="Floor" super="abstract_Buildingcomponent" valid="=isInstanceEO() and isInstanceOf('IT_Architecture.Levelcomponents.Floor')" acceptedChildren="Room">
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

[Explanation](javascript:void\(0\);) The ID of the node isFloor, and it is referenced in the next step. The configuration of the parent node is referenced with the attribute super="abstract_Buildingcomponent" to inherit its properties. The attribute valid="=isInstanceEO() and isInstanceOf('IT_Architecture.Levelcomponents.Floor')" determines the type that the project component must conform to, so that it can be added as a floor. The responsibility for Floor appearing as a container of Room is that of the attribute acceptedChildren="Room". The tag figurePolygon determines that Floor is added in the diagram as a polygon. All the other properties are then configured, provided this has not already been done through the parent node. The meanings of the individual properties:ID name| Meaning  
---|---  
bendpointsCount| Initial number of bendpoints for a polygon.  
bendpointsModifiable| Specifies, if the number of bendpoints can be modified.  
true = additional bendpoints possible  
true = number of bendpoints is fixed  
prefWidth| Predefined width of the graphical object  
prefHeight| Predefined height of the graphical object  
The configuration of the properties of figurePolygon is followed by the properties for the node Floor itself. The tag property id="text" configures a label that is displayed at the top left of the polygon. Floor is the node that is to be added to the diagram as an element of the uppermost level. To that end, the configuration of <diagramEditor> must be expanded with the attribute acceptedChildren="Floor".
    1. In the tag <diagramEditor>, add the attribute acceptedChildren="Floor". Do not save after inserting, because the statement acceptedChildren="Room" would still lead to a validation error.
