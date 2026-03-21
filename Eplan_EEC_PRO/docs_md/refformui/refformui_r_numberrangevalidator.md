---
title: "numberRangeValidator"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_numberrangevalidator.htm"
file: "refformui_r_numberrangevalidator"
category: "refformui"
---

# numberRangeValidator

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  numberRangeValidator In this type of validation, the content that has been input is converted into a number and compared with the specifications for the lower limit (attribute start) and upper limit (attribute end). When defining specifications you can specify both fixed values as well as formulas. The validation is processed at these points of times:  
     * When building-up the Form-UI page.
     * When pressing the Enter key.
     * When the focus leaves the input field.
If the input is not in the permitted range, the input field is shown with a red background color and the self-defined tooltip (attribute message) then shows a corresponding message. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
end | required | any |  | Upper limit of the allowed range  
message | required | eo, focusOut, modify |  | Text displayed as a tooltip when an error occurred.  
start | required | any |  | Lower limit of the allowed range  
Allowed sub-elements | Quantity  
---|---  
none |   
[Example code](javascript:void\(0\);) A process temperature to be entered must be in the range of -10 through +20.
    
        <input type="text" receiver="parameter('Temperature')" >
    	<inputValidators>
    		<numberRangeValidator start="-10" end="20" message="Valid values are in the range of -10 to +20" />
    	</inputValidators>
    </input>

Result: [Example code](javascript:void\(0\);) A process temperature to be entered must be in the Variables range of $startValue through $endValue. In the formula language these attribute values can be referenced via the specifications nvStart and nvEnd.
    
        <form id="validation" title="Validation">
    	<table border="1" boColor="0,0,0" columns="2">
    		<td>
    			<label>startValue</label>
    		</td>
    		<td>
    			<input receiver="parameter('startValue')"></input>
    		</td> 
    		<td>
    			<label>endValue</label></td>
    		<td>
    			<input receiver="parameter('endValue')"></input>
    		</td>
    		<td>
    			<label>Nominal temperature</labels></td>
    		<td>
    			<input type="text" receiver="parameter('Temperature')" >
    				<inputValidators>
    					<numberRangeValidator 
    						start="=$startValue" 
    						end="=$endValue" 
    						message="='Valid values are in the range of ' + nvStart + ' to ' + nvEnd + '.'" />
    				</inputValidators>
    			</input>
    		</td>
    	</table>
    </form>

Result:
