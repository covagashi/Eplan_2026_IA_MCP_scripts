---
title: "Engineering.SetParameterValueFromJsonFileCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_engineering_setparametervaluefromjsonfilecommand.htm"
file: "refcommands_r_engineering_setparametervaluefromjsonfilecommand"
category: "refcommands"
---

# Engineering.SetParameterValueFromJsonFileCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Engineering.SetParameterValueFromJsonFileCommand Note This command can be used both in the Job Server environment with fileTrigger as well with a normal EEC installation. Saves the contents of a JSON file as map in a parameter. The JSON file is transferred to the Job Server via FileTrigger. The following variant of the command writes the contents of the specified JSON file into the parameter whose name is defined in the model variables. The parameter must be contained in the project component of the uppermost level. Argument | Type | Description  
---|---|---  
jsonFile | String | Name of the JSON file.  
      
        Engineering.SetParameterValueFromJsonCommand("c:\json\parameter.json")

The following variant of the command writes the contents of the specified JSON file into the parameter whose name is defined in the model variables. The parameter must be included in the specified project component. Argument | Type | Description  
---|---|---  
jsonFile | String | Name of the JSON file.  
componentPath | String | Path to the project component.  
      
        Engineering.SetParameterValueFromJsonCommand("c:\json\parameter.json", "Feeder.Mechatronic.Feeder")

The following variant of the command writes the contents of the specified JSON file into the parameter whose name is transferred. The parameter must be included in the specified project component. Argument | Type | Description  
---|---|---  
jsonFile | String | Name of the JSON file.  
componentPath | String | Path to the project component.  
parameterName | String | Name of the parameter.  
      
        Engineering.SetParameterValueFromJsonCommand("c:\json\parameter.json", "Feeder.Mechatronic.Feeder", "MyJsonData")

The following variant of the command writes the contents of the specified JSON file into the parameter whose name is defined in the model variables. The parameter must be included in the specified project component. Argument | Type | Description  
---|---|---  
jsonFile | String | Name of the JSON file.  
obj | Object | Project or project component.  
      
        Engineering.SetParameterValueFromJsonCommand("c:\json\parameter.json", Â«FeederÂ»)

The following variant of the command writes the contents of the specified JSON file into the parameter whose name is transferred. The parameter must be included in the specified project component. Argument | Type | Description  
---|---|---  
jsonFile | String | Name of the JSON file.  
obj | Object | Project or project component.  
parameterName | String | Name of the parameter.  
      
        Engineering.SetParameterValueFromJsonCommand("c:\json\parameter.json", Â«FeederÂ», "MyJsonData")

[Example application](javascript:void\(0\);) [The extension of the tutorial model with additional parameters](javascript:void\(0\);)
    1. Start EEC
    2. Import the EOX file \install\Tutorial\Mechatronic\Mechatronic.eox.
    3. Create a parameter with the name JsonData and the type Map in the unit T_Mechatronic_ModularSystem.Mechatronic.Parameter. The name of the parameter must be identical with the value of the model variable Name of the parameter which stores the JSON structure.
    4. Create the parameter with the name PartName and the type String, as well the name OrderPos and the type Integer.
    5. Add the selection values 1, 2, 3 and 4 to the parameter OrderPos.
    6. Open the Feeder mechatronic component.
    7. Enter the three new parameters in the mechatronic component Feeder.
    8. Enter the following formula for the PartName parameter:
    
        =$JsonData.value('json').value('OrderItems').value(parameter('OrderPos').value().toString).select(x|x.key='PartName').values().asList().at(0)

    1. With that the tutorial model is successfully extended.
Explanation of the formula: The target of the formula is to determine the part name (PartName parameter) for a specified order position (OrderPos parameter) from 1 to 4. The expression $JsonData.value('json').value('OrderItems') accesses the read-in JSON data in the JsonData parameter and reduces them to entries within the OrderItems map. The expression .value(parameter('OrderPos').value().toString) reduces the entries to the contents of the map with the specified number in the parameter OrderPos. Since this parameter is of the type Integer, the value is converted into a string. The expression .select(x|x.key='PartName').values().asList().at(0) returns the values for the key PartName as a list and takes the first (and in this example only) entry from there. [The extension of the modular system with an action](javascript:void\(0\);)
    1. In the mechatronic modular system create a new unit called Actions.
    2. In the Actions unit create a new action called WriteJsonFileToParameterAction.
    3. Add a new method to the action.
    4. Change the name of the method from New Name to run.
    5. As the language select the method java.
    6. Add an argument.
    7. Change the name of the argument from New Argument to jsonFileName.
    8. Change the type of the argument from Engineering.Object to Engineering.String.
    9. Enter the following Java code into the Code field:
    
        import com.mind8.mechatronic.skill.*;
    import com.mind8.mechatronic.skill.eos.*;
    import com.mind8.mechatronic.skill.api.IUtilAPI;
    import org.foederal.apache.log4j.SpaceLogger;
    
    logger = SpaceLogger.getSpaceLogger("SetParameterValueFromJsonAction");
    logger.info(this, "Start logging");
    
    TypeClass.findType(self.getUnitOfWork(),"Engineering.SetParameterValueFromJsonFileCommand").perform("execute", jsonFileName);
    self.getUnitOfWork().saveChanges();

    1. Save the action.
    2. The WriteJsonFileToParameterAction action has been successfully created.
For explanation: The arguments execute and jsonFileName are transferred to the Engineering.SetParameterValueFromJsonFileCommand command. The first argument corresponds to the start method and the second argument transfers the absolute file name of the JSON File. This file name must be transferred as an argument during the action call. During the execution the contents of the JSON structure is written into the parameter, whose name is defined in the model variables (default is JsonData). The parameter must be contained in the project component of the top level (this is the Feeder component in the tutorial model). This change is saved when the JSON data has been written into the parameter. [The extension of the tutorial model with a Form-UI](javascript:void\(0\);) The user is to have the following possibilities through a Form-UI:
     * Import the JSON file on request.
     * Select a value for the order position.
     * Receive the part designation as a result.
    1. Open the Feeder mechatronic component.
    2. Change to the UI configuration editor.
    3. Change to the Source editor tab.
    4. Copy the following configuration in the editor area:
    
        <?xml version="1.0" encoding="UTF-8"?>
    <uis xmlns="http://www.mind8.com/FormUI"
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    	<form title="SetParameterFromJsonFile" id="SetParameterFromJsonFile">
    		<label>Click the button below to write the content of a JSON file to the parameter 'JsonData'.</label>
    		<action name="T_Mechatronic_ModularSystem.Actions.WriteJsonFileToParameterAction" arguments="=List{'C:\\JSON\\order.json'}" type="button" >Import JSON File</action>
    		<table columns="2">
    			<td><label>Select an order position</label></td>
    			<td><input receiver="=parameter('OrderPos')" type="combo"></input></td>
    			<td><label text="='Part name'"></label></td>
    			<td><label text="=$PartName"></label></td>
    		</table>
    	</form>
    </uis>

    1. Save the UI configuration.
    2. The Form-UI has been successfully created as a result.
[The creation of the JSON file c:\JSON\order.json](javascript:void\(0\);)
    1. Start any text editor, for example Notepad++.
    2. Insert the following JSON structure:
    
        {
    	"defaultJobName":"DemoJob",
    	"params":{
    		"OrderNo":"20211117001",
    		"OrderDate":"20211117"
    	},
    	"json":{
    		"OrderHeader":{
    			"Company":"Eplan",
    			"Address":{
    				"Street":"An der alten Ziegelei 2",
    				"ZipCode":"40789",
    				"City":"Monheim"
    			}
    		},
    		"OrderItems":{
    			"1":{
    				"PartName":"Main switch",
    				"EAN":"001356897563",
    				"Qty":"1"
    			},
    			"2":{
    				"PartName":"Fuse",
    				"EAN":"001452976326",
    				"Qty":"24"
    			},
    			"3":{
    				"PartName":"Terminal",
    				"EAN":"000556894712",
    				"Qty":"48"
    			},
    			"4":{
    				"PartName":"Wire",
    				"EAN":"00059655331",
    				"Qty":"96"
    			}
    		}
    	}
    }

    1. Save this data under the file name C:\JSON\order.json.
    2. The JSON file has been successfully created as a result.
[The tutorial model with evaluation of the read-in data structure](javascript:void\(0\);)
    1. Open the Feeder.Mechatronic.Feeder project component.
    2. Open the Form-UI SetParameterFromJsonFile.
    3. Click the button Import JSON File.
    4. For Select an order position select a value of 1 to 4 from the drop-down list.
    5. For OrderPos = 1 the Part name = Main switch is determined.
    6. For OrderPos = 2 the Part name = Fuse is determined.
    7. For OrderPos = 3 the Part name = Terminal is determined.
    8. For OrderPos = 4 the Part name = Wire is determined.
The example has been created as a result. More: [Parameter name for the JSON structure](../../../admin/Content/htm/admin_r_modelvar_commands_json.htm)
