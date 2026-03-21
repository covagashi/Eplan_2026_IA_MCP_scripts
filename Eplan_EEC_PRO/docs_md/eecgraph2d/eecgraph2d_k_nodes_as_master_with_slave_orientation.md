---
title: "Orientation of master and slave"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecgraph2d_k_nodes_as_master_with_slave_orientation.htm"
file: "eecgraph2d_k_nodes_as_master_with_slave_orientation"
category: "eecgraph2d"
---

# Orientation of master and slave

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Orientation of master and slave

The positioning of the slave node on the border of the master node may be specified in the configuration of the master node. The principle for positioning on the outside edge of the master node is called outside-edged, while positioning on the inside edge is called inside-edged (not currently supported).

A slave node is initially positioned at one of the cardinal directions relative to the master node as specified by the direction attribute of the <slaveNode> element. Which cardinal direction a slave node may be moved to manually in relation to the master node is specified by the direction attribute of the <movement> sub-element.

Sample code for aligning slave nodes to a master node:

The example of the thermodynamic model demonstrates how to align inputs and outputs as slave nodes that are always aligned in relation to the master node so as to ensure that the airflow direction is maintained.

In the configuration of the master node (id=âAbstractThermodynamicComponent"), the slaveNodes=â=rmos(âThermodynamic_Architecture.ConnectionPoint')" attribute indicates that all subordinate components of the ConnectionPoint type are to be aligned as slave nodes.

Nodes with node=âAirInputâ and nodes with nodes=âAirOutputâ are all defined as slave nodes. Their orientation in relation to the master node is specified by the direction="WEST" and direction="EAST" attribute.

### [Sample code for a master node with slave nodes as docking points](javascript:void\(0\);)
    
        <node id="AbstrakteThermodynamikKomponente"
    	super="Komponente"
    	slaveNodes="=rmos('Thermodynamik_Architektur.Anschluss')"
    	valid="=isInstanceOf('Thermodynamik_Architektur.IThermodynamikFunktion')">
    	<figureImage>
    		<configuration>
    			<editRequestHandler xsi:type="formui:formui-handler"/>
    			<editRequestHandlerInfo xsi:type="formui:formui-handler-info"
    			refId="TDD"/>
    		</configuration>
    		<properties>
    			<property id="img">
    				<read value="=type('Thermodynamik_Baukasten.
    					Diagramm_Konfiguration.Bildregister').image(this)"/>
    			</property>
    		</properties>
    	</figureImage>
    	<slaveNode node="LuftEingang" layout="outsideEdged" direction="WEST"
    		parent="=mc">
    		<movement direction="EAST SOUTH WEST NORTH" rotate="YES"/>
    	</slaveNode>
    	<slaveNode node="LuftAusgang" layout="outsideEdged"
    		direction="EAST" parent="=mc">
    		<movement direction="EAST SOUTH WEST NORTH" rotate="YES"/>
    	</slaveNode>
    </node>
    <node id="ThermodynamischerAnschluss" super="Komponente"
    	valid="=isInstanceOf('Thermodynamik_Architektur.Anschluss')">
    	<property id="prefWidth">
    		<read value="20"/>
    	</property>
    	<property id="prefHeight">
    		<read value="20"/>
    	</property>
    	<property id="boColor">
    		<read value="0,0,0"/>
    	</property>
    	<property id="boWidth">
    		<read value="0"/>
    	</property>
    </node>
    <node id="LuftEingang" super="ThermodynamischerAnschluss"
    	valid="=isInstanceOf('Thermodynamik_Baukasten.Basis.LuftEingang')">
    	<property id="img">
    		<read value="=type('Thermodynamik_Baukasten.
    		Diagramm_Konfiguration.Bildregister').image(this)"/>
    	</property>
    </node>
    <node id="LuftAusgang" super="ThermodynamischerAnschluss"
    	valid="=isInstanceOf('Thermodynamik_Baukasten.Basis.LuftAusgang')">
    	<property id="img">
    		<read value="=type('Thermodynamik_Baukasten.
    		Diagramm_Konfiguration.Bildregister').image(this)"/>
    	</property>
    </node>

Result:
