---
title: "action"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_r_action.htm"
file: "refjobserver_r_action"
category: "refjobserver"
---

# action

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  action In a job definition, the <action> tag specifies an action that the job server is to execute. The actions are executed in the order in which they occur in the document. You can use the formula language for the arguments attribute. You can also call up static methods. To this purpose, apply the following syntax:  
      
        <action name="<class name>:<static method name>" arguments="List{<argument1>, <argument2>}" />

The tag has no sub-elements. Attribute | Usage | Values | Default value | Description  
---|---|---|---|---  
name | required |  |  | Absolute name of the action or command, e.g. T_Ecad_Ui.UpdateExtensions.  
In order to call a static method attach the name of the static method to the absolute name of the class, separated by a colon.  
arguments | required |  |  | List of arguments that are passed to the action or command. When defining the arguments, it is implied that this indicates the job object that recognizes a trigger property. You can use the formula language to determine an object as an argument.  
Use the syntax trigger.<Trigger property> to access a property of the trigger. The properties for fileTrigger, webServiceTrigger and both fileTrigger and webServiceTrigger are differentiated.  
fileTrigger:
     * trigger.currentJobId: Returns the current JobId, e.g. d366dc65-2974-4664-948c-d1736917c596.
     * trigger.fileName/trigger.getFileName: Returns the file name without extension, for example Job2010916.
     * trigger.fullFileName/trigger.getFullFileName: Returns the file name with extension, for example Job20140916.xls.
     * trigger.fileExtension/trigger.getFileExtension: Returns the file extension, for example xls.
     * trigger.filePath/trigger.getFilePath: Returns the absolute path to the file that triggered the Job processing, for example C:\input\Job20140916.xls.
WebService Trigger:
     * trigger.params/trigger.getParams: Returns the value of an URL parameter.
File Trigger and WebService Trigger:
     * trigger.additionalResultsDir/trigger.getAdditionalResultsDir: Folder for additional data, for example a PX file.
     * trigger.outputFolder/trigger.getOutputFolder: Returns the path to the defined output folder for the storage of the data in case of success.
     * trigger.failedFolder/trigger.getFailedFolder: Returns the path to the defined output folder for the storage of the data in case of failure.
     * trigger.jobName/trigger.getJobName: Returns the unique name of the Job to be executed. Consists of the value of the name attribute of the tag <jobdefinition> \+ <_TimeStamp (yyMMdd_HHmm_ssSSS)>
The formal language permits the use of regular expressions.  
[Code example](javascript:void\(0\);)
    
        <?xml version="1.1"?>
    <jobdefinition name="='test'+ trigger.fileName" continueOnError="false" model="K:\customers\2.4\64869_JobServer\JobServer\model.eox" xmlns:xi="http://www.w3.org/2001/XInclude">
    	<fileTrigger>
    		<failedFolder value="K:\customers\2.4\64869_JobServer\JobServer\error" />
    		<incomingFolder value="K:\customers\2.4\64869_JobServer\JobServer\input" />
    		<outputFolder value="K:\customers\2.4\64869_JobServer\JobServer\output" />
    		<filter value="*.px" />
    	</fileTrigger>
    	<actions>
    		<action name="T_Mechatronic_ModularSystem.Action.ImportPXAction" arguments="List{trigger.filePath}" />
    		<action name="Engineering.ExportPXCommand" arguments="List{'TestProj',trigger.additionalResultsDir + 'proj.px',true}" />
    		<action name="T_Mechatronic_ModularSystem.Action.SendMailOnEndCommand" arguments="List{trigger.outputFolder,trigger.failedFolder,trigger.jobName}" />
    	</actions>
    </jobdefinition>

[Code example for calling a static method](javascript:void\(0\);) To create a static method:
    1. Create a mechatronics component (for example StaticClass).
    2. Open the Methods editor.
    3. At least one method is added (for example setResultData).
    4. Mark the Class method check box.
    5. Select a language (for example Java).
    6. Add at least one argument (for example data).
    7. Create the code of the method to be executed in the code window.
You call up this method in a job definition as follows:
    
        <?xml version='1.0' encoding='UTF-8'?>
    	<jobdefinition name="Job Name"
    		model="/C:/jobserver/eox/basis.eox"
    		xmlns:xi='http://www.w3.org/2001/XInclude'
    		xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'
    		xsi:noNamespaceSchemaLocation='C:/jobserver/xsd/jmx.xsd'>
    	<webserviceTrigger>
    		<failedFolder value="C:/jobserver/worker/error" />
    		<outputFolder value="C:/jobserver/worker/out" />
    	</webserviceTrigger>
    	<actions>
    		<action name="T_Mechatronic_ModularSystem.Actions.StaticClass:setResultData"
    			arguments="List{'testContent'}" />
    	</actions>
    </jobdefinition>

[Code example for an action whose argument contains a formula](javascript:void\(0\);)
    
        <?xml version="1.1"?>
    <jobdefinition name="testJob" continueOnError="false" model="K:\JobServer\model.eox" xmlns:xi="http://www.w3.org/2001/XInclude">
    	<webserviceTrigger>
    		<failedFolder value="K:\JobServer\error" />
    		<outputFolder value="K:\JobServer\output" />
    	</webserviceTrigger>
    	<actions>
    		<action name="T_Mechatronic_ModularSystem.Action.ImportPXAction" arguments="List{trigger.params.value('file')}" />
    		<action name="Customizing_Engineering.SetResultDataToObjectNameAction" arguments="List{absRef('TestProj.Mechatronik.Feeder.Discard')}"/>
    		<action name="Engineering.ExportPXCommand" arguments="List{'TestProj',trigger.additionalResultsDir + 'proj.px',true}" />
    	</actions>
    </jobdefinition>

Description: With the first action (ImportPXAction) you import components and add them to the project. The second action (SetResultDataToObjectNameAction) references the name of the component that you can determine via the formula absRef('TestProj.Mechatronic.Feeder.Discard'). The name of the determined component is used for the naming of the created data. [Code example for a Job Definition whose name contains a Job ID](javascript:void\(0\);)
    
        <?xml version="1.0"?>
    <jobdefinition name="='Job1_' + trigger.currentJobId" continueOnError="true" model="E:\Users\Public\EPLAN\EngineeringConfiguration\2022_3_0_20210914-JS_W\resources\JobServer\EOX\Tutorial_JobServer.eox" xmlns:xi="http://www.w3.org/2001/XInclude">
    	<fileTrigger>
    		<failedFolder value="E:\Users\Public\EPLAN\EngineeringConfiguration\2022_3_0_20210914-JS_W\resources\JobServer\error" />
    		<incomingFolder value="E:\Users\Public\EPLAN\EngineeringConfiguration\2022_3_0_20210914-JS_W\resources\JobServer\input" />
    		<outputFolder value="E:\Users\Public\EPLAN\EngineeringConfiguration\2022_3_0_20210914-JS_W\resources\JobServer\output" />
    		<filter value="*.imx" />
    	</fileTrigger>
    	<actions>
    		<action name="Engineering.ImportIMXCommand" arguments="List{trigger.filePath}" />
    	</actions>
     </jobdefinition>

Description: For the Job name you concatenate the static string Job1_ with the dynamically generated Job ID and the obligatory timestamp with the formula ='Job1_' + trigger.currentJobId. [Code example for an action that offers the target file for downloading in the user interface](javascript:void\(0\);)
    
        <?xml version="1.1"?>
    <jobdefinition name="testJob" continueOnError="false" model="\\share\models\model.eox" xmlns:xi="http://www.w3.org/2001/XInclude">
    	<webserviceTrigger>
    		<failedFolder value="failed" />
    		<outputFolder value="output" />
    	</webserviceTrigger>
    	<actions>
    		<action name="T_Mechatronic_ModularSystem.Action.ImportPXAction" arguments="List{trigger.params.value('file')}" />
    		<action name="Customizing_Engineering.SetResultDataToObjectNameAction" arguments="List{absRef('TestProj.Mechatronik.Feeder.Discard')}"/>
    		<action name="Engineering.ExportPXCommand" arguments="List{'TestProj',trigger.additionalResultsDir + 'proj.px',true}" />
    		<action name="T_Mechatronic_ModularSystem.Commands.MarkFileForDownloadCommand" arguments="List{trigger.outputFolder + 'results\\proj1.px'}"/>
    	</actions>
    </jobdefinition>

Description: The MarkFileForDownloadCommand command creates a link to the target file of the Job. The link to the target file is displayed as a symbol in the user interface: Note The action shown in the example uses a command whose implementation has to be created self with scripting.  
The script uses the markFileForDownload method from the IJobAPI class. The method expects the path to the target file as the parameter. Example for the implementation:
    
        import com.mind8.mechatronic.skill.api.IJobAPI;
    IJobAPI.DEFAULT.markFileForDownload(pathToFile);

[Code example for saving the model data as an EOX file](javascript:void\(0\);)
    
        <?xml version="1.1"?><jobdefinition name="Job8" continueOnError="true" model="EOX\Tutorial_JobServer.eox" xmlns:xi="http://www.w3.org/2001/XInclude">
    	<fileTrigger>
    		<failedFolder value="error" />
    		<incomingFolder value="input" />
    		<outputFolder value="output" />
    		<filter value="*.imx" />
    	</fileTrigger>
    	<actions>
    		<action name="Engineering.ImportIMXCommand" arguments="=List{trigger.filePath}" />
    		<action name="Engineering.SaveObjectCommand" arguments="=List{absRef('NewFeeder.Mechatronic.Feeder')}" />
    		<action name="Engineering.ExportEOXCommand" arguments="=List{trigger.outputFolder + 'results\\Model.eox',List{'NewFeeder'}}" />
    	 	<action name="JobServer.MarkFileForDownloadCommand" arguments="=List{trigger.outputFolder + 'results\\Model.eox'}" /> 
    	</actions>
    </jobdefinition>

Description: You first back up all the model changes by using the command Engineering.SaveObjectCommand. Subsequently write the model data into an EOX file by means of the command Engineering.ExportEOXCommand. The MarkFileForDownloadCommand command creates a link to the EOX file. To offer multiple files for download, the JobServer.MarkFileForDownloadCommand has to be performed for each individual file. Note To download target files the browser has to be set so that popup windows are allowed for this application.
