---
title: "Engineering.ExportEOXCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_engineering_exporteoxcommand.htm"
file: "refcommands_r_engineering_exporteoxcommand"
category: "refcommands"
---

# Engineering.ExportEOXCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Engineering.ExportEOXCommand Exports the selected assemblies to an EOX file. Argument | Type | Description  
---|---|---  
obj | Root | Root object of the mechatronic structure or of a discipline structure  
Argument | Type | Description  
---|---|---  
fileName | String | Name of the EOX file to be exported to.  
assembliesToExport | List | List of assemblies to be exported to the EOX file.  
[Example code](javascript:void\(0\);) The following example was inserted into the Mechatronic tutorial, but is not part of the tutorial. In the T_Mechatronic_ModularSystem class, an Action must be created, that has the following contents: This Action calls the ExportEoxCommand command and transfers the filename of the EOX file and Assembly arguments. The Assembly must be transferred as an object in a list. The Action is called in this example by means of a button in a Form-UI. In the T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder class, the following Form-UI is inserted:
    
        <?xml version="1.0" encoding="UTF-8"?>
    <uis xmlns="http://www.mind8.com/FormUI" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    	<form title="Feeder" id="feeder">
    		<label text="='Pressing the button exports the project to an EOX file'"></label>
    		<action name="T_Mechatronic_ModularSystem.ExportEOXAction"
    			type="button"
    			arguments="=List{'C:\\MyProjects\\Feeder.eox',List{this.project.name}}">Export</action>
    	</form>
    </uis>

The Form-UI in the project:When the button is pressed, EEC exports the project as an EOX file after C:\MyProjects\Feeder.eox.
