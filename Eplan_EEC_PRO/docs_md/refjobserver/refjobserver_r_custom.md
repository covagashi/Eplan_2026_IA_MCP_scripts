---
title: "custom"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_r_custom.htm"
file: "refjobserver_r_custom"
category: "refjobserver"
---

# custom

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  custom The <custom> tag encloses tags for customer-specific definitions. The <custom> tag has to be inserted before the <actions> tag in the Job definition. Allowed sub-elements | Quantity  
---|---  
[jobStatusHtml](refjobserver_r_jobstatushtml.htm) | 1  
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
