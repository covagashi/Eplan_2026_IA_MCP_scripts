---
title: "ECAD.OpenEcadProjectCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_ecad_openecadprojectcommand.htm"
file: "refcommands_r_ecad_openecadprojectcommand"
category: "refcommands"
---

# ECAD.OpenEcadProjectCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  ECAD.OpenEcadProjectCommand Opens the Eplan Electric P8 project. Operation in Web EEC installation environment: Returns an URL of the created file. This will open a browser-own dialog in the browser on the client-side for downloading the (in EEC Server created) file. Access to the created file has to be guaranteed on the Web EEC Server as well as on the EEC Server, e.g. by installing both servers on the same computer. The following variants are possible for using the command: Argument | Type | Description  
---|---|---  
wiringDiagram | ECAD.WiringDiagram | Schematic for which the project is to be opened.  
      
        ECAD.OpenEcadProjectCommand(mos('WiringDiagram').first.derived)

[Example in Form-UI](javascript:void\(0\);)
    
        <action name="ECAD.OpenEcadProjectCommand"
    	arguments="=mos('WiringDiagram').first.derived"
    	type="link">Open wiring diagram</action>

Argument | Type | Description  
---|---|---  
root | Root | Root object of the mechatronic for which the project will be created.  
      
        ECAD.OpenEcadProjectCommand(mroot.parent)

[Example in Form-UI](javascript:void\(0\);)
    
        <action name="ECAD.OpenEcadProjectCommand"
    	arguments="=mroot.parent"
    	type="link">Open wiring diagram</action>

Argument | Type | Description  
---|---|---  
pages | List | Opens the schematic that contains the schematic pages in the list.  
      
        ECAD.OpenEcadProjectCommand(List{mos('WiringDiagram').first.derived.dos('T_Mechatronic_ModularSystem.ECAD.Page.Page')})

[Example in Form-UI](javascript:void\(0\);)
    
        <action name="ECAD.OpenEcadProjectCommand"
    	arguments="=List{mos('WiringDiagram').first.derived.dos('T_Mechatronic_ModularSystem.ECAD.Page.Page')}"
    	type="link">Open wiring diagram</action>
