---
title: "Node as polygon"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecgraph2d_k_nodes_as_polygon.htm"
file: "eecgraph2d_k_nodes_as_polygon"
category: "eecgraph2d"
---

# Node as polygon

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Node as polygon

In general, all that is needed to represent a polygon is the number of corner points (bendpointsCount). The number of bendpoints determines the basic form of the polygon, from a triangle to a polygon with any number of sides.

### [Example code for a rectangle](javascript:void\(0\);)
    
        <node id="Schutzkreis" valid="=isInstanceEO() and
    	isInstanceOf('Rohbau_Architektur.Ebenenkomponenten.Schutzkreis')">
    	<figurePolygon figure="com.mind8.graph2d.figure.container.Polygon">
    		<properties>
    			<property id="bendpointsCount">
    				<read value="4"/>
    			</property>
    		</properties>
    	</figurePolygon>
    </node>

Result:

The number of bendpoints can be edited in the diagram, if the property bendpointsModifiable is inserted and set to true.
