---
title: "jobStatusHtml"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_r_jobstatushtml.htm"
file: "refjobserver_r_jobstatushtml"
category: "refjobserver"
---

# jobStatusHtml

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  jobStatusHtml Job definition The <jobStatusHtml> tag provides the name of the HTML file, which displays the customer-specific job status. If a job with WebTrigger or FileTrigger is created, the assigned HTML page is displayed in the job monitor during generation process. The path to the HTMl file assignment is always relative to the repository folder, absolute path assignments are not valid. Only the relative path can be assigned, if the HTML file has the standard name job-status.html. One example of a customer-specific presentation of the job status is the Eplan DataPortal website, which is provided by each EEC. It is located in the <EEC_Installation_Folder>install\jobserver\htmlTemplates\DataPortalTemplate folder. Attribute | Usage | Values | Default value | Description  
---|---|---|---|---  
value | required |  |  | Name of the HMTL file, which displays the customer-specific job status.  
[Code example](javascript:void\(0\);)
    
        <?xml version="1.1"?>
    <jobdefinition name="='test'+ trigger.fileName" continueOnError="false" model="models\model.eox" xmlns:xi="http://www.w3.org/2001/XInclude">
    	<fileTrigger>
    		<failedFolder value="failed" />
    		<incomingFolder value="input" />
    		<outputFolder value="output" />
    		<filter value="*.px" />
    	</fileTrigger>
    	<custom>
    		<jobStatusHtml value="html/my_status_page.html" />
    	</custom>
    	<actions>
    		<action name="T_Mechatronic_ModularSystem.Action.ImportPXAction" arguments="List{trigger.filePath}" />
    		<action name="Engineering.ExportPXCommand" arguments="List{'TestProj',trigger.additionalResultsDir + 'proj.px',true}" />
    		<action name="T_Mechatronic_ModularSystem.Action.SendMailOnEndCommand" arguments="List{trigger.outputFolder,trigger.failedFolder,trigger.jobName}" />
    	</actions>
    </jobdefinition>
