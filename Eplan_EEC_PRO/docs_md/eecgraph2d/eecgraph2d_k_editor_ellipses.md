---
title: "Ellipses"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecgraph2d_k_editor_ellipses.htm"
file: "eecgraph2d_k_editor_ellipses"
category: "eecgraph2d"
---

# Ellipses

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Ellipses

In the configuration file, it is now possible to define ellipses for the figure class.

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

With the definition in the example code, an instance of the safety circuit is represented in the diagram as an ellipse. The size and shape of the ellipse can be changed by dragging the bendpoints (see the following figure).
