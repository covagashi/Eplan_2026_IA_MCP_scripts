---
title: "ECAD.GenerateECADCodeCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_ecad_generateecadcodecommand.htm"
file: "refcommands_r_ecad_generateecadcodecommand"
category: "refcommands"
---

# ECAD.GenerateECADCodeCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  ECAD.GenerateECADCodeCommand Generates the schematic. Argument | Type | Description  
---|---|---  
obj | ECADComponent | ECAD component (e.g. page) in the ECAD-structure for which the schematic diagram should be created.  
      
        ECAD.GenerateEcadCodeCommand(mos('WiringDiagram').first.derived)

[Example in Form-UI](javascript:void\(0\);)
    
        <action name="ECAD.GenerateEcadCodeCommand"
    	arguments="=mos('WiringDiagram').first.derived"
    	type="link">Generate ECAD code</action>
