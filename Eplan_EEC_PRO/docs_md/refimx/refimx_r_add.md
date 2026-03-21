---
title: "\u003cadd\u003e"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refimx_r_add.htm"
file: "refimx_r_add"
category: "refimx"
---

# \u003cadd\u003e

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  <add> IMX The <add> tag specifies, as a child tag of <libraries>, which library must be imported into the project. As the child tag of <arrayList>, the <add> tag indicates what value must be added to a list. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
value | required |  |  | Specifies, as a child tag of <libraries>, the names of a library.  
Specifies, as a child tag of <arrayList>, the value to be added.  
type | optional | String, Boolean, Integer, Double, Object, Formula | String | Specifies the type of the value that must be added to a list. If type is not specified, the value is converted into type String.  
Allowed sub-elements | Quantity  
---|---  
[<hashMap>](refimx_r_hashmap.htm) | 1  
[<arrayList>](refimx_r_arraylist.htm) | 1  
[Example code for library](javascript:void\(0\);)
    
        <libraries>
    	<add type="String" value="T_Mechatronic_ModularSystem"/>
    </libraries>

[Example code for list](javascript:void\(0\);)
    
        <parameter name="FunctionUnits">
    	<value>
    		<arrayList>
    			<add value="Axis" type="String"/>
    			<add value="Gripper" type="String"/>
    			<add value="OrientationInspector" type="String"/>
    			<add value="Separator" type="String"/>
    			<add value="Stack" type="String"/>
    		</arrayList>
    	</value>
    </parameter>
