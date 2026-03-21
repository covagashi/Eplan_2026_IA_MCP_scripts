---
title: "Engineering.ImportIMXWithTemplateCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_engineering_importimxwithtemplatecommand.htm"
file: "refcommands_r_engineering_importimxwithtemplatecommand"
category: "refcommands"
---

# Engineering.ImportIMXWithTemplateCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Engineering.ImportIMXWithTemplateCommand Imports an IMX file according to the specified template file into a project or a project component. The following variants are possible for using the command: Argument | Type | Description  
---|---|---  
pathToTemplate | String | Path to the template file.  
pathToImx | String | Path to the IMX file.  
      
        Engineering.ImportIMXWithTemplateCommand("c:\templates\template.imx", "c:\importfiles\project.imx")

Argument | Type | Description  
---|---|---  
pathToTemplate | String | Path to the template file.  
projectName | String | Name of the target project.  
pathToImx | String | Path to the IMX file.  
      
        Engineering.ImportIMXWithTemplateCommand("c:\templates\template.imx", "Feeder", "c:\importfiles\project.imx")

Argument | Type | Description  
---|---|---  
pathToTemplate | String | Path to the template file.  
projectOrMo | Object | Project or project component.  
pathToImx | String | Path to the IMX file.  
      
        Engineering.ImportIMXWithTemplateCommand("c:\templates\template.imx", Â«FeederÂ», "c:\importfiles\project.imx")
