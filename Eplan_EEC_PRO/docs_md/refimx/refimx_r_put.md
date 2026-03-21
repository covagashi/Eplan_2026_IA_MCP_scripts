---
title: "\u003cput\u003e"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refimx_r_put.htm"
file: "refimx_r_put"
category: "refimx"
---

# \u003cput\u003e

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  <put> IMX The <put> tag writes a key-value pair into a map. The information on the key and value can be passed within the tag with the key and value attributes or with the child elements <key> and <value>. With the help of the child tags <key> and <value>, multiple key-value pairs can be written in one map. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
key | optional |  |  | Specifies the key of a pair.  
value | optional |  |  | Specifies the value of a pair.  
Allowed sub-elements | Quantity  
---|---  
[<key>](refimx_r_key.htm) | any  
[<value>](refimx_r_value.htm) | any  
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
