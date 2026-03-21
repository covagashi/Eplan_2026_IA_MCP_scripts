---
title: "ECAD.GenerateEcadProjectCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_ecad_generateecadprojectcommand.htm"
file: "refcommands_r_ecad_generateecadprojectcommand"
category: "refcommands"
---

# ECAD.GenerateEcadProjectCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  ECAD.GenerateEcadProjectCommand Generates the Eplan Electric P8 project. The following variants are possible for using the command: Argument | Type | Description  
---|---|---  
obj | Root | Root object of the mechatronic for which the project will be created.  
      
        ECAD.GenerateEcadProjectCommand(mroot.parent)

[Example in Form-UI](javascript:void\(0\);)
    
        <action name="ECAD.GenerateEcadProjectCommand"
    	arguments="=mroot.parent"
    	type="link">Generate wiring diagram</action>

Argument | Type | Description  
---|---|---  
wiringDiagram | WiringDiagram | Schematic that is to be created.  
      
        ECAD.GenerateEcadProjectCommand(mos('WiringDiagram').first.derived)

[Example in Form-UI](javascript:void\(0\);)
    
        <action name="ECAD.GenerateEcadProjectCommand"
    	arguments="=mos('WiringDiagram').first.derived"
    	type="link">Generate wiring diagram</action>

Argument | Type | Description  
---|---|---  
pages | List | List of schematic pages to be created.  
      
        ECAD.GenerateEcadProjectCommand(List{mos('WiringDiagram').first.derived.dos('T_Mechatronic_ModularSystem.ECAD.Page.Page')})

[Example in Form-UI](javascript:void\(0\);)
    
        <action name="ECAD.GenerateEcadProjectCommand"
    	arguments="=List{mos('WiringDiagram').first.derived.dos('T_Mechatronic_ModularSystem.ECAD.Page.Page')}"
    	type="link">Generate wiring diagram</action>
