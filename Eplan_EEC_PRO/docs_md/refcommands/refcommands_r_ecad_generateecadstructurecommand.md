---
title: "ECAD.GenerateEcadStructureCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_ecad_generateecadstructurecommand.htm"
file: "refcommands_r_ecad_generateecadstructurecommand"
category: "refcommands"
---

# ECAD.GenerateEcadStructureCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  ECAD.GenerateEcadStructureCommand Generates the ECAD structure. Argument | Type | Description  
---|---|---  
obj | Root | Root object of the mechatronic structure or of a discipline structure  
      
        ECAD.GenerateEcadStructureCommand(mroot.parent)

[Example in Form-UI](javascript:void\(0\);)
    
        <action name="ECAD.GenerateEcadStructureCommand"
    	arguments="=mroot.parent"
    	type="link">Generate ECAD structure</action>
