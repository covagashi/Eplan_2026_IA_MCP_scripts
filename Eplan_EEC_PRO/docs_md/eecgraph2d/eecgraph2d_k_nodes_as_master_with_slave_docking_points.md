---
title: "Slave nodes as docking points for master nodes"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecgraph2d_k_nodes_as_master_with_slave_docking_points.htm"
file: "eecgraph2d_k_nodes_as_master_with_slave_docking_points"
category: "eecgraph2d"
---

# Slave nodes as docking points for master nodes

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Slave nodes as docking points for master nodes

Master nodes can be docked together with the help of slave nodes, provided the slave nodes are configured as docking points. This requires that the slave node be designated a docking point via the snapPoint="true" attribute, that it be aligned on the outer contour of the master via the layout="onEdge" attribute, and that it be positioned on the outer contour of the master via the position attribute. The mechatronic component must have a parameter for storing the object reference.

### [Sample code for a master node with slave nodes as docking points](javascript:void\(0\);)
    
        <node id="abstractBelt" slaveNodes="=mos">
    	<figureBase>
    		<properties>
    			<property id="resizable">
    				<read value="true" />
    			</property>
    		</properties>
    	</figureBase>
    	<slaveNode id="startSlave" node="snapPointStart"
    	parent="=mc" layout="onEdge" direction="=$Direction"
    	creation="byMaster" snapPoint="true" position="50%" />
    	<slaveNode id="endSlave" node="snapPointEnd"
    	parent="=mc" layout="onEdge" direction="=$Direction"
    	creation="byMaster" snapPoint="true" position="50%" />
    	<slaveNode id="stopperSlave" node="stopperApp"
    	parent="=mc" layout="outsideEdged" creation="byMaster"/>
    </node>
    <reference id="ReihenfolgeReferenz" type="connectable"
    	src="=isInstanceEO() and
    	isInstanceOf('SnapPoint.Mechatronic.ConnectionPoints.BeltConnectionPointStart')"
    	target="=isInstanceEO() and
    	isInstanceOf('SnapPoint.Mechatronic.ConnectionPoints.BeltConnectionPointEnd')">
    	<forward multiplicity="1" connector="=getParameter('Reference')" />
    	<backward multiplicity="1" connector="=getParameter('Reference')" />
    </reference>

Result:

To begin with, the nodes to be connected are stored in the diagram editor. Then a node is moved over the nodes to be connected until red cross-hairs appear (see the below screenshot). The object reference for this connection is stored in the âreferenceâ parameter.

To delete this connection, hold down the [Alt] key and move the node away from the connected nodes.
