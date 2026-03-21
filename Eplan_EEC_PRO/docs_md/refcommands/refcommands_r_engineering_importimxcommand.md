---
title: "Engineering.ImportIMXCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_engineering_importimxcommand.htm"
file: "refcommands_r_engineering_importimxcommand"
category: "refcommands"
---

# Engineering.ImportIMXCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Engineering.ImportIMXCommand Imports a project according to the assigned IMX file. As a further argument for the target either the project name, the project or the project component itself can be specified. An already existing project is overwritten. The following variants are possible for using the command: Argument | Type | Description  
---|---|---  
pathToImx | String | Path to the IMX file.  
      
        Engineering.ImportIMXCommand("c:\importfiles\project.imx")

Argument | Type | Description  
---|---|---  
projectName | String | Name of the target project.  
pathToImx | String | Path to the IMX file.  
      
        Engineering.ImportIMXCommand("Feeder", "c:\importfiles\project.imx")

Argument | Type | Description  
---|---|---  
projectOrMo | Object | Project or project component.  
pathToImx | String | Path to the IMX file.  
      
        Engineering.ImportIMXCommand(Â«FeederÂ», "c:\importfiles\project.imx")
