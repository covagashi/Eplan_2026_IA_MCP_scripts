---
title: "\u003cproperties\u003e"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refexcel_r_properties.htm"
file: "refexcel_r_properties"
category: "refexcel"
---

# \u003cproperties\u003e

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  <properties> The <properties> tag fills the named parameters of the Map type of the parent component with key-value pairs. If the multiRowEntryKey and multiRowKey attributes are not specified, a one-dimensional map is created that contains, as keys, the entry for the name attribute and, as values, the entry for the typeClass attribute of the parent component. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
name | required |  |  | Specifies the name of the parameter of Map type.  
multiRowEntrykey | optional |  |  | Specifies the absolute name of the library component from which an instance should be added.  
multiRowKey | optional |  |  |   
Allowed sub-elements | Quantity  
---|---  
[<property>](refexcel_r_property.htm) | any  
[Example for a one-dimensional map](javascript:void\(0\);) For this example, the modular system of the tutorial can be used. The following modifications must be made therein:
     * The following library components must be supplemented by an insertion place for an arbitrary number of arbitrary components and by a new parameter MyMap of type Map:
     * Feeder
     * Insert
     * Inspect
     * Move
The content of the Excel table is divided into three sections to be able to better show the content:| A| B  
---|---|---  
1| Machine_Name| Machine_Type  
2| Feeder_2| T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder  
3| Feeder_2| T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder  
4| Feeder_2| T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder  
5| Feeder_2| T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder  
6| Feeder_2| T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder  
| C| D  
---|---|---  
1| Functiongroup_Name| Functiongroup_Type  
2| Discard_2| T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Discard  
3| Insert_2| T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Insert  
4| Inspect_2| T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Inspect  
5| Move_2| T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Move  
6| Store_2| T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Store  
| E| F  
---|---|---  
1| Functionunit_Name| Functionunit_Type  
2| Axis_2| T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Axis  
3| Gripper_2| T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Gripper  
4| Orientationinspector_2| T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Orientationinspector  
5| Separator_2| T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Separator  
6| Stack_2| T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Stack  
Schema file content:
    
        <?xml version="1.0" encoding="UTF-8"?>
    <schema tableName="Mechatronic" columnKeySeparator="_">
    	<node id="Station" name="${Machine_Name}" typeClass="${Machine_Type}">
    		<node id="Functiongroup" name="${Functiongroup_Name}" typeClass="${Functiongroup_Type}">
    			<properties name="SizesMap"/>
    			<node id="Functionunit" name="${Functionunit_Name}" typeClass="${Functionunit_Type}">
    			</node>
    		</node>
    	</node>
    </schema>

Result: The result the key-value pair of the map formed from the entries of the Functiongroup_name and Functiongroup_Type columns. The content of the Functiongroup_name column is entered as the key and the content of the Functiongroup_Type column is entered as the value of the Map.
    
        =Map{
    	Pair{'Name','Axis_2'},
    	Pair{'Type','T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Axis'}
    }

[Example for a three-dimensional map](javascript:void\(0\);) For this example, the modular system of the tutorial can be used. The following modifications must be made therein:
     * The Feeder and Move library components must be supplemented by an insertion place for an arbitrary number of arbitrary components.
     * The Axis library component must be supplemented by a new parameter MyMap of type Map.
The content of the Excel table is divided into four sections to be able to better show the content:| A| B  
---|---|---  
1| Machine_Name| Machine_Type  
2| Feeder_2| T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder  
3| Feeder_2| T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder  
4| Feeder_2| T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder  
5| Feeder_2| T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder  
6| Feeder_2| T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder  
| C| D  
---|---|---  
1| Functiongroup_Name| Functiongroup_Type  
2| |   
3| Move_2| T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Insert  
4| Move_2| T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Inspect  
5| Move_2| T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Move  
6| Move_2| T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Store  
| E| F  
---|---|---  
1| Functionunit_Name| Functionunit_Type  
2| |   
3| Axis_2| T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Axis  
4| Axis_2| T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Axis  
5| Axis_2| T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Axis  
6| Axis_2| T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Axis  
| G| H  
---|---|---  
1| Functionunit_Key_Position| Functionunit_Key_Function  
2| |   
3| 1| Get_item  
4| 2| Inspect_item  
5| 3| Store_good_item  
6| 4| Discard_bad_item  
Schema file content:
    
        <?xml version="1.0" encoding="UTF-8"?>
    <schema tableName="Mechatronic" columnKeySeparator="_">
    	<node id="Station" name="${Machine_Name}" typeClass="${Machine_Type}">
    		<node id="Functiongroup" name="${Functiongroup_Name}" typeClass="${Functiongroup_Type}">
    			<node id="Functionunit" name="${Functionunit_Name}" typeClass="${Functionunit_Type}">
    				<properties name="MyMap" multiRowKey="Key" multiRowEntryKey="Functionunit_Key_Position"/>
    			</node>
    		</node>
    	</node>
    </schema>

Result: The result shows the nested map. The outer map is made up of the key-value pairs that have the ID (Functionunit) of the parent node in the column name, including the first column name with the key word (attribute multiRowKey). Here, the part of the column heading after the separator character (attribute columnKeySeparator) forms the key and the content of the column forms the value of each pair. Starting with the first column whose heading contains the key word (multiRowKey="Key"), the contents of this column are applied as the key and another map is applied as the value. The innermost map forms the key from the column headings with the combination ID_multiRowKey (Functionunit_Key) and the values from the corresponding column values.
    
        =Map{
    	Pair{'Name','X_Axis_2'},
    		Pair{'Key',Map{
    			Pair{'3',Map{
    				Pair{'Function','Store_good_item'},
    				Pair{'Position','3'}
    				}
    			},
    			Pair{'2',Map{
    				Pair{'Function','Inspect_item'},
    				Pair{'Position','2'}
    				}
    			},
    			Pair{'1',Map{
    				Pair{'Function','Get_item'},
    				Pair{'Position','1'}
    				}
    			},
    			Pair{'4',Map{
    				Pair{'Function','Discard_bad_item'},
    				Pair{'Position','4'}
    				}
    			}
    		}	
    	},
    	Pair{'Type','T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Axis'}
    }
