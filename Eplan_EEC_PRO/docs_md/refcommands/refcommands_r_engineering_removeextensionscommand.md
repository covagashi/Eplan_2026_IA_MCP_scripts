---
title: "Engineering.RemoveExtensionsCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_engineering_removeextensionscommand.htm"
file: "refcommands_r_engineering_removeextensionscommand"
category: "refcommands"
---

# Engineering.RemoveExtensionsCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Engineering.RemoveExtensionsCommand Engineering.RemoveExtensionsCommand The execute method of this command removes the components, which are inserted on extension points. The effective range of this command is limited to the following areas by the different execute methods:  
    1. The entire mechatronic structure.
Argument | Type | Description  
---|---|---  
obj | MechatronicRoot | Root object of the mechatronic  
    2. Below the passed mechatronic component.
Argument | Type | Description  
---|---|---  
obj | MechatronicComponent | Mechatronic component  
    3. On the passed extension point.
Argument | Type | Description  
---|---|---  
obj | Placeholder | Extension point
