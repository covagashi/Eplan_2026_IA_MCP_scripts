---
title: "Configuring slave nodes as labels"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutgraph2d_h_configuration_of_slave_nodes_as_label.htm"
file: "tutgraph2d_h_configuration_of_slave_nodes_as_label"
category: "tutgraph2d"
---

# Configuring slave nodes as labels

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Configuring slave nodes as labels With the configuration so far, the nodes stood for themselves. In this section, the existing nodes are to be viewed as Master nodes, to which slave nodes can be assigned as labels. The slave nodes as labels in this diagram fulfill two tasks:
    1. Displaying a label with the name of the Master node on the upper edge of the Master node.
    2. Displaying a label with the name of the slave node, which represents the LAN_Jack of a room component. The room components can later be connected with one another via this slave node.
First, a slave node is configured.
    1. Add the following lines below the node with id=âComponent".
    
        <!-- Slave -->
    <node id="LAN_Jack" valid="=isInstanceOf('IT_ModularSystem.Basic.LAN_Jack')">
    	<figureLabel figure="com.mind8.graph2d.figure.Label">
    		<properties>
    			<property id="text">
    				<read value="=$Name" />
    			</property>
    			<property id="showIcon">
    				<read value="false" />
    			</property>
    		</properties>
    	</figureLabel>
    </node>

[Explanation:](javascript:void\(0\);) The new customer for the slave has the ID LAN_Jack that is still referenced.  
The attribute valid="isInstanceOf('IT_ModularSystem.Basic.LAN_Jack')" determines the type, which the project component must conform to, so that it can be added as LAN_Jack.  
With <figureLabel>, a node is configured, which is to be displayed as a label.  
The property <property id="text"> <read value="=$Name"> describes that the value of the parameter Name is displayed as text.  
The property <property id="showIcon"> <read value="false"> prevents the depiction of a general symbol next to the text of the label.  
The meanings of the individual properties: ID name | Meaning  
---|---  
text | Text or formula, which determines a text, which is to be displayed in the label  
showIcon | Specifies the visibility of the icon in the label  
true = icon is displayed  
false = icon is not displayed  
Now, it is defined how the component LAN_Jack is to be displayed as a slave node on the outside edges of the Master. At the same time, the label that is to display the name of the master component is configured.
    1. Add the following lines below the node with id=âComponent".
    
        <!-- Relation of Master (PC/Printer/Telephone/5waySwitch/2wayLANJack) to Slave (LAN_Jack) and Label -->
    <node id="abstract_Roomcomponent" super="Component" slaveNodes="=rmos('IT_ModularSystem.Basic.LAN_Jack').append(this)">
    	<slaveNode id="SN_LAN_Jack" node="LAN_Jack" layout="outsideEdged" direction="=$Direction" parent="=mc">
    		 <movement direction="WEST SOUTH EAST NORTH" rotate="NO" />
    	</slaveNode>
    	<slaveNode id="SNLabel" valid="=isInstanceEO() and isInstanceOf('IT_Architecture.Levelcomponents.RoomComponent')" layout="outsideEdged" direction="NORTH" parent="=this">
    		<figureLabel figure="com.mind8.graph2d.figure.Label">
    			<properties>
    				<property id="text">
    					<read value="=$Tooltip" />
    				</property>
    				<property id="prefWidth">
    					<read value="100" />
    				</property>
    				<property id="prefHeight">
    					<read value="30" />
    				</property>
    				<property id="showIcon">
    					<read value="false" />
    				</property>
    			</properties>
    		</figureLabel>
    		<property id="showLabel">
    			< read value="true" />
    		</property>
    		 <movement rotateWithMaster="NO" rotate="NO" />
    	</slaveNode>
    </node>

    1. In the tag <node id="Room">, change the attribute acceptedChildren="Master" to acceptedChildren="abstract_Roomcomponent".
    2. In the tag <node id="Master">, change the attribute super="Component" to super="abstract_Roomcomponent".
    3. Save the diagram configuration ([Ctrl] + [S]).
[Explanation:](javascript:void\(0\);) The ID of the new node is abstract_Roomcomponent. Now, the node with the ID Master does not reference Component as being the node from which the properties are inherited any more, it references abstract_Roomcomponent. The node abstract_Roomcomponent now inherits the properties of the node Component. In order that the new node abstract_Roomcomponent can be inserted in a room, it is now approved, through acceptedChildren="abstract_Roomcomponent", as a permitted subordinate component. The attribute slaveNodes="=rmos('IT_ModularSystem.Basic.LAN_Jack').append(this)" defines that all the components of the type LAN_Jack are to be collected as slave nodes. The configuration of the first slave-node type follows. For this type, with node="LAN_Jack", the previously created configuration of the slave node is referenced with the ID SN_LAN_Jack. The attribute layout="outsideEdged" determines that the slave node is to be arranged on the outside edge of the Master. On which outside edge the slave node is arranged is determined by the attribute direction="=$Direction". The value of the parameter Direction is stored in every slave node. The attribute parent="=mc" determines the project component that is valid as the Master. Here it is the project component,that is incorporated in the component LAN_Jack. The subordinate tag <movement direction="WEST SOUTH EAST NORTH" rotate="NO" /> determines that these slave nodes can be pushed to all the outside edges of the Master, but cannot be rotated. The following slave-node configuration has the ID SNLabel. The slave node for this configuration must conform to the type of the attributes valid="=isInstanceEO() and isInstanceOf('IT_Architecture.Levelcomponents.RoomComponent')". These slave nodes too, in keeping with the attribute layout="outsideEdged" are arranged on an outside edge of the Master. These slave nodes are always arranged on the upper edge owing to the attribute direction="NORTH". With the attribute parent="=this", the project component of a device itself, rather than a subordinate one, is defined as the origin of the data which are to be displayed with the label. Then, figureLabel determines that the slave node is shown as a label. In the label, through the property property id="text", a text is displayed, which is saved in the parameter Tooltip of the component. The property id="showLabel" with read value="true" ensures that the label is displayed. Finally, the tag <movement rotateWithMaster="NO" rotate="NO" /> ensures that the slave node does not rotate when the Master node rotates, i.e. the label always remains at the upper edge and the text is always legible.
