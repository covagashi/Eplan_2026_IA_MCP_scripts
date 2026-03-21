---
title: "Engineering.UpdateExtensionsCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_engineering_updateextensionscommand.htm"
file: "refcommands_r_engineering_updateextensionscommand"
category: "refcommands"
---

# Engineering.UpdateExtensionsCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Engineering.UpdateExtensionsCommand Engineering.UpdateExtensionsCommand The execute methods of this command remove the invalid components, which are inserted on extension points and inserts new valid components. As remaining components are not changed. The [Engineering.RemoveExtensionsCommand](refcommands_r_engineering_removeextensionscommand.htm) is to be used to remove all components, which are inserted on extension points. The effective range of this command is limited to the following areas by the different execute methods:
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
