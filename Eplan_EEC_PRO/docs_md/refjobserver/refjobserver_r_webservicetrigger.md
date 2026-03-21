---
title: "webserviceTrigger"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_r_webservicetrigger.htm"
file: "refjobserver_r_webservicetrigger"
category: "refjobserver"
---

# webserviceTrigger

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  webserviceTrigger The <webserviceTrigger> tag encloses the definition for file folders for the storage of generated files. This tag has no attributes. Allowed sub-elements | Quantity | Description  
---|---|---  
jsonAlias | 1 | Defines the name of the JSON node within the transferred data.  
[outputFolder](refjobserver_r_outputfolder.htm) | 1 | Contains the generated files and a log file in case of the successful execution of a job.  
[failedFolder](refjobserver_r_failedfolder.htm) | 1 | Contains the source files and a log file in case of a failed execution of a job.  
[Example of a job definition with webserviceTrigger](javascript:void\(0\);)
    
        <?xml version='1.0' encoding='UTF-8'?>
    <jobdefinition name="myjob" model="model.eox" xmlns:xi="http://www.w3.org/2001/XInclude">
    	<webserviceTrigger>
    		<jsonAlias value="myJsonData" />
    		<outputFolder value="\output" />
    		<failedFolder value="\failed" />
    	</webserviceTrigger>
    	<actions>
    		<action name="Engineering.ImportIMXCommand" arguments="List{trigger.params.pathToIMX}" />
    		<action name="T_Mechatronic_ModularSystem.Actions.WriteJsonToParameterAction" arguments="List{trigger.json}"/>
    		<action name="Engineering.ExportEOXCommand" arguments="List{trigger.additionalResultsDir + 'Feeder.eox',List{'Feeder'}}" />
    		<action name="JobServer.MarkFileForDownloadCommand" arguments="=List{trigger.outputFolder + 'results\\Feeder.eox'}" />
    	</actions>
    </jobdefinition>

Description: This job definition is listed in the user interface of the Job Server with the name myjob. The model.eox EOX file is used as the database (see row 2). A JSON structure is not transferred with the default keyword json, but with the alias myJsonData (see row 4 in Job Definition and compare with row 10 in transferred data). The result data are located in the \output directory (see row 5). If an error occurs, the source data as well as a log are stored in the \failed directory (see row 6). The Engineering.ImportIMXCommand action imports an IMX file and thus changes data in the project (see row 8). The WriteJsonToParameterAction action writes the transferred JSON structure into a map of the JsonData parameter of the component Feeder (see row 10). With the Engineering.ExportEOXCommand action the changed project is exported as an EOX file (see row 11). The JobServer.MarkFileForDownloadCommand action ensures that the exported EOX file can be downloaded (see row 12). Data transferred via REST call (POST) for the example:
    
        {
    	"params":{
    		"pathToXslt": "C:\\Service\\JobServer\\XSL\\ParameterWithType.xsl",
    		"pathToTemplate": "C:\\Service\\JobServer\\IMX\\Template_CSV.imx",
    		"projectOrMo": "Feeder",
    		"pathToCsv": "C:\\Service\\JobServer\\CSV\\Parameter.csv",
    		"pathToIMX": "C:\\Service\\JobServer\\IMX\\T2_Extension_AllLevels.imx",
    		"delimiter": ";"
    	},
    	"myJsonData":{
    		"key1": "value1",
    		"key2": "value2",
    		"key3": "value3",
    		"key4": "value4"
    	}
    }

Result: Tip If the <failedFolder> tag is omitted, the result data are also stored in the directory that is specified in the <outputFolder> tag in case of a failure. If both the <failedFolder> and the <outputFolder> tags do not exist, no logs or result files are stored. This is used to save space when there are many Jobs and the results of the Job are transferred via the PutResultCommand with the Job status (see [JobServer.PutResultCommand](refcommands_r_jobserver_putresultcommand.htm)). The following actions can be executed by means of webserviceTrigger:
     * [Calling up jobs (without callback)](refjobserver_r_webservicetrigger_jobcall.htm)
     * [Calling up a job and placing it directly at the head of the queue](refjobserver_r_webservicetrigger_topjob.htm)
     * [Querying job status](refjobserver_r_webservicetrigger_jobstatus.htm)
     * [Call back by the Job Server](refjobserver_r_webservicetrigger_callback.htm)
     * [Downloading generated files](refjobserver_r_webservicetrigger_download.htm)
