---
title: "\u003cvalue\u003e"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refimx_r_value.htm"
file: "refimx_r_value"
category: "refimx"
---

# \u003cvalue\u003e

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  <value> IMX The <value> tag writes a value into the parameter whose name is specified in the parent tag. If one of the child elements follows, the value is defined only in the next tag. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
type | optional | String, Boolean, Integer, Double, Object, Formula | String | Specifies the type of the parameter value. If type is not specified, the value is converted into type String.  
value | required |  |  | Specifies the value of the parameter.  
Allowed sub-elements | Quantity  
---|---  
[<hashMap>](refimx_r_hashmap.htm) | any  
[<arrayList>](refimx_r_arraylist.htm) | any  
[Example code for simple parameters](javascript:void\(0\);)
    
        <parameter name="Option_Inspect_available">
    	<value type="Boolean" value="true"/>
    </parameter>

[Example code for a map](javascript:void\(0\);)
    
        <parameter name="SizesMap">
    	<value>
    		<hashMap>
    			<put>
    				<key type="String" value="Height" />
    				<value type="Integer" value="120" />
    			</put>
    			<put>
    				<key type="String" value="Width" />
    				<value type="Integer" value="40" />
    			</put>
    			<put>
    				<key type="String" value="Depth" />
    				<value type="Integer" value="10" />
    			</put>
    		</hashMap>
    	</value>
    </parameter>
