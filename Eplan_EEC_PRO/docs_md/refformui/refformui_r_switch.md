---
title: "switch"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_switch.htm"
file: "refformui_r_switch"
category: "refformui"
---

# switch

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  switch The element <switch> with at least one sub-element <case> and one sub-element <default> formulates one or more conditions for displaying either input fields or labels in a column of the pureTable. The conditions are expressed as formulas. The case expressions have to be unique! A default expression must always be given, since one value always has to be supplied. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
receiver | required |  |  | Formula to the object  
Allowed sub-elements | Quantity  
---|---  
[case](refformui_r_case.htm) | 1..n  
[default](refformui_r_default.htm) | 1  
A pureTable displays an input field or a label depending on the parameter value: [Example code](javascript:void\(0\);)
    
        <pureTable receiver="=mos" variable="x">
    	<column heading="Location">
    		<switch receiver="x.parameter('Location').hasValue">
    			<case on="true"><label text="x.$Location"></label></case>
    			<case on="false"><input receiver="x.parameter('Location')"></input></case>
    			<default><label text="='Plant A'"></label></default>
    		</switch>
    	</column>
    </pureTable>

Result: In the table, all the existing values of the parameter Location are displayed as labels (1). If there is no value present for the parameter, a value can be entered with an input field (2).
