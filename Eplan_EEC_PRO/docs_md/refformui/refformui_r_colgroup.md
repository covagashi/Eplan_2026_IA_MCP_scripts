---
title: "colGroup"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_colgroup.htm"
file: "refformui_r_colgroup"
category: "refformui"
---

# colGroup

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  colGroup The element <colGroup> groups columns, which are superordinate set to the same properties. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
align | optional | left, center, right | left | horizontal alignment of the columns content  
bColor | optional | 0,0,0 to 255,255,255 | System color | Background color as RGB value  
readonly | optional | true, false |  | true = Column group is read-only.  
false = Input can be written to the column group.  
span | optional | Integer |  | Number of columns, which should be set to the same properties  
valign | optional | bottom, middle, top | middle | vertical alignment of the columns content  
width | optional | Absolute value in pixels  
Percentage  
Shares |  | Absolute value in pixels = width of the column in pixels, e.g. "150"  
Percentage = width of the column in relation to the table width, e.g. "30%"  
Shares = number of shares, e.g. "3*"  
Allowed sub-elements | Quantity  
---|---  
[col](refformui_r_col.htm) | any  
Table with column group: The following example shows a table where all columns are grouped together to assign a uniform width and alignment. To show that the configuration of an enclosed element replaces the configuration of the enclosing element, the background color (bColor) of the first column and the alignment of the last column are set to another value. [Example code](javascript:void\(0\);)
    
        <table columns="5" border="1" boColor="0,0,0">
    	<**colgroup** width="80" align="left">
    		<col bColor="200,200,200"/>
    		<col/>
    		<col/>
    		<col/>
    		<col align="right"/>
    	</colGroup>
    	<td><label font="bold">Cell 1.1</label></td>
    	<td><label>Cell 1.2</label></td>
    	<td><label>Cell 1.3</label></td>
    	<td><label>Cell 1.4</label></td>
    	<td><label>Cell 1.5</label></td>
    	<td><label font="bold">Cell 2.1</label></td>
    	<td><label>Cell 2.2</label></td>
    	<td><label>Cell 2.3</label></td>
    	<td><label>Cell 2.4</label></td>
    	<td><label>Cell 2.5</label></td>
    </table>

Result: Table with column group: The following example shows a table with five columns, where only the first 3 columns (span="3") are grouped, to assign a uniform width and alignment. To show that the configuration of an enclosed element replaces the configuration of the enclosing element, the background color (bColor) of the first column and the alignment of the second column are set to another value. [Example code](javascript:void\(0\);)
    
        <table columns="5" border="1" boColor="0,0,0">
    	<colGroup **span="3"** width="80" align="left">
    		<col bColor="200,200,200"/>
    		<col align="center"/>
    	</colGroup>
    	<td><label>Cell 1.1</label></td>
    	<td><label>Cell 1.2</label></td>
    	<td><label>Cell 1.3</label></td>
    	<td><label>Cell 1.4</label></td>
    	<td><label>Cell 1.5</label></td>
    	<td><label>Cell 2.1</label></td>
    	<td><label>Cell 2.2</label></td>
    	<td><label>Cell 2.3</label></td>
    	<td><label>Cell 2.4</label></td>
    	<td><label>Cell 2.5</label></td>
    </table>

Result:
