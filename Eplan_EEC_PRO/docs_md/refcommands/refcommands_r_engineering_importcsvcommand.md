---
title: "Engineering.ImportCSVCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_engineering_importcsvcommand.htm"
file: "refcommands_r_engineering_importcsvcommand"
category: "refcommands"
---

# Engineering.ImportCSVCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Engineering.ImportCSVCommand Imports a project according to the assigned CSV file. In any case, the schema file must be passed as the first argument. Optional an additional template file may be passed. As further arguments for the target either the project name, the project or the project component itself can be specified. An already existing project is overwritten. If no separator is specified, the command interprets each semicolon as a separator. The following variants are possible for using the command: Argument | Type | Description  
---|---|---  
pathToXslt | String | Path to the schema file.  
pathToCsv | String | Path to the CSV file.  
delimiter | String | Separator, standard = Semicolon (;)  
      
        Engineering.ImportCSVCommand("c:\schema\csv_schema.xslt", "c:\importfiles\project.csv", ";")

Argument | Type | Description  
---|---|---  
pathToXslt | String | Path to the schema file.  
pathToTemplate | String | Path to the template file.  
pathToCsv | String | Path to the CSV file.  
delimiter | String | Separator, standard = Semicolon (;)  
      
        Engineering.ImportCSVCommand("c:\schema\csv_schema.xslt", "c:\templates\csv_template.imx", "c:\importfiles\project.csv", ";")

Argument | Type | Description  
---|---|---  
pathToXslt | String | Path to the schema file.  
pathToTemplate | String | Path to the template file.  
pathToProject | String | Path to the project.  
pathToCsv | String | Path to the CSV file.  
delimiter | String | Separator, standard = Semicolon (;)  
      
        Engineering.ImportCSVCommand("c:\schema\csv_schema.xslt", "c:\templates\csv_template.imx", "Feeder", "c:\importfiles\project.csv", ";")

Argument | Type | Description  
---|---|---  
pathToXslt | String | Path to the schema file.  
pathToTemplate | String | Path to the template file.  
projectOrMo | Object | Project or project component.  
pathToCsv | String | Path to the CSV file.  
delimiter | String | Separator, standard = Semicolon (;)  
      
        Engineering.ImportCSVCommand("c:\schema\csv_schema.xslt", "c:\templates\csv_template.imx", Â«FeederÂ», "c:\importfiles\project.csv", ";")

Argument | Type | Description  
---|---|---  
pathToXslt | String | Path to the schema file.  
projectOrMo | Object | Project or project component.  
pathToCsv | String | Path to the CSV file.  
delimiter | String | Separator, standard = Semicolon (;)  
      
        Engineering.ImportCSVCommand("c:\schema\csv_schema.xslt", Â«FeederÂ», "c:\importfiles\project.csv", ";")
