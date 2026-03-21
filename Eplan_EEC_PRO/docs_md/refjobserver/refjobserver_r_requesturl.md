---
title: "Job execution via URL"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_r_requesturl.htm"
file: "refjobserver_r_requesturl"
category: "refjobserver"
---

# Job execution via URL

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Job execution via URL Job definition A Job can be created directly for the Job Server by means of a URL. The URL has the following syntax:
    
        http://<Job Server Host>/jobs/request/<JobDefinition>?<param1>=<value1>&<param2>=<value2>...

     * <Job Server Host>: Name and port of the Job Server.
     * <JobDefinition>: Name of the job definition file that is to be used for the Job.
     * <param1>=<value1>&<param2>=<value2>: Parameters and parameter values (key-word pairs) that can be transferred to actions within the job definition.
The URL can be created and transferred by direct input or by using a table (form post). Direct input: [Example of a URL](javascript:void\(0\);)
    
        http://localhost:8787/jobs/request/jobdef_web?file=K:\JobServer\input\MyProj.px

Description: A Job (jobdef_web) is started that uses the Web Service Trigger and that transfers the parameter file with the path K:\JobServer\input\MyProj.px to the script. As soon as the Job has been started, the Job Server receives status information about the progress: Job definition for this example:
    
        <?xml version="1.0"?>
    <jobdefinition name="testJob" continueOnError="false" model="K:\JobServer\model.eox" xmlns:xi="http://www.w3.org/2001/XInclude">
    	<webserviceTrigger>
    		<failedFolder value="K:\JobServer\error" />
    		<outputFolder value="K:\JobServer\output" />
    	</webserviceTrigger>
    	<actions>
    		<action name="T_Mechatronic_ModularSystem.Action.ImportPXAction" arguments="List{trigger.params.file}" />
    		<action name="Engineering.ExportPXCommand" arguments="List{'TestProj',trigger.additionalResultsDir + 'proj.px',true}" />
    		<action name="Customizing_Engineering.SetResultDataAction"/>
    	</actions>
    </jobdefinition>

Generation by using an HTML form (Post Method): The table is provided as an HTML file. The content consists of key-value pairs that are located in two columns. [Example of an HTML table](javascript:void\(0\);)
    
        <html>
    	<body>
    		<h1>Configuration</h1>
    			<form action="http://jobserver:8686/jobs/request/jobdef5" method="post">
    				<table>
    					<tr>
    						<td>EAN</td>
    						<td><input type="text" name="EAN" value="4016779578639" /></td>
    					</tr>
    					<tr>
    						<td>Weight</td>
    						<td><input type="text" name="Weight" value="4000" /></td>
    					</tr>
    					<tr>
    						<td>MaxSpeed</td>
    						<td><input type="text" name="MaxSpeed" value="240" /></td>
    					</tr>
    					<tr>
    						<td>MaxFunctiongroups</td>
    						<td><input type="text" name="MaxFunctiongroups" value="5" /></td>
    					</tr>
    					<tr>
    						<td>Option</td>
    						<td><input type="text" name="Option" value="Inspect" /></td>
    					</tr>
    					<tr>
    						<td>js.queuedJobName</td>
    						<td><input type="text" name="js.queuedJobName5" value="Job_5" /></td>
    					</tr>
    				</table>
    			<input type="submit" value="Post job" />
    		</form>
    	</body>
    </html>

Description: The form is enveloped by the tag <form>. The attribute action specifies the URL of the Job definition in the Job Server that is to be used. In order to transfer the table as form post, the attribute method is specified with the value post. Within the tag <forms>, <input> tags are used to define any number of parameters with their values. These are transferred as trigger.params to the Server side. For example the name EAN with the value 4016779578639 becomes params.EAN=4016779578639. The tag <input> with the attribute type="submit" creates a button in order to create a Job in the queue of the Job Server. If the Job status is to be queried, the usual means can also be used here (see install\htmlTemplates\DataPortalTemplate). The table for the new configuration has the following appearance in a browser: Several <input> fields can also have the same name. The trigger.params then includes a key with the name and all the values are separated there as a string with \t.
