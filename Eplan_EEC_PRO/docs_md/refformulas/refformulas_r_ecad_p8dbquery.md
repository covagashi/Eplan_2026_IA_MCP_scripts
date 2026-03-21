---
title: "p8dbquery(String Partnumber, String Variant, Integer Id)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_ecad_p8dbquery.htm"
file: "refformulas_r_ecad_p8dbquery"
category: "refformulas"
---

# p8dbquery(String Partnumber, String Variant, Integer Id)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  p8dbquery(String Partnumber, String Variant, Integer Id) Returns the value of the specified identifying number for the specified part of the specified variant. If the part cannot be found in the parts database, the method returns an error. p8dbquery(String Partnumber, String Variant, Integer Id)  
---  
Arguments | String | Partnumber | Part number  
String | Variant | Part variant  
Integer | Id | Identifying number of the property  
Return value |  |   
[Example in formula](javascript:void\(0\);) Formula | Result  
---|---  
=p8dbquery('TS 8886.500','1',22014) | 597.0  
[Example in the script](javascript:void\(0\);)
    
        return mo.evaluate("p8dbquery('TS 8886.500','1',22014)");

Read more
     * [evaluate()](refscripting_r_calculate_formulas_for_components.htm)
