---
title: "\u003chashMap\u003e"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refimx_r_hashmap.htm"
file: "refimx_r_hashmap"
category: "refimx"
---

# \u003chashMap\u003e

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  <hashMap> IMX The <hashMap> tag describes that the next key-value pairs are written into a map. The tag has no attributes. Allowed sub-elements | Quantity  
---|---  
[<put>](refimx_r_put.htm) | any  
[Example code](javascript:void\(0\);)
    
        <parameter name="SizesMap">
    	<value>
    		<hashMap>
    			<put>
    				<key type="String" value="Height"/>
    				<value type="Integer" value="120"/>
    			</put>
    			<put>
    				<key type="String" value="Width"/>
    				<value type="Integer" value="40"/>
    			</put>
    			<put>
    				<key type="String" value="Depth"/>
    				<value type="Integer" value="10"/>
    			</put>
    		</hashMap>
    	</value>
    </parameter>
