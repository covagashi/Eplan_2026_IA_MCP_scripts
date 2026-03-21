---
title: "Configuring the nodes for room components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutgraph2d_h_configuration_of_nodes_for_roomcomponents.htm"
file: "tutgraph2d_h_configuration_of_nodes_for_roomcomponents"
category: "tutgraph2d"
---

# Configuring the nodes for room components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Configuring the nodes for room components Several nodes must be configured for the room components. To start with, once again, a parent node is configured, which contains, as a common property for all the room components to be displayed with it, the configuration for a tooltip. The tooltip is displayed when the mouse pointer is placed over a room component.
    1. Below the configuration of the node Room, insert the following lines for the parent node of the image object.
    
        <!-- Node of room components -->
    <!-- Room component with common properties which is referenced multiple -->
    <node id="Component">
    	<figureImage figure="com.mind8.graph2d.figure.Image">
    		<properties>
    				<property id="tooltip">
    					<read value="=$Tooltip" />
    				</property>
    			</properties>
    		</figureImage>
    	</node>

    1. Under this configuration, insert the following lines.
    
        <!-- Master -->
    <node id="Master" super="Component" valid="=isInstanceOf('IT_Architecture.Levelcomponents.RoomComponent')">
    <property id="img">
    		<read value="=type('IT_ModularSystem.Images.Imageregister').image(this.type)" />
    	</property>
    	</node>

In order that such a node can be inserted in a Room, the configuration for Room must be expanded with the attribute acceptedChildren="Master".
    1. In the tag <node id="Room"> add the attribute acceptedChildren="Master".
    2. Save the diagram configuration ([Ctrl] \+ [S]).
[Explanation:](javascript:void\(0\);) The ID of the parent node is now Component, which the node Master references. The node with the ID Master is in turn referenced as a permitted sub-node of Room. With <figureImage>, a node is configured, which is to be displayed as an image. It has the property <property id="tooltip"> to display a tooltip. The tag <read value="=$Tooltip" /> is used to access the parameter Tooltip of the project component, to display its value as a tooltip. For the node Master, the attribute valid="=isInstanceOf('IT_Architecture.Levelcomponents.RoomComponents') is used to determine the type that a project component must conform to, so that it can be displayed as an image. The property <property id="img"> <read value="=type('IT_ModularSystem.Images.Imageregister').image(this.type)"> describes which image is to be accessed, i.e. an image from the Imageregister, which conforms to the type of the project component to be inserted. The meanings of the individual properties:ID name| Meaning  
---|---  
img| Formula to the graphical object of the project component  
tooltip| Tip for the element when the mouse cursor is placed on it. Either a fixed text or a formula that returns a string.
