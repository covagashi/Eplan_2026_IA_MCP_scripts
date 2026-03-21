---
title: "ECAD.GenerateEcadProjectFromTypicalFileCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_ecad_generateecadprojectfromtypicalfilecommand.htm"
file: "refcommands_r_ecad_generateecadprojectfromtypicalfilecommand"
category: "refcommands"
---

# ECAD.GenerateEcadProjectFromTypicalFileCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  ECAD.GenerateEcadProjectFromTypicalFileCommand Generates the Eplan Electric P8 project on the basis of a typical.xml in the format of EEC One. The following variants are possible for using the command: Argument | Type | Description  
---|---|---  
pathToTypicalFile | String | Absolute file name of the typical.xml  
      
        ECAD.GenerateEcadProjectFromTypicalFileCommand('C:/typical.xml')

[Example in Form-UI](javascript:void\(0\);)
    
        <action name="ECAD.GenerateEcadProjectFromTypicalFileCommand"
    	arguments="=List{'C:/typical.xml'}"
    	type="link">Generate From typical.xml</action>
