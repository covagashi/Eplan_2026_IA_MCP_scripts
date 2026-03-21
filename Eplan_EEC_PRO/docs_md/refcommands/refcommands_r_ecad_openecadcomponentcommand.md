---
title: "ECAD.OpenECADComponentCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_ecad_openecadcomponentcommand.htm"
file: "refcommands_r_ecad_openecadcomponentcommand"
category: "refcommands"
---

# ECAD.OpenECADComponentCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  ECAD.OpenECADComponentCommand Generates and opens the schematic for the passed ECAD component. The created schematic only includes the passed components and all superordinate components. Operation in Web EEC installation environment: Returns an URL of the created file. This will open a browser-own dialog in the browser on the client-side for downloading the (in EEC Server created) file. Access to the created file has to be guaranteed on the Web EEC Server as well as on the EEC Server, e.g. by installing both servers on the same computer. Argument | Type | Description  
---|---|---  
obj | ECADComponent | ECAD component (e.g. page) in the ECAD structure for which the schematic is to be created and opened  
      
        ECAD.OpenECADComponentCommand(mos('WiringDiagram').first.derived.rdos('T_Mechatronic_ModularSystem.ECAD.PLC_Inputs.Sensor_Inductive').first)

[Example in Form-UI](javascript:void\(0\);)
    
        <action name="ECAD.ECAD.OpenECADComponentCommand"
    	arguments="=mos('WiringDiagram').first.derived.rdos('T_Mechatronic_ModularSystem.ECAD.PLC_Inputs.Sensor_Inductive').first"
    	type="link">Open wiring diagram with first inductive sensor</action>
