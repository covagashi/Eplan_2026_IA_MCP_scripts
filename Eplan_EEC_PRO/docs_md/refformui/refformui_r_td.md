---
title: "td"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_td.htm"
file: "refformui_r_td"
category: "refformui"
---

# td

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  td The element <td> inserts a table cell. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
align | optional | centre, left, right | left | horizontal alignment of the cell content  
bColor | optional | 0,0,0 to 255,255,255 | System color | Background color as RGB value  
colSpan | optional | Integer |  | Number of cells, that are connected in a row. The attribute value has to be specified as a constant or formula.  
readonly | optional | true, false |  | true = cell is read-only.  
false = Input can be written to the cell.  
rowSpan | optional | Integer |  | Number of cells, that are connected in a column. The attribute value has to be specified as a constant or formula.  
valign | optional | bottom, middle, top | middle | vertical alignment of the cell content  
visible | optional | true, false | true | true = table cell is visible  
true = table cell is invisible  
Allowed sub-elements | Quantity  
---|---  
[action](refformui_r_action.htm) | any  
[group](refformui_r_group.htm) | any  
[img](refformui_r_img.htm) | any  
[include](refformui_r_include.htm) | any  
[input](refformui_r_input.htm) | any  
[instantiation](refformui_r_instantiation.htm) | any  
[label](refformui_r_label.htm) | any  
[line](refformui_r_line.htm) | any  
[loop](refformui_r_loop.htm) | any  
[mailto](refformui_r_mailto.htm) | any  
[open](refformui_r_open.htm) | any  
[progressBar](refformui_r_progressbar.htm) | any  
[table](refformui_r_table.htm) | any  
Table with different alignments of the table cells: The following example shows a simple table listing the various alignments of the content of table cells. The attribute align specifies the horizontal and the attribute valign defines the vertical alignment. [Example code](javascript:void\(0\);)
    
        <table columns="4" border="1" boColor="0,0,0" cellPadding="10" >
    	<td/>
    	<td align="center"><label font="bold">align="left"</label></td>
    	<td align="center"><label font="bold">align="center"</label></td>
    	<td align="center"><label font="bold">align="right"</label></td>
    	<td align="left">
    		<label font="4"/>
    		<label font="bold">valign="top"</label>
    	<label font="4"/>
    	</td>
    	<td align="left" valign="top"><label>abc</label></td>
    	<td align="center" valign="top"><label>abc</label></td>
    	<td align="right" valign="top"><label>abc</label></td>
    	<td align="left">
    		<label font="4"/>
    		<label font="bold">valign="middle"</label>
    		<label font="4"/>
    	</td>
    	<td align="left" valign="middle"><label>abc</label></td>
    	<td align="center" valign="middle"><label>abc</label></td>
    	<td align="right" valign="middle"><label>abc</label></td>
    	<td align="left">
    		<label font="4"/>
    		<label font="bold">valign="bottom"</label>
    		<label font="4"/>
    	</td>
    	<td align="left" valign="bottom"><label>abc</label></td>
    	<td align="center" valign="bottom"><label>abc</label></td>
    	<td align="right" valign="bottom"><label>abc</label></td>
    </table>

Result: Table with connected cells in a row: In the first row of the table the cells of column 2 and 3 are connected. [Example code](javascript:void\(0\);)
    
        <table columns="5" border="2" boColor="0,0,0">
    	<td><label>Zelle 1.1</label></td>
    	<td colSpan="2"><label>Zelle 1.2 + Zelle 1.3</label></td>
    	<td><label>Zelle 1.4</label></td>
    	<td><label>Zelle 1.5</label></td>
    	<td><label>Zelle 2.1</label></td>
    	<td><label>Zelle 2.2</label></td>
    	<td><label>Zelle 2.3</label></td>
    	<td><label>Zelle 2.4</label></td>
    	<td><label>Zelle 2.5</label></td>
    </table>

Result: Table with connected cells in a column: In the first column of the table the cells of row 2 and 3 are connected. The attribute value for rowSpan is calculated by means of a formula. [Example code](javascript:void\(0\);)
    
        <table columns="2" border="2" boColor="0,0,0">
    	<td><label>Zelle 1.1</label></td>
    	<td><label>Zelle 1.2</label></td>
    	<td rowSpan="=1+1"><label>Zelle 2.1 + Zelle 3.1</label></td>
    	<td><label>Zelle 2.2</label></td>
    	<td><label>Zelle 3.2</label></td>
    	<td><label>Zelle 4.1</label></td>
    	<td><label>Zelle 4.2</label></td>
    </table>

Result:
