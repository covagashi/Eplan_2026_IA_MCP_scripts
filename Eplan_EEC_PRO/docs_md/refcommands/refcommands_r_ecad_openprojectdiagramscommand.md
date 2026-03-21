---
title: "ECAD.OpenProjectDiagramsCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_ecad_openprojectdiagramscommand.htm"
file: "refcommands_r_ecad_openprojectdiagramscommand"
category: "refcommands"
---

# ECAD.OpenProjectDiagramsCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  ECAD.OpenProjectDiagramsCommand Generates and opens all schematic diagrams of a project. Operation in Web EEC installation environment: Returns an URL of the created file. This will open a browser-own dialog in the browser on the client-side for downloading the (in EEC Server created) file. Access to the created file has to be guaranteed on the Web EEC Server as well as on the EEC Server, e.g. by installing both servers on the same computer. Argument | Type | Description  
---|---|---  
obj | Root | Root object for which the complete schematic diagram is to be generated and opened  
      
        ECAD.OpenProjectDiagramsCommand(mroot.parent)

[Example in Form-UI](javascript:void\(0\);)
    
        <action name="ECAD.OpenProjectDiagramsCommand"
    	arguments="=mroot.parent"
    	type="link">Open all wiring diagrams</action>
