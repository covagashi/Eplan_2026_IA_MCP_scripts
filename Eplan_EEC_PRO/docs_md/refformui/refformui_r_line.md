---
title: "line"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_line.htm"
file: "refformui_r_line"
category: "refformui"
---

# line

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  line The Form-UI element <line> arranges sub-elements in one line of the Form-UI. Note Too many UI components and nesting of Form-UIs which is too deep can result in the error message "No more handles". Remedy:
     * Reduce the number of UI components <group>, <line>, <tab> and their child elements.
     * Reduce the nesting depth.
Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
readonly | optional | true, false |  | true = The line is read-only.  
false = Input can be written to the line.  
visible | optional | true, false | true | true = line visible  
true = line invisible  
Allowed sub-elements | Quantity  
---|---  
[action](refformui_r_action.htm) | any  
[img](refformui_r_img.htm) | any  
[include](refformui_r_include.htm) | any  
[input](refformui_r_input.htm) | any  
[instantiation](refformui_r_instantiation.htm) | any  
[label](refformui_r_label.htm) | any  
[open](refformui_r_open.htm) | any  
[progressBar](refformui_r_progressbar.htm) | any  
Lines of several different elements: The following example shows two lines in a Form-UI. The first line displays a check box with text (2 elements), the second line displays two check boxes with text besides (4 elements). [Example code](javascript:void\(0\);)
    
        <line>
    	<input type="check" receiver="parameter('found')"/>
    	<label>wanted</label>
    </line>
    <line>
    	<input type="check" receiver="parameter('found')"/>
    	<label>wanted</label>
    	<input type="check" receiver="parameter('found')"/>
    	<label>found</label>
    </line>

Result:
