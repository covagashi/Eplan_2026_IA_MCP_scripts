---
title: "keyValidator"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_keyvalidator.htm"
file: "refformui_r_keyvalidator"
category: "refformui"
---

# keyValidator

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  keyValidator This type of validation compares each letter while entering with the specification of a regular expression. It is not possible to input anything that varies from the regular expression. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
javaRegEx | required | any |  | Regular expression which describes the allowed content.  
Allowed sub-elements | Quantity  
---|---  
none |   
For entering a German zip code only 5 numeric numbers are allowed. [Example code](javascript:void\(0\);)
    
        <input type="text" receiver="parameter('Test')">
    	<inputValidators>
    		<keyValidator javaRegEx="[0-9]" />
    		<contentValidator javaRegEx="^[0-9]{5}$" message="5stellige deutsche Postleitzahl eingeben" />
    	</inputValidators>
    </input>

Result:
