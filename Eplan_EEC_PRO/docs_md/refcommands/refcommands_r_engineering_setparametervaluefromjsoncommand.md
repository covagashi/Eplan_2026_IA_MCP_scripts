---
title: "Engineering.SetParameterValueFromJsonCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_engineering_setparametervaluefromjsoncommand.htm"
file: "refcommands_r_engineering_setparametervaluefromjsoncommand"
category: "refcommands"
---

# Engineering.SetParameterValueFromJsonCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Engineering.SetParameterValueFromJsonCommand Note This command can only be used in the Job Server environment with webserviceTrigger. Saves the contents of a JSON structure as a map in a parameter. The JSON structure is transferred to the Job Server as POST data. The following variants are possible for using the command: The following variant of the command writes the contents of the JSON structure into the parameter whose name is defined in the model variables. The parameter must be contained in the project component of the uppermost level. Argument | Type | Description  
---|---|---  
jsonData | Object | Project or project component.  
The following variant of the command writes the contents of the JSON structure into the parameter whose name is defined in the model variables. The parameter must be included in the specified project component. Argument | Type | Description  
---|---|---  
jsonData | Object | Project or project component.  
componentPath | String | Path to the project component.  
The following variant of the command writes the contents of the JSON structure into the parameter, whose name is transferred. The parameter must be included in the specified project component. Argument | Type | Description  
---|---|---  
jsonData | Object | Map or Array  
componentPath | String | Path to the project component.  
parameterName | String | Name of the parameter.  
The following variant of the command writes the contents of the JSON structure into the parameter whose name is defined in the model variables. The parameter must be included in the specified project component. Argument | Type | Description  
---|---|---  
jsonData | Object | Map or Array  
obj | Object | Project or project component.  
The following variant of the command writes the contents of the JSON structure into the parameter, whose name is transferred. The parameter must be included in the specified project component. Argument | Type | Description  
---|---|---  
jsonData | Object | Map or Array  
obj | Object | Project or project component.  
parameterName | String | Name of the parameter.  
[Example application](javascript:void\(0\);) [A Job Server/Worker environment](javascript:void\(0\);) For the example EEC was installed with the option Stand-Alone and subsequently the optional functions for Job Server and Job Server Worker (see [Job Server with Job Server Worker installation](admin_h_installation_jobserver_worker.htm)). Perform the following work in the file system:
    1. Create the <installation folder>\model folder.
    2. Copy the <installation folder>\install\Tutorial/Mechatronic.eox file into the <installation folder>/model folder.
    3. Rename the <installation folder>/model\Mechatronik.eox file to <installation folder>\model\model.eox.
    4. Create the <installation folder>\resources\JobServer\jmx folder.
    5. Create the c:\JobServer\output folder.
Enter the following customizations in the initialization file (ec.ini): -Dorg.foederal.sn.connectionURL=proxy://initial=eox:///./model/model.eox?mode=rw -Dde.eplan.eec.jobserver.port=8686 -Dde.eplan.eec.jobserver.aliasurl=http://localhost:8686 -Dde.eplan.eec.jobserver.private.aliasurl=http://localhost:8686 -Dde.eplan.eec.jobserver.worker.port=8989 -Dde.eplan.eec.jobserver.worker.autostart=true -Dde.eplan.eec.jobserver.worker.jobdefinitionsfolder=resources\\\Jobserver\\\jmx [The extension of the modular system with an action](javascript:void\(0\);)
    1. Start EEC
    2. Switch from the Job Server perspective to the engineering perspective.
    3. Switch the database eox:///./model/model.eox?mode=rw.
    4. Create a new action called WriteJsonToParameterAction.
    5. Add a new method to the action.
    6. Change the name of the method from New Name to run.
    7. As the language select the method java.
    8. Add an argument.
    9. Change the name of the argument from New Argument to json.
    10. Change the type of the argument from Engineering.Object to Engineering.Map.
    11. Enter the following Java code into the Code field:
    
        import com.mind8.mechatronic.skill.*;
    import com.mind8.mechatronic.skill.eos.*;
    import com.mind8.mechatronic.skill.api.IUtilAPI;
    import org.foederal.apache.log4j.SpaceLogger;
    
    logger = SpaceLogger.getSpaceLogger("SetParameterValueFromJsonAction");
    logger.info(this, "Start logging");
    
    TypeClass.findType(self.getUnitOfWork(),"Engineering.SetParameterValueFromJsonCommand").perform("execute", json);
    self.getUnitOfWork().saveChanges();
    TypeClass.findType(self.getUnitOfWork(),"Engineering.ExportPXCommand").perform("execute", "Feeder", "C:\\JobServer\\output\\ProjectWithJson.px",false);

    1. Save the action.
    2. WriteJsonToParameterAction has been successfully created as a result.
For explanation: The arguments execute and json are transferred to the command Engineering.SetParameterValueFromJsonCommand. The first argument corresponds to the start method and the second argument transfers the webserviceTrigger object. During the execution, the contents of the JSON structure are written into the parameter, whose name is defined in the model variables (default is JsonData). The parameter must be contained in the project component of the top level (this is the Feeder component in the tutorial model). This change is saved when the JSON data has been written into the parameter. Subsequently the project change is exported with the command Engineering.ExportPXCommand into a file on the file system. This specification has to be adjusted, if necessary. [The creation of a Job definition with webserviceTrigger](javascript:void\(0\);) Create a Job definition having the name \resources\JobServer\JMX\readjson.jmx and the following contents:
    
        <?xml version="1.1"?>
    <jobdefinition name="readjson" model="..\..\..\model\model.eox" xmlns:xi="http://www.w3.org/2001/XInclude">
    	<webserviceTrigger>
    		<outputFolder value="..\..\..\resources\JobServer\output" />
    	</webserviceTrigger>
    	<actions>
    		<action name="T_Mechatronic_ModularSystem.Actions.WriteJsonToParameterAction" arguments="List{trigger.json}"/>
    	</actions>
    </jobdefinition>

[The extension of the modular system with additional parameters](javascript:void\(0\);)
    1. Start EEC
    2. Switch from the Job Server perspective to the engineering perspective.
    3. Create a parameter with the name JsonData and the type Map in the unit T_Mechatronic_ModularSystem.Mechatronic.Parameter.
    4. Open the Feeder mechatronic component.
    5. Insert the JsonData parameter into the Feeder component.
    6. Switch the database eox:///./eox/model.eox?mode=rw.
    7. Repeat steps 3 to 5.
    8. In addition create the parameters with the name PartName and the type String, as well as the name OrderPos and the type Integer.
    9. Add the selection values 1, 2, 3 and 4 to the parameter OrderPos.
    10. Enter these three parameters in the mechatronic component Feeder.
    11. Enter the following formula in the mechatronics component Feeder for the parameter PartName:
    
        =$JsonData.value('OrderItems').value(parameter('OrderPos').value().toString).select(x|x.key='PartName').values().asList().at(0)

    1. Switch the database eox:///./model/model.eox?mode=rw.
    2. Switch from the engineering perspective to the Job Server perspective.
    3. The modular system T_Mechatronik_ModularSystem has been successfully extended as a result.
Explanation of the formula: The target of the formula is to determine the part name (PartName parameter) for a specified order position (OrderPos parameter) from 1 to 4. The expression $JsonData.value('OrderItems') accesses the read-in JSON data in the JsonData parameter and reduces them to entries within the OrderItems map. The expression .value(parameter('OrderPos').value().toString) reduces the entries to the contents of the map with the specified number in the parameter OrderPos. Since this parameter is of the type Integer, the value is converted into a string. The expression .select(x|x.key='PartName').values().asList().at(0) returns the values for the key PartName as a list and takes the first (and only) entry from there. [The creation of a JSON structure which is transferred via webserviceTrigger to the Job Server](javascript:void\(0\);)
    1. Create the following JSON structure:
    
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

    1. Update the Job definition in the Job Server.
    2. Transfer the JSON structure by means of a RESET call to http://localhost:8686/api/request/readjson.
    3. In the Jobs view the successful execution of a Job should be listed with the Job definition readjson.
    4. The ProjectWithJson.px file should be available in the c:\JobServer\output folder.
[Importing the generated PX file](javascript:void\(0\);)
    1. Switch from the Job Server perspective to the engineering perspective.
    2. Switch the database eox:///./eox/model.eox?mode=rw.
    3. Import the configuration result of the ProjectWithJson.px file.
[The tutorial model with evaluation of the read-in data structure](javascript:void\(0\);)
    1. Open the Feeder.Mechatronic.Feeder project component.
    2. Open the Parameter editor.
    3. For the OrderPos parameter select a value of 1 to 4 from the drop-down list.
    4. For OrderPos = 1 the PartName = Main switch is determined.
    5. For OrderPos = 2 the PartName = Fuse is determined.
    6. For OrderPos = 3 the PartName = Terminal is determined.
    7. For OrderPos = 4 the PartName = Wire is determined.
The example has been created as a result. More: [Parameter name for the JSON structure](../../../admin/Content/htm/admin_r_modelvar_commands_json.htm) [webserviceTrigger](refjobserver_r_webservicetrigger.htm)
