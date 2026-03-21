---
title: "group"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_group.htm"
file: "refformui_r_group"
category: "refformui"
---

# group

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  group By means of the Form-UI element <group>, the elements nested by this tag are grouped. Note Too many UI components and nesting of Form-UIs which is too deep can result in the error message "No more handles". Remedy:
     * Reduce the number of UI components <group>, <line>, <tab> and their child elements.
     * Reduce the nesting depth.
Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
bColor | optional | 0,0,0 to 255,255,255 | System color | Background color as RGB value  
expanded | optional | true, false | true | true = group is expanded at start  
true = group is collapsed at start  
font | optional | Font name-style-size | System font | Font name, style, and size for displaying text  
hSize | optional |  |  | Width of the element  
EEC = width in characters  
Web application = width in pixels  
hSizeMax | optional |  |  | maximum width of the element  
EEC = width in characters  
Web application = width in pixels  
hSizeMaxPx | optional |  |  | maximum width of the element in pixels  
hSizeMin | optional |  |  | minimum width of the element  
EEC = minimum width in characters  
Web application = minimum width in pixels  
hSizeMinPx | optional |  |  | minimum width of the element  
EEC = minimum width in pixels  
Web application = minimum width in pixels  
readonly | optional | true, false |  | true = Group is read-only.  
false = Input can be written to the group.  
title | required | any |  | Text of the title  
twistie | optional | true, false | true | true = expanding and collapsing is active  
false = expanding and collapsing is inactive  
visible | optional | true, false | true | true = Form-UI is visible in the list of Form-UIs  
false = Form-UI is invisible in the list of Form-UIs  
vSize | optional |  |  | Height of the element  
EEC = height in characters  
Web application = height in pixels  
vSizeMax | optional |  |  | maximum height of the element  
EEC = maximum height in characters  
Web application = maximum height in pixels  
vSizeMaxPx | optional |  |  | maximum height of the element  
EEC = maximum height in pixels  
Web application = maximum height in pixels  
vSizeMin | optional |  |  | minimum height of the element  
EEC = minimum height in characters  
Web application = minimum height in pixels  
vSizeMinPx | optional |  |  | minimum height of the element  
EEC = minimum height in pixels  
Web application = minimum height in pixels  
Allowed sub-elements | Quantity  
---|---  
[action](refformui_r_action.htm) | any  
[group]() | any  
[img](refformui_r_img.htm) | any  
[include](refformui_r_include.htm) | any  
[input](refformui_r_input.htm) | any  
[instantiation](refformui_r_instantiation.htm) | any  
[label](refformui_r_label.htm) | any  
[line](refformui_r_line.htm) | any  
[loop](refformui_r_loop.htm) | any  
[open](refformui_r_open.htm) | any  
[progressBar](refformui_r_progressbar.htm) | any  
[table](refformui_r_table.htm) | any  
Groups with the attribute twistie can be expanded and collapsed, to improve the overview within a Form-UI. To expand and collapse you have to click on the triangle, that is displayed at the left border (see the following figure). The triangle with the tip down (2) marks a group that can be expanded, a triangle with the tip right marks a collapsed one. Groups without the attribute twistie or with twistie="false" are always displayed in expanded manner and cannot be collapsed (3). The attribute expanded controls the appearance of a group whilst opening a Form-UI. If the value is true, then the group is expanded whilst opening, if the value is false, then it is collapsed. [Example code](javascript:void\(0\);)
    
        <form title="Grouping" id="Grouping">
    	<line>
    		<label>The group tag groups all enclosed tags.</label>
    	</line>
    	<group title="Example 1" twistie="false">
    		<group title="twistie=&quot;true&quot;" twistie="true">
    			<label>Expandable and collapsible group</label>
    		</group>
    	</group>
    	<group title="Example 2" twistie="false">
    		<group title="font=&quot;Arial-regular-14&quot;" font="Arial-regular-14">
    			<label>Group with specific font</label>
    		</group>
    	</group>
    	<group title="Example 3" twistie="false">
    		<group title="expanded=&quot;false&quot;" expanded="false">
    			<label>Initially collapsed group</label>
    		</group>
    	</group>
    	<group title="Attributes" expanded="false">
    		<table columns="3">
    			<td><label font="bold">Attribute name</label></td>
    			<td><label font="bold">Explanation</label></td>
    			<td><label font="bold">Default</label></td>
    			<td align="left"><label>title</label></td>
    			<td align="left"><label>Text of group</label></td>
    			<td align="left"></td>
    			<td align="left"><label>font</label></td>
    			<td align="left"><label>Font style and size for the title representation</label></td>
    			<td align="left"><label>System font</label></td>
    			<td align="left"><label>twistie</label></td>
    			<td align="left"><label>Group is expandable and collapsible</label></td>
    			<td align="left"><label>true</label></td>
    			<td align="left"><label>expanded</label></td>
    			<td align="left"><label>Group is initially expanded or collapsed</label></td>
    			<td align="left"><label>true</label></td>
    			<td align="left"><label>visible</label></td>
    			<td align="left"><label>Shows or hides the group</label></td>
    			<td align="left"><label>true</label></td>
    		</table>
    	</group>
    </form>

Result:
