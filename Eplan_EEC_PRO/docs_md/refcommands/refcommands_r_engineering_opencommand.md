---
title: "Engineering.OpenCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_engineering_opencommand.htm"
file: "refcommands_r_engineering_opencommand"
category: "refcommands"
---

# Engineering.OpenCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Engineering.OpenCommand Engineering.OpenCommand Operation in Stand-alone installation environment: Opens the object that is specified by absoluteName. A name that is relative to the eo component can be given instead of the absolute name. The following options exist for opening a Form-UI: Open Form-UI of the object specified with EO: OpenCommand(EO,"#Page:<ID of Form-UI>"). Open Form-UI of the object specified with relative path: OpenCommand(EO,"<relative path>#Page:<ID of Form-UI>"). Open Form-UI of the object specified with absolute path: OpenCommand(EO,"<absolutePath>#Page:<ID of Form-UI>"). Operation in Web EEC installation environment: Returns an URL of the created file. This will open a browser-own dialog in the browser on the client-side for downloading the (in EEC Server created) file. Access to the created file has to be guaranteed on the Web EEC Server as well as on the EEC Server, e.g. by installing both servers on the same computer. Argument | Type | Description  
---|---|---  
eo | Object | Engineering object  
absoluteName | String | Path to the object that is to open
