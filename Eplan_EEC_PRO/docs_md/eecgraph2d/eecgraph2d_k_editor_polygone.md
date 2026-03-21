---
title: "Polygons"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecgraph2d_k_editor_polygone.htm"
file: "eecgraph2d_k_editor_polygone"
category: "eecgraph2d"
---

# Polygons

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Polygons

In the configuration file, it is possible to define polygons for the figure class that are specified in terms of the number of node points (bendpointsCount attribute). Furthermore, the bendpointsModifiable attribute can be used to specify whether the project engineer can insert additional bendpoints.

### [Example code for the definition of the safety circuit as a hexagon](javascript:void\(0\);)
    
        <node id="Schutzkreis"
    	super="Komponente"
    	valid="=isInstanceEO() and
    	isInstanceOf('Rohbau_Architektur.Ebenenkomponenten.Schutzkreis')"
    	acceptedChildren="Funktion LabelAsSlave">
    	<figurePolygon figure="com.mind8.graph2d.figure.container.Polygon">
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
    				<read value="250"/>
    			</property>
    			<property id="bendpointsCount">
    				<read value="6"/>
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
    /node>

The size and shape of the polygon can be changed by dragging the corners (see the following figure).

To interactively change the number of bendpoints and hence the shape of a polygon, select the polygon and then press [P]. Between each pair of node points at the corners (bendpoints), a small bendpoint appears in the middle of the straight line.

Inserting a bendpoint:

Pressing [P] and dragging a bendpoint from the middle of a straight line causes a new bendpoint to be created.

Deleting a bendpoint:

Pressing [P] and dragging a bendpoint from one corner onto another corner causes two straight lines to become one straight line and the overlapping bendpoints to become a single bendpoint.
