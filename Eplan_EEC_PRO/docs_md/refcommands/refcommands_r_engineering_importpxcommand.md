---
title: "Engineering.ImportPXCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_engineering_importpxcommand.htm"
file: "refcommands_r_engineering_importpxcommand"
category: "refcommands"
---

# Engineering.ImportPXCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Engineering.ImportPXCommand Imports all projects occurring in a PX file. Argument | Type | Description  
---|---|---  
absolutePXFilePath | String | Absolute name of the PX file to import from  
      
        Engineering.ImportPXCommand("c:\importfiles\project.px")

Imports all projects occurring in a PX file. Existing projects can be updated. Argument | Type | Description  
---|---|---  
absolutePXFilePath | String | Absolute name of the PX file to import from  
updateExisting | Boolean | Update existing projects  
      
        Engineering.ImportPXCommand("c:\importfiles\project.px", "true")
