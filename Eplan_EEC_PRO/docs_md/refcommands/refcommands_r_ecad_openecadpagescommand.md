---
title: "ECAD.OpenECADPagesCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_ecad_openecadpagescommand.htm"
file: "refcommands_r_ecad_openecadpagescommand"
category: "refcommands"
---

# ECAD.OpenECADPagesCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  ECAD.OpenECADPagesCommand Generates and opens the passed wiring diagrams of the project. If the project is not existing yet, it is created, as by OpenECADComponentCommand. If the project already exists, so the pages are created in it. If the pages already exist, the command replaces the existing pages by new ones. Operation in Web EEC installation environment: Returns an URL of the created file. This will open a browser-own dialog in the browser on the client-side for downloading the (in EEC Server created) file. Access to the created file has to be guaranteed on the Web EEC Server as well as on the EEC Server, e.g. by installing both servers on the same computer. Argument | Type | Description  
---|---|---  
objs | List | List of discipline components to create and to open  
      
        ECAD.OpenECADPagesCommand(mos('WiringDiagram').first.derived.dos('T_Mechatronic_ModularSystem.ECAD.Page.Page').first)

[Example in Form-UI](javascript:void\(0\);)
    
        <action name="ECAD.ECAD.OpenECADPagesCommand"
    	arguments="=List{mos('WiringDiagram').first.derived.dos('T_Mechatronic_ModularSystem.ECAD.Page.Page')}"
    	type="link">Regenerate pages</action>

Information The command is only implemented for Electric P8. All other ECAD implementations are not supported!
