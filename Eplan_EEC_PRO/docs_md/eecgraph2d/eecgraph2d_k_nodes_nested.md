---
title: "Nested nodes"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecgraph2d_k_nodes_nested.htm"
file: "eecgraph2d_k_nodes_nested"
category: "eecgraph2d"
---

# Nested nodes

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Nested nodes

Nodes are also arranged in nested order within a diagram in accordance with the hierarchy of the mechatronic structure. For example, in the planning diagram for the âBodyshell workâ model, roller conveyors and robots can only be positioned within a safety circuit. To this end, a list of all subordinate nodes is defined in the configuration of the superordinate node by means of the acceptedChildren attribute.

Sample code for a nested structure:

This example illustrates the nesting of a safety circuit and robots in the planning diagram for the âBodyshell workâ demo model. The relevant parts of the code are in boldface. Every node that corresponds to the configuration of Function and LabelAsSlave is permitted as a subordinate node of SafetyCircuit. In this example, the node for robots is configured as a Function and is therefore a permitted sub-element of SafetyCircuit.

### [Example code](javascript:void\(0\);)
    
        <node id="Schutzkreis" super="Komponente" valid="=isInstanceEO() and
    	isInstanceOf('Rohbau_Architektur.Ebenenkomponenten.Schutzkreis')"
    	acceptedChildren="Funktion LabelAsSlave">
    	<figurePolygon figure="com.mind8.graph2d.figure.container.Polygon">
    		<properties>
    			<property id="bColor">
    				<read value="255,255,255"/>
                </property>
    			<property id="boLineStyle">
    				<read value="1"/>
                </property>
                <property id="showLabel">
    				<read value="true"/>
                </property>
                <property id="boColor">
    				<read value="62,12,144"/>
                </property>
                <property id="boWidth">
    				<read value="4"/>
                </property>
                <property id="bendpointsCount">
    				<read value="4"/>
                </property>
                <property id="bendpointsModifiable">
    				<read value="true"/>
    			</property>
    		</properties>
    	</figurePolygon>
    	<property id="text">
    		<read value="=$Bezeichnung"/>
    		<write key="value" receiver="=getParameter('Bezeichnung')"/>
    	</property>
    </node>
    <node id="Roboter"
    	super="Funktion"
    	valid="=isInstanceOf('Rohbau_Baukasten.
    	Mechatronik.Roboter')">
    	<property id="img">
    		<read value="=type('Rohbau_Baukasten.Diagramm_Konfiguration.
    		Planungs_Diagramm.Register').image(this)"/>
    	</property>
    </node>

Result:
