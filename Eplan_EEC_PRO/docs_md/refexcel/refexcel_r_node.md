---
title: "\u003cnode\u003e"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refexcel_r_node.htm"
file: "refexcel_r_node"
category: "refexcel"
---

# \u003cnode\u003e

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  <node> The <node> tag creates a node that corresponds to a mechatronic component. The component of the highest level can be added to a project only once! Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
id | required |  |  | Specifies a unique code for the node.  
name | required |  |  | Specifies the name of the project component.  
typeClass | required |  |  | Specifies the absolute name of the library component from which an instance should be added.  
Allowed sub-elements | Quantity  
---|---  
[<node>]() | any  
[<properties>](refexcel_r_properties.htm) | any  
[Example](javascript:void\(0\);) For this example, the modular system of the tutorial can be used. The Feeder mechatronic component must be supplemented therein by an insertion place for an arbitrary number of arbitrary components. Content of the Excel table:| A| B| C| D  
---|---|---|---|---  
1| Machine_Name| Machine_Type| Functiongroup_Name| Functiongroup_Type  
2| Feeder_2| T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder| Discard_2| T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Discard  
3| Feeder_2| T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder| Insert_2| T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Insert  
4| Feeder_2| T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder| Inspect_2| T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Inspect  
5| Feeder_2| T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder| Move_2| T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Move  
6| Feeder_2| T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder| Store_2| T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Store  
Schema file content:
    
        <?xml version="1.0" encoding="UTF-8"?>
    <schema tableName="Mechatronic" columnKeySeparator="_">
    	<node id="Station" name="${Machine_Name}" typeClass="${Machine_Type}">
    		<node id="Functiongroup" name="${Functiongroup_Name}" typeClass="${Functiongroup_Type}">
    		</node>
    	</node>
    </schema>

Result: The following figure shows the project catalog with the newly imported project NewProject. This project contains the station Feeder_2 as an instance of the library component Feeder as the element of the highest level. The components Discard, Insert, Inspect, Move, and Store are included as standard installed components of Feeder. The components Discard_2, Insert_2, Inspect_2, Move_2, and Store_2 have also been instantiated by Rows 2 to 6 of the Excel table.
