---
title: "col"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_col.htm"
file: "refformui_r_col"
category: "refformui"
---

# col

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  col The <col> element determines the properties for one or more table columns. The attributes, which are assigned by the <colGroup> element are replaced by the attributes of the <col> element. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
align | optional | left, center, right | left | horizontal alignment of the columns content  
bColor | optional | 0,0,0 to 255,255,255 | System color | Background color as RGB value  
readonly | optional | true, false |  | true = Column is read-only.  
false = Input can be written to the column.  
span | optional | Integer |  | Number of consecutive columns that should apply to the same properties.  
valign | optional | bottom, middle, top | middle | vertical alignment of the columns content  
width | optional | Absolute value in pixels  
Percentage  
Shares |  | Absolute value in pixels = width of the column in pixels, e.g. "150"  
Percentage = width of the column in relation to the table width, e.g. "30%"  
Shares = number of shares, e.g. "3*"  
Allowed sub-elements | Quantity  
---|---  
none | any  
Table with columns whose widths are defined as shares: The following table with the overall width of 450 pixels consists of three columns. The left column has a width of 4 shares, the middle one of 3 shares and the right one of 2 shares. In this case the width of 450 pixels corresponds to 9 shares (4/9 + 3/9 + 2/9). [Example code](javascript:void\(0\);)
    
        <table width="450" border="2" boColor="0,0,0" columns="3">
    	<colGroup>
    		<col **width="4*"** />
    		<col **width="3*"** />
    		<col **width="2*"** />
    	</colGroup>
    	<td><label>Cell 1.1</label></td>
    	<td><label>Cell 1.2</label></td>
    	<td><label>Cell 1.3</label></td>
    	<td><label>Cell 2.1</label></td>
    	<td><label>Cell 2.2</label></td>
    	<td><label>Cell 2.3</label></td>
    </table>

Result: Table with a configuration of column group and column configuration: The following table consists of 3 columns, whose width are fixed by the configuration of the column group. The first column instead has another width and replaces the configuration in the column group. [Example code](javascript:void\(0\);)
    
        <table border="1" boColor="0,0,0" columns="3">
    	<colGroup width="100">
    		<col width="150"/>
    		<col/>
    		<col/>
    		</colGroup>
    		<td><label>Cell 1.1</label></td>
    		<td><label>Cell 1.2</label></td>
    		<td><label>Cell 1.3</label></td>
    		<td><label>Cell 2.1</label></td>
    		<td><label>Cell 2.2</label></td>
    		<td><label>Cell 2.3</label></td>
    </table>

Result:
