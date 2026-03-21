---
title: "Node as ellipse"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecgraph2d_k_nodes_as_ellipse.htm"
file: "eecgraph2d_k_nodes_as_ellipse"
category: "eecgraph2d"
---

# Node as ellipse

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Node as ellipse

In order to depict a node as an ellipse, the element <figureEllipse> must be set as a sub-element of <node>.

In addition to the basic properties for nodes, the width and height of the ellipse may be set using the following specific properties: <property id="prefWidth"> and <property id="prefHeight">.

### [Example code](javascript:void\(0\);)
    
        <node id="Schutzkreis"
    	super="Komponente"
    	valid="=isInstanceEO() and
    	isInstanceOf('Rohbau_Architektur.Ebenenkomponenten.Schutzkreis')"
    	acceptedChildren="Funktion LabelAsSlave">
    	<figureEllipse figure="com.mind8.graph2d.figure.container.Ellipse">
    		<properties>
    			<property id="showLabel">
    				<read value="true"/>
    			</property>
    			<property id="boColor">
    				<read value="62,12,144"/>
    			</property>
    			<property id="transparency">
    				<read value="80"/>
    			</property>
    			<property id="bColor">
    				<read value="255,255,255"/>
    			</property>
    			<property id="boWidth">
    				<read value="4"/>
    			</property>
    			<property id="prefWidth">
    				<read value="250"/>
    			</property>
    			<property id="prefHeight">
    				<read value="100"/>
    			</property>
    		</properties>
    	</figureEllipse>
    	<property id="text">
    		<read value="=$Bezeichnung"/>
    		<write key="value" receiver="=getParameter('Bezeichnung')"/>
    	</property>
    </node>

Result:

With the definition in the example code, an instance of the safety circuit is represented in the diagram as an ellipse. The size and shape of the ellipse can be changed by dragging the handles. If the [Shift] key is held down while a corner handle is dragged, the size is modified without changing the original aspect ratio. The [Ctrl] \+ [Shift] key combination changes the size of the node from the midpoint of the node (coaxial).
