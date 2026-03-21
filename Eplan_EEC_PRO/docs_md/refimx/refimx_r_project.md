---
title: "\u003cproject\u003e"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refimx_r_project.htm"
file: "refimx_r_project"
category: "refimx"
---

# \u003cproject\u003e

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  <project> IMX The tag <project> addresses an existing project or creates a new project. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
mroot | optional |  |  | Specifies the name of the mechatronic root node. This has to match the name of the existing mechatronic root node in the case of importing into an existing project. If no name is specified, the language-specific default name (for example Mechatronic) applies.  
name | optional |  |  | Specifies the name of the project. If a start object passed during import or through the command, this attribute is omitted.  
delete | optional | true, false | false | Deletes an existing project with the specified name.  
save | optional | true, false | true | Save the project after creating.  
Allowed sub-elements | Quantity  
---|---  
[<libraries>](refimx_r_libraries.htm) | 1..n  
[<mo>](refimx_r_mo.htm) | any  
[Example code](javascript:void\(0\);)
    
        <project name="Feeder" save="true">
