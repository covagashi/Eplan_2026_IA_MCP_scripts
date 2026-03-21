---
title: "Node as editable text element"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecgraph2d_k_nodes_as_editable_text_item.htm"
file: "eecgraph2d_k_nodes_as_editable_text_item"
category: "eecgraph2d"
---

# Node as editable text element

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Node as editable text element

The attributes of a component can also be represented as nodes This enables important attribute values to be displayed in diagrams, e.g. as slave nodes directly on a master node.

The following example illustrates how the name of a component can be displayed and modified with the help of a slave node.

### [Example code](javascript:void\(0\);)
    
        <node id="Funktion" super="Komponente" slaveNodes="=this">
    	<figureImage figure="com.mind8.graph2d.figure.Image"/>
    	<slaveNode id="LabelAsSlave" node="LabelAsSlave" super="Komponente"
    		valid="=isInstanceEO() and
    		isInstanceOf('Rohbau_Architektur.Ebenenkomponenten.Funktion')"
    		layout="outsideEdged" direction="SOUTH" parent="=this">
    		<figureLabel figure="com.mind8.graph2d.figure.Label">
    			<properties>
    				<property id="text">
    					<read value="=name"/>
    					<write key="name" receiver="this"/>
    				</property>
    				<property id="prefWidth">
    					<read value="100"/>
    				</property>
    				<property id="prefHeight">
    					<read value="30"/>
    				</property>
    			</properties>
    		</figureLabel>
    		<property id="showLabel">
    			<read value="true"/>
    		</property>
    		<movement rotateWithMaster="NO" rotate="NO"/>
    	</slaveNode>
    </node>

Result:
