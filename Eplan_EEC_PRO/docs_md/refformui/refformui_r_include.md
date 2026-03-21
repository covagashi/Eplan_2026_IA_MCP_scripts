---
title: "include"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_include.htm"
file: "refformui_r_include"
category: "refformui"
---

# include

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  include The element <include> inserts the content of a Form-UI at the place where the element tag <include> is positioned. If the Form-UI which is inserted with <include>, contains buttons, they can be displayed explicitly with the showButton attribute. Note Too many UI components and nesting of Form-UIs which is too deep can result in the error message "No more handles". Remedy:
     * Reduce the number of UI components <group>, <line>, <tab> and their child elements.
     * Reduce the nesting depth.
Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
readonly | optional | true, false |  | true = The inserted Form-UI is read-only.  
false = Input can be written to the inserted Form-UI.  
receiver | required |  |  | Formula to the object  
ref | required | Form-UI ID |  | Shows the Form-UI with the corresponding ID No value has to be supplied for displaying buttons.  
showButtons | optional | Button-IDs |  | Shows the buttons with the corresponding IDs  
visible | optional | true, false | true | true = the included element is visible  
false = the included element is invisible  
Allowed sub-elements | Quantity  
---|---  
none |   
Example code of a simple nesting: The following example shows a Form-UI, which includes the Form-UI with the id="docu" attribute by means of the ref="docu" attribute. The Form-UI element <instantiation> is represented as a hyperlink. [Example code](javascript:void\(0\);)
    
        <group title="Include without buttons" expanded="false">
    	<loop variable="x" receiver="mosWithPlaceholders">
    		<instantiation receiver="x"
    			visible="x.isInstanceOf('Engineering.Placeholder')"
    			type="link" name="='St'+(mc.mos.indexOf(this)+1)+type.name" />
    		<include visible="not x.isInstanceOf('Engineering.Placeholder')"
    			receiver="x" ref="docu" />
    	</loop>
    </group>

Result: Example code for a nesting with attribute showButtons: The following example shows the same nesting as the previous example, but the showButtons attribute has the value DELETE, which adds a button for each instantiated object, for deleting its self. The Form-UI element <instantiation> is represented as a hyperlink with calculated text. [Example code](javascript:void\(0\);)
    
        <group title="Include with delete Buttons and calculated text" expanded="false">
    	<loop variable="x" receiver="mosWithPlaceholders">
    		<instantiation text="8/2+5" receiver="x"
    			visible="x.isInstanceOf('Engineering.Placeholder')" type="link"
    			name="='St'+(mc.mos.indexOf(this)+1)+type.name" />
    		<include showButtons="DELETE"
    			visible="not x.isInstanceOf('Engineering.Placeholder')" receiver="x"
    			ref="docu" />
    	</loop>
    </group>

Result: Example code for a nesting with attribute showButtons: The following example shows the same nesting as the previous example, but the showButtons attribute has the value MOVE, which adds a button for each instantiated object, for moving its self. The Form-UI element <instantiation> is represented as a button. [Example code](javascript:void\(0\);)
    
        <group title="Include only with move buttons and type=&quot;button&quot;"
    	expanded="false">
    	<loop variable="x" receiver="mosWithPlaceholders">
    		<instantiation receiver="x"
    			visible="x.isInstanceOf('Engineering.Placeholder')" type="button"
    			name="='St'+(mc.mos.indexOf(this)+1)+type.name" />
    		<include showButtons="MOVE"
    			visible="not x.isInstanceOf('Engineering.Placeholder')" receiver="x"
    			ref="docu" />
    	</loop>
    </group>

Result: Example code for a nesting with attribute showButtons: The following example shows the same nesting as the previous example, but the showButtons attribute has the value DELETE|MOVE, which adds a button for each instantiated object, for deleting and moving its self. The Form-UI element <instantiation> is represented as a hyperlink. [Example code](javascript:void\(0\);)
    
        <group title="Include with delete and move buttons" expanded="false">
    	<loop variable="x" receiver="mosWithPlaceholders">
    	<instantiation
    		receiver="x" visible="x.isInstanceOf('Engineering.Placeholder')"
    		type="link" name="='St'+(mc.mos.indexOf(this)+1)+type.name" />
    	<include showButtons="DELETE|MOVE"
    		visible="not x.isInstanceOf('Engineering.Placeholder')"
    		receiver="x" ref="docu" />
    	</loop>
    </group>

Result:
