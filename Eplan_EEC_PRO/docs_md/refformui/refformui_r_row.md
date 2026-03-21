---
title: "row"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_row.htm"
file: "refformui_r_row"
category: "refformui"
---

# row

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  row The element <row> determines the properties for one or more table rows. The attributes, which are assigned by the element <rowGroup> are replaced by the attributes of the element <row>. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
height | optional | Absolute value in pixels |  | Absolute value in pixels = height of the row in pixels, e.g. "150"  
readonly | optional | true, false |  | true = Row is read-only.  
false = Input can be written to the line.  
Allowed sub-elements | Quantity  
---|---  
none | any  
Table with a configuration of column group and row: The following table consists of 3 rows, whose heights are fixed by the configuration of the row group. The second row instead has another height and replaces the configuration in the row group. [Example code](javascript:void\(0\);)
    
        <table columns="2" boColor="0,0,0" border="2">
    	**< rowGroup height="50">**
    		<row/>
    		**< row height="100"/>**
    		<row/>  
     	</rowGroup>
    	<td><label>Cell 1.1</label></td>
    	<td><label>Cell 1.2</label></td>
    	<td><label>Cell 2.1</label></td>
    	<td><label>Cell 2.2</label></td>
    	<td><label>Cell 3.1</label></td>
    	<td><label>Cell 3.2</label></td>
    </table>

Result:
