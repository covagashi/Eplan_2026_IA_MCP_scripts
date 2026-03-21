---
title: "Configuring the superior node for the container object"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutgraph2d_h_configuration_of_supernode_for_container.htm"
file: "tutgraph2d_h_configuration_of_supernode_for_container"
category: "tutgraph2d"
---

# Configuring the superior node for the container object

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Configuring the superior node for the container object The nodes for Floor and Room should both be able to hold additional nodes. Therefore, container objects are involved. Since both these container objects are similar in many properties, a parent container node is created and the specific nodes for Floor and Room inherit its properties.
    1. Replace the configuration of the node <node id="node"> with the following lines.
    
        <!-- Nodes -->
    <!-- Nodes of building components which inherit their properties-->
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

    1. Save the diagram configuration ([Ctrl] \+ [S]).
Tip After insertion from the clipboard, if the formatting in the diagram configuration does not conform to the familiar hierarchical alignment of the tags, the alignment can be corrected with the key combination [Ctrl] + [Shift] + [F]. [Explanation](javascript:void\(0\);) The ID of the node is now abstract_Buildingcomponent, which is later referenced from the node for Floor and Room. <figureContainer> is used to configure a container object, which is able to accept and house other objects. All the common properties are listed under <properties>. Every property is opened with the <property id="PROPERTY"> tag , there follows a <read value="VALUE"> tag and a closing tag </property>. The meanings of the individual properties:ID name| Meaning  
---|---  
resizeable| Specifies, if the size of the graphical object can be modified.  
showScrollBars| Defines whether scrollbars are displayed for the graphical object  
showLabel| Specifies the visibility of the label  
boLineStyle| Line style  
1 = solid line (default)  
2 = dashed line  
3 = dotted line  
4 = dash-dot line  
5 = dash-dot-dot line  
boWidth| Border width in pixels  
boColor| Border color as RGB value  
selectedBoColor| Border color as RGB value, if the component is marked  
fColor| Font color as RGB value  
selectedFColor| Font color as RGB value, if the component is marked  
bColor| Background color as RGB value  
transparency| Transparency  
0 = opaque  
100 = transparent  
tooltip| Tip for the element when the mouse cursor is placed on it. Either a fixed text or a formula that returns a string.
