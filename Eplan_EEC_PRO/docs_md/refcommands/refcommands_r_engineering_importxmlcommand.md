---
title: "Engineering.ImportXMLCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_engineering_importxmlcommand.htm"
file: "refcommands_r_engineering_importxmlcommand"
category: "refcommands"
---

# Engineering.ImportXMLCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Engineering.ImportXMLCommand Imports a project according to the assigned XML file. In any case, the schema file must be passed as the first argument. Optional an additional template file may be passed. As further arguments for the target either the project name, the project or the project component itself can be specified. An already existing project is overwritten. The following variants are possible for using the command: Argument | Type | Description  
---|---|---  
pathToXslt | String | Path to the schema file.  
pathToXml | String | Path to the XML file.  
      
        Engineering.ImportXMLCommand("c:\schema\schema.xslt", "c:\importfiles\project.xml")

Argument | Type | Description  
---|---|---  
pathToXslt | String | Path to the schema file.  
pathToTemplate | String | Path to the template file.  
pathToXml | String | Path to the XML file.  
      
        Engineering.ImportXMLCommand("c:\schema\schema.xslt", "C:\templates\template.imx", "c:\importfiles\project.xml")

Argument | Type | Description  
---|---|---  
pathToXslt | String | Path to the schema file.  
pathToTemplate | String | Path to the template file.  
pathToProject | String | Path to the project.  
pathToXml | String | Path to the XML file.  
      
        Engineering.ImportXMLCommand("c:\schema\schema.xslt", "C:\templates\template.imx", "Feeder", "c:\importfiles\project.xml")

Argument | Type | Description  
---|---|---  
pathToXslt | String | Path to the schema file.  
pathToTemplate | String | Path to the template file.  
projectOrMo | Object | Project or project component.  
pathToXml | String | Path to the XML file.  
      
        Engineering.ImportXMLCommand("c:\schema\schema.xslt", "C:\templates\template.imx", Â«FeederÂ», "c:\importfiles\project.xml")

Argument | Type | Description  
---|---|---  
pathToXslt | String | Path to the schema file.  
projectOrMo | Object | Project or project component.  
pathToXml | String | Path to the XML file.  
      
        Engineering.ImportXMLCommand("c:\schema\schema.xslt", Â«FeederÂ», "c:\importfiles\project.xml")
