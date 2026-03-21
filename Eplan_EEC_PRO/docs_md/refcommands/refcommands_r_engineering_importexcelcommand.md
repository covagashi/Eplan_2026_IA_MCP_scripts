---
title: "Engineering.ImportExcelCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_engineering_importexcelcommand.htm"
file: "refcommands_r_engineering_importexcelcommand"
category: "refcommands"
---

# Engineering.ImportExcelCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Engineering.ImportExcelCommand Imports an Excel file according to the specified schema and template file into a project or a project component. The following variants are possible for using the command: Argument | Type | Description  
---|---|---  
pathToSchema | String | Path to the schema file.  
pathToTemplate | String | Path to the template file.  
pathToXls | String | Path to Excel file.  
      
        Engineering.ImportExcelCommand("c:\schema\excel_schema.xml", "c:\templates\csv_template.imx", "c:\importfiles\project.xls")

Argument | Type | Description  
---|---|---  
pathToSchema | String | Path to the schema file.  
pathToTemplate | String | Path to the template file.  
projectName | String | Name of the target project.  
pathToXls | String | Path to Excel file.  
      
        Engineering.ImportExcelCommand("c:\schema\excel_schema.xml", "c:\templates\csv_template.imx", "Feeder", "c:\importfiles\project.xls")

Argument | Type | Description  
---|---|---  
pathToSchema | String | Path to the schema file.  
pathToTemplate | String | Path to the template file.  
projectOrMo | Object | Project or project component.  
pathToXls | String | Path to Excel file.  
      
        Engineering.ImportExcelCommand("c:\schema\excel_schema.xml", "c:\templates\csv_template.imx", Â«FeederÂ», "c:\importfiles\project.xls")
