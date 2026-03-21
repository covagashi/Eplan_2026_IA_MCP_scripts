---
title: "gap"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_gap.htm"
file: "refformui_r_gap"
category: "refformui"
---

# gap

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  gap The Form-UI element <gap> creates a concrete gap with the unit pixel between two Form-UI elements, which are located in one line (element <line>). Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
hSizePx | optional |  |  | Width of the element in pixels  
Allowed sub-elements | Quantity  
---|---  
none |   
Line with gap of 100 pixels between a label and a text box: The following example shows one line in a Form-UI. On the left side is a text and with a concrete gap of 100 pixels on the right side is a text box. [Example code](javascript:void\(0\);)
    
        <line>
    	<label>Place</label>
    	<gap hSizePx="100" />
    	<input type="text" receiver="parameter('Place')" />
    </line>

Result:
