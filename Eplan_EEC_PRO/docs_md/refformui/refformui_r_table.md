---
title: "table"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_table.htm"
file: "refformui_r_table"
category: "refformui"
---

# table

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  table The element <table> inserts a table into the Form-UI. Note Attributes whose values can be calculated using the formula language allow design specifications to be made at a central point of the model. Note If the width of the inner table is specified as a percentage at nested tables, the cellPadding="0" attribute must be set for the outer table. If you do not specify the attribute for the outer table, the width of the table changes each time the Form-UI undergoes an updating process. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
align | optional | left, center, right | left | Alignment of the table in the enclosing element  
boColor | optional | 0,0,0 to 255,255,255 | System color | Border color as RGB value  
border | optional | Integer |  | Border thickness in pixels. You can have the value calculated by means of the formula language.  
cellPadding | optional | Integer |  | Distance of the cell contents to the cell border, in pixels. You can have the value calculated by means of the formula language.  
cellSpacing | optional | Integer |  | Distance of the cells to each other and to the table border, in pixels. You can have the value calculated by means of the formula language.  
columns | optional | Integer |  | Number of table columns  
readonly | optional | true, false |  | true = Table is read-only.  
false = Input can be written to the table.  
visible | optional | true, false | true | true = table is visible  
true = table is invisible  
width | optional | Absolute value in pixels  
Percentage |  | Absolute value in pixels = width of the entire table in pixels, e.g. "300"  
Percentage = width of the entire table in relation to the width that is available, e.g. "60%"  
Allowed sub-elements | Quantity  
---|---  
[colGroup](refformui_r_colgroup.htm) | any  
[include](refformui_r_include.htm) | any  
[loop](refformui_r_loop.htm) | any  
[rowGroup](refformui_r_rowgroup.htm) | any  
[td](refformui_r_td.htm) | any  
Table with 3 columns and 2 lines: The following example shows a simple table. The attribute columns with the value "3" divides the table into three columns. An element <td> has to be defined for each column. Since the table has two rows, 6 elements <td> are defined. [Example code](javascript:void\(0\);)
    
        <table **columns="3"** >
    	<td><label>Cell 1.1</label></td>
    	<td><label>Cell 1.2</label></td>
    	<td><label>Cell 1.3</label></td>
    	<td><label>Cell 2.1</label></td>
    	<td><label>Cell 2.2</label></td>
    	<td><label>Cell 2.3</label></td>
    </table>

Result: Table with an absolute width: The example shows a table with 3 columns with an entire width of 300 pixels. [Example code](javascript:void\(0\);)
    
        <table **width="300"** columns="3" border="2" boColor="0,0,0" >
    	<td><label>Cell 1.1</label></td>
    	<td><label>Cell 1.2</label></td>
    	<td><label>Cell 1.3</label></td>
    	<td><label>Cell 2.1</label></td>
    	<td><label>Cell 2.2</label></td>
    	<td><label>Cell 2.3</label></td>
    </table>

Result: Table with red border color: The example shows a table with 3 columns with a red border. [Example code](javascript:void\(0\);)
    
        <table **boColor="255,0,0"** border="2" columns="3">
    	<td><label>Cell 1.1</label></td>
    	<td><label>Cell 1.2</label></td>
    	<td><label>Cell 1.3</label></td>
    	<td><label>Cell 2.1</label></td>
    	<td><label>Cell 2.2</label></td>
    	<td><label>Cell 2.3</label></td>
    </table>

Result: Table with a defined distance between the cell borders and their content: The table displays the content with a distance of 10 pixels to the cell border. [Example code](javascript:void\(0\);)
    
        <table **cellPadding="10"** columns="5" border="1" boColor="0,0,0">
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

Result: Table with a defined distance between the cells: The table displays the cells with a distance of 5 pixels to each other. [Example code](javascript:void\(0\);)
    
        <table **cellSpacing="5"** columns="5" border="1" boColor="0,0,0">
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

Result: Nested tables with a defined alignment: A table is inserted centered into a table cell. [Example code](javascript:void\(0\);)
    
        <table border="2" boColor="0,0,0" columns="2" width="450">
    	<td>
    		<table align="center" border="2" boColor="255,0,0" columns="3">
    			<td><label>Cell 1.1</label></td>
    			<td><label>Cell 1.2</label></td>
    			<td><label>Cell 1.3</label></td>
    			<td><label>Cell 2.1</label></td>
    			<td><label>Cell 2.2</label></td>
    			<td><label>Cell 2.3</label></td>
    		</table>
    	</td>
    	<td/>
    </table>

Result: Table with nesting: Table cells from another configuration are inserted into a table. [Example code](javascript:void\(0\);)
    
        <form title="Table with included cells" id="Table">
    	<table border="1" boColor="0,0,0">
    		<include receiver="this" ref="partId"/>
    	</table>
    </form>
    <form title="includable cells" id="partId">
    	<td><label>Cell 1.1</label></td>
    	<td><label>Cell 1.2</label></td>
    	<td><label>Cell 1.3</label></td>
    	<td><label>Cell 2.1</label></td>
    	<td><label>Cell 2.2</label></td>
    	<td><label>Cell 2.3</label></td>
    </form>

Result:
