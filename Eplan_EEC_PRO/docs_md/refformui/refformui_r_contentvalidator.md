---
title: "contentValidator"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_contentvalidator.htm"
file: "refformui_r_contentvalidator"
category: "refformui"
---

# contentValidator

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  contentValidator In this type of validation, the input content is compared with the given specifications by means of a regular expression. The validation is processed at these points of times:
     * When building-up the Form-UI page.
     * When pressing the Enter key.
     * When the focus leaves the input field.
If the input is not identical to the regular expression, the input field is shown with a red background color and the self-defined tooltip (attribute message) then shows a corresponding message. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
javaRegEx | required | any |  | Regular expression which describes the allowed content.  
message | required | eo, focusOut, modify |  | Text displayed as a tooltip when an error occurred.  
Allowed sub-elements | Quantity  
---|---  
none |   
Only specific names should be possible for entering a cardinal point. [Example code](javascript:void\(0\);)
    
        <input type="text" receiver="=parameter('Himmelsrichtungen')">
    	<inputValidators>
    	<contentValidator javaRegEx="\b(West|Ost|Nord|SÃ¼d)\b" message="Erlaubte Himmelsrichtungen sind: Nord, SÃ¼d, Ost, West" />
     	</inputValidators>
    </input>

Result:
