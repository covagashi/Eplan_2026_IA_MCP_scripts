---
title: "Inserting nodes automatically"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecgraph2d_k_insert_nodes_automatically.htm"
file: "eecgraph2d_k_insert_nodes_automatically"
category: "eecgraph2d"
---

# Inserting nodes automatically

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Inserting nodes automatically

Slave nodes can be automatically inserted into the diagram in two ways.

    1. Master nodes and corresponding slave nodes are instantiated in the project structure. Next, the master nodes are manually inserted into the diagram, causing the corresponding slave nodes to be automatically inserted as well.
    2. Slave nodes whose master nodes have already been inserted into the diagram are then instantiated in the project structure. When the diagram is opened, they are specified in accordance with the configuration and then placed at the appropriate master node.

In order to distinguish automatically inserted slave nodes after the diagram has been opened, a special color can be set for their borders. The slave nodes retain this one-color designation until the diagram has been saved (CTRL+S).

### [Example code](javascript:void\(0\);)

When master nodes are inserted manually, the salve nodes are inserted automatically. These slave nodes are displayed with a green border:
    
        <node id="Station" super="Komponente"  
     valid="=isInstanceOf('Rohbau_Baukasten_V2.Mechatronik.RoboterStation')"  
     slaveNodes="=mos('Rohbau_Baukasten_V2.Mechatronik.Roboter')">
    	<figureImage figure="com.mind8.graph2d.figure.Image">
    		<properties>
    			<property id="img">
    				<read value="=type('Rohbau_Baukasten_V2.Diagramm_Konfiguration.  
     				Planungsdiagramm.Register').image(this)"/>
    			</property>
    			<property id="highlightBoColor">
    				<read value="0,255,0"/>
    			</property>
    		</properties>
    	</figureImage>
    	<slaveNode node="Roboter" autoUpdated="false" layout="outsideEdged"  
     	direction="=$diagramDirection" parent="=mc">
    		<movement rotateWithMaster="NO" rotate="NO"/>
    	</slaveNode>
    </node>

### [Example code](javascript:void\(0\);)

Slave nodes are inserted automatically into the diagram subsequently. These slave nodes are displayed with a green border:
    
        <node id="Station" super="Komponente"  
     valid="=isInstanceOf('Rohbau_Baukasten_V2.Mechatronik.RoboterStation')"  
     slaveNodes="=mos('Rohbau_Baukasten_V2.Mechatronik.Roboter')">
    	<figureImage figure="com.mind8.graph2d.figure.Image">
    		<properties>
    			<property id="img">
    				<read value="=type('Rohbau_Baukasten_V2.Diagramm_Konfiguration.  
     				Planungsdiagramm.Register').image(this)"/>
    			</property>
    			<property id="highlightBoColor">
    				<read value="0,255,0"/>
    			</property>
    		</properties>
    	</figureImage>
    	<slaveNode node="Roboter" autoUpdated="true" layout="outsideEdged"  
     	direction="=$diagramDirection" parent="=mc">
    		<movement rotateWithMaster="NO" rotate="NO"/>
    	</slaveNode>
    </node>
