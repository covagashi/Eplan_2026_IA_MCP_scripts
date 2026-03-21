---
title: "\u003cschema\u003e"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refexcel_r_schema.htm"
file: "refexcel_r_schema"
category: "refexcel"
---

# \u003cschema\u003e

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  <schema> The <schema> tag is the top-level element in a schema file. All following tags are wrapped by this element. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
tableName | required |  |  | Specifies the name of the worksheet in the Excel file.  
columnKeySeparator | optional |  |  | Specifies the character that surrounds the key for a multidimensional map.  
This example uses the character '_' to bookend the key:  
Functionunit_Key_Position  
Allowed sub-elements | Quantity  
---|---  
[<node>](refexcel_r_node.htm) | 1  
[Example code](javascript:void\(0\);)
    
        <schema tableName="ActuatorData" columnKeySeparator="_">
