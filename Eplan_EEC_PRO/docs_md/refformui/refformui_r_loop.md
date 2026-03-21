---
title: "loop"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_loop.htm"
file: "refformui_r_loop"
category: "refformui"
---

# loop

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  loop To iterate consecutively multiple times over Form-UI elements, they are enclosed by the loop element <loop>. The number of loop passes is determined by the receiver attribute. The value of the receiver attribute has to be a list, e.g. receiver="=List(1,2,3,4,5,6,7,8)". The loop is passed once for each item of the list. The variable attribute determines the variable. This variable contains the list value of the current loop pass of the list defined by receiver. As for the above example, the value of the variable for the first pass of the loop is 1, for the second loop pass is 2, etc. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
receiver | required |  |  | Formula to the object  
variable | optional |  |  | Name of the variable  
Allowed sub-elements | Quantity  
---|---  
[action](refformui_r_action.htm) | any  
[img](refformui_r_img.htm) | any  
[include](refformui_r_include.htm) | any  
[input](refformui_r_input.htm) | any  
[instantiation](refformui_r_instantiation.htm) | any  
[group](refformui_r_group.htm) | any  
[label](refformui_r_label.htm) | any  
[line](refformui_r_line.htm) | any  
[loop]() | any  
[open](refformui_r_open.htm) | any  
[tab](refformui_r_tab.htm) | any  
[table](refformui_r_table.htm) | any  
[td](refformui_r_td.htm) | any  
A table calculated with 8 loop passes: A table with 6 columns contains a loop which is passed 8 times. For each loop pass 6 table cells are created, a calculation with the current value of the variable "x" is performed and displayed as an RGB value and as a color. [Example code](javascript:void\(0\);)
    
        <table columns="6">
    	<td></td>
    	<td></td>
    	<td></td>
    	<td></td>
    	<td>
    		<label font="bold">RGB value</label>
    	</td>
    	<td>
    		<label font="bold">Color</label>
    	</td>
    	<loop receiver="=List{1,2,3,4,5,6,7,8}" variable="x">
    		<td align="right">
    			<label>2 raised to the power of </label>
    		</td>
    		<td align="right">
    			<line>
    				<label text="x"></label>
    				<label>: </label>
    			</line>
    		</td>
    		<td>
    			<label>-&gt;</label>
    		</td>
    		<td align="right">
    			<label text="2.pow(x)"></label>
    		</td>
    		<td>
    			<line>
    				<label text="='200,'+(2.pow(x)-1)+','+(2.pow(x)-1)"></label>
    			</line>  
     		</td>
    		<td bColor="='200,'+(2.pow(x)-1)+','+(2.pow(x)-1)">
    			<label></label>
    		</td>
    	</loop>  
    </table>

Result:
