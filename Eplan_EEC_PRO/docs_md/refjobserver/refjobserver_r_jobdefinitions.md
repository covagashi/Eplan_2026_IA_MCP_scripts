---
title: "Job definitions"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_r_jobdefinitions.htm"
file: "refjobserver_r_jobdefinitions"
category: "refjobserver"
---

# Job definitions

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Job definitions Job definitions are XML files with .JMX file extensions. They describe what commands, respectively actions have to be performed by the Worker in order to create a new project or to create target data from them. This chapter describes the structure of the job definition and the individual tags it employs. [Example of a job definition](javascript:void\(0\);)
    
        <?xml version="1.0" encoding="UTF-8"?>
    <jobdefinition name="='testJob_' + trigger.fileName" 
    	model="C:Users\public\EPLAN\base.eox" 
    	successMailRecipients="Me@MyCompany.com,MyDepartmentManager@MyCompany.com" 
    	failedMailRecipients="Me@MyCompany.com,MyDepartmentManager@MyCompany.com">
    	<custom>
    		<jobStatusHtml value="/hmtl/my_status_page.html" />
    	<custom>
    	<actions>
    		<action name="Engineering.ImportIMXCommand" arguments="List{'project.imx'}" />
    		<action name="T_Ecad_Ui.UpdateExtensions" arguments="List{absRef('Feeder.Mechatronic')}"/>
    		<action name="Engineering.ImportIMXCommand" arguments="List{'project2.imx'}" />
    		<xi:include xmlns:xi="http://www.w3.org/2001/XInclude" href="includedJobDef.xml"/>
    	</actions>
    </jobdefinition>
