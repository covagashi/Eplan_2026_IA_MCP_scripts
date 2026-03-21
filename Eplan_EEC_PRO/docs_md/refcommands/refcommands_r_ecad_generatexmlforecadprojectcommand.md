---
title: "ECAD.GenerateXmlForEcadProjectCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_ecad_generatexmlforecadprojectcommand.htm"
file: "refcommands_r_ecad_generatexmlforecadprojectcommand"
category: "refcommands"
---

# ECAD.GenerateXmlForEcadProjectCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  ECAD.GenerateXmlForEcadProjectCommand Creates an XML file ec-instructions.xml, as well as the macro files of the project which should be created in the specified folder. If no target path (targetFolderName) is specified, the generated XML file is stored in the folder <User temp path>\EcExport\. If several projects of the same name are to be created for the project, the first macro is stored in the specified target directory and all further ones in subfolders with a sequential number. Values in the ec-instructions.xml can be influenced by means of model variables (see[Eplan Data Zip (.edz) generation](admin_r_modelvar_eplandatazipgeneration.htm)). Argument | Type | Description  
---|---|---  
root | Root | Project component, ECAD discipline components thereof are collected.  
Argument | Type | Description  
---|---|---  
wiringDiagram | WiringDiagram | ECAD component (e.g. page) in the ECAD-structure for which the schematic diagram should be created.  
Argument | Type | Description  
---|---|---  
root | Root | Project component, ECAD discipline components thereof are collected.  
targetFolderName | String | Name of the target directory.  
If a name or a relative path is specified, the created files are stored below the project directory.  
An absolute name can be specified alternatively.  
  
Argument | Type | Description  
---|---|---  
wiringDiagram | WiringDiagram | ECAD component (e.g. page) in the ECAD-structure for which the schematic diagram should be created.  
targetFolderName | String | Name of the target directory.  
If a name or a relative path is specified, the created files are stored below the project directory.  
An absolute name can be specified alternatively.
