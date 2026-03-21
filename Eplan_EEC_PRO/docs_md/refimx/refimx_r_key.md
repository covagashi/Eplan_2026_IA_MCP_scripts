---
title: "\u003ckey\u003e"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refimx_r_key.htm"
file: "refimx_r_key"
category: "refimx"
---

# \u003ckey\u003e

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  <key> IMX The <key> tag specifies the key for a key-value pair in a map. The tag has no sub-elements. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
type | required | String, Boolean, Integer, Double, Object, Formula | String | Specifies the type of the key. If type is not specified, the key is converted into type String.  
value | required |  |  | Specifies the key of a pair.  
[Example code](javascript:void\(0\);)
    
        <parameter name="SizesMap">
    	<value>
    		<hashMap>
    			<put>
    				<key type="String" value="Height">
    				<value type="Integer" value="120">
    			</put>
    			<put>
    				<key type="String" value="Width">
    				<value type="Integer" value="40">
    			</put>
    			<put>
    				<key type="String" value="Depth">
    				<value type="Integer" value="10">
    			</put>
    		</hashMap>
    	</value>
    </parameter>
