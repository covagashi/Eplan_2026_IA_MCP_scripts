---
title: "jobdefinition"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_r_jobdefinition.htm"
file: "refjobserver_r_jobdefinition"
category: "refjobserver"
---

# jobdefinition

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  jobdefinition The tag <jobdefinition> is the top-level element. All other tags are contained within this element. Attribute | Usage | Values | Default value | Description  
---|---|---|---|---  
failedMailRecipients | optional | <mail address>,<mail address> |  | In the event of an error, e-mails are sent to these addresses. Additional addresses should be separated by commas.  
globalMutex | optional | <mutex name> |  | Name of a globalMutex. This type of Mutex prevents the parallel execution of Jobs with a globalMutex of the same name across all Workers.  
model | required | <path to eox file> |  |  UNC path to EOX or EECX file of the basic model. A relative path specification is possible if a path is specified for the repository folder in the user specifications or the initialization file. If this specification is missing, the path to the JMX file is used instead. The path to the model can also be specified with a formula as =trigger.filePath. Then a search is carried out for an EON or EECX file in the incomingFolder. A corresponding filter has to be set for this purpose. If a webTrigger is specified with the formula =trigger.params.<model parameter>, the path to the EON or EECX file has to be specified as a parameter in the Web call.  
name | required | <job name> |  | Name of the job. If the name is defined by means of a formula, the name can be combined dynamically with the extension trigger.fileName into a name including job file name or with the extension trigger.currentJobId dynamically into a name including JobId.  
priority | optional |  lowPriorityJob, highPriorityJob, highestPriorityJob | No specification on priority | The priority is taken into consideration when a job is started. The priority of a job is displayed in the user interface of the Worker.  
successMailRecipients | optional | <mail address>,<mail address> |  | In the event of success, e-mails are sent to these addresses. Additional addresses should be separated by commas.  
workerMutex | optional | <mutex name> |  | Name of a workerMutex. This type of Mutex prevents the parallel execution of Jobs with a workerMutex of the same name on the same Worker.  
xmlns:xi | required if not specified in the <xi:include> tag |  http://www.w3.org/2001/XInclude |  | Namespace extension to facilitate use of xi:include  
Allowed sub-elements | Quantity  
---|---  
[fileTrigger](refjobserver_r_filetrigger.htm) | 1  
[webserviceTrigger](refjobserver_r_webservicetrigger.htm) | 1  
[actions](refjobserver_r_actions.htm) | 1  
[custom](refjobserver_r_custom.htm) | 1  
Note In the event of success or failure, e-mails can be sent to predetermined addresses. This is only possible when the Send mails on success check box or the Send mails on failure check box is selected and values that are valid for the SMTP server have been entered. Job designation: The job name actually combines the value of the Name attribute with the time stamp (Local Time of the Job Server), e.g. "_140805_1544_01000", where the 1000 represents the number of milliseconds that have elapsed since the previous minute. This ensures that each job name is unique. In this case (see the above definition) the list of jobs (e.g. as sub-folders containing job results, definition, UMC logs) would appear as follows: File_Werk1_140805_1544_00012 File_Werk1_140805_1546_56435 File_Werk2_140805_1546_03455 [Job definition with model in EOX format](javascript:void\(0\);)
    
        <?xml version="1.1"?>
    <jobdefinition name="='test'+ trigger.fileName" model="models\model.eox" xmlns:xi="http://www.w3.org/2001/XInclude" priority="highPriorityJob" >
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

Example of a Job definition that specifies the storage location for the basic model via fileTrigger: [Job definition with dynamic specification of the basic model via fileTrigger](javascript:void\(0\);)
    
        <?xml version="1.1"?>
    <jobdefinition name="='test'+ trigger.fileName" model="=trigger.filePath" xmlns:xi="http://www.w3.org/2001/XInclude" priority="highestPriorityJob" >
    	<fileTrigger>
    		<failedFolder value="failed" />
    		<incomingFolder value="input" />
    		<outputFolder value="output" />
    		<filter value="*.eox" />
    	</fileTrigger>
    	<actions>
    		<action name="UtilLib.Do"/>
    	</actions>
    </jobdefinition>

Description: The attribute model="=trigger.filePath" in the tag <jobdefinition> does not specify a model file directly. Rather, this has to be located in the file that is specified with the tag <incomingFolder>. The file type is specified with the tag <filter>. In this case a search for an EON file is carried out. Example of a Job definition that specifies the storage location for the basic model via webserviceTrigger: [Job definition with dynamic specification of the basic model via webserviceTrigger](javascript:void\(0\);)
    
        <?xml version="1.1"?>
    <jobdefinition name="='test'+ trigger.fileName" model="=trigger.params.model" xmlns:xi="http://www.w3.org/2001/XInclude" priority="lowPriorityJob" >
    	<webserviceTrigger>
    		<failedFolder value="failed" />
    		<outputFolder value="output" />
    	</webserviceTrigger>
    	<actions>
    		<action name="UtilLib.Do"/>
    	</actions>
    </jobdefinition>

Description: The attribute model="=trigger.params.model" in the tag <jobdefinition> does not specify a model file directly. Rather, this is passed as the parameter model via Web call. Example of a call:
    
        http://localhost:8787/jobs/request/jobdef_web?model=K:\JobServer\input\feeder.eox

Example of a Job definition with webserviceTrigger in order to name Jobs differently depending on the call: [Job definition with dynamic specification of the Job name via webserviceTrigger](javascript:void\(0\);)
    
        <?xml version="1.1"?>
    <jobdefinition name="='Conveyor_'
    +	if((trigger.params.belt).size>0).ifEmptyNullOrError(false)
    					then 'Belt_' + trigger.params.belt + '_'
    					else ''
    					endif
    +	if((trigger.params.roller).size>0).ifEmptyNullOrError(false)
    					then 'Roller_' + trigger.params.roller + '_'
    					else ''
    					endif
    +	if((trigger.params.chain).size>0).ifEmptyNullOrError(false)
    					then 'Chain_' + trigger.params.chain + '_'
    					else ''
    					endif"
    	continueOnError="false" 
    	model="WebShop.eecx" 
    	xmlns:xi="http://www.w3.org/2001/XInclude"
    	priority="highPriorityJob" >
    	<webserviceTrigger>
    		<failedFolder value="failed" />
    		<outputFolder value="output" />
    	</webserviceTrigger>
    	<actions>
    		<action name="JobServerActions.WebShopCall"
    		arguments="List{trigger.params, 
    				trigger.jobName, 
    				trigger.outputFolder, 
    				trigger.failedFolder}"/>
    	</actions>
    </jobdefinition>

Description: The Job name is displayed in the Job list depending on the transferred parameter. To this purpose a query with conditions that compiles the Job name differently from fragments s inserted in the <jobdefinition> tag. Possible variants are:
     * Conveyor_Belt_<Job-ID>_POS_<Position>_<Time stamp>
     * Conveyor_Roller_<Job-ID>_POS_<Position>_<Time stamp>
     * Conveyor_Chain_<Job-ID>_POS_<Position>_<Time stamp>
Exclude parallel execution of Jobs If the Maximum number of parallel Jobs is set to a value greater than 1 in the settings, several Jobs can be executed parallel. However, for specific Jobs, parallel execution cannot be allowed and it must be possible to exclude it. Mutual exclusion is generally abbreviated as Mutex. The parallel execution of Jobs can be excluded in two levels through the attributes workerMutex and globalMutex.
     * The workerMutex ensures that Jobs for the same Job definition are not executed parallel on one Worker. The workerMutex is always to be used when mutual resources of a Worker may not be used parallel, for example P8. This causes these Jobs to be executed sequentially. Jobs for Job definitions without workerMutex or other workerMutex continue to be executed parallel.
     * The definition of a globalMutex ensures that a Job for the same Job definition is not executed parallel across all the Workers. The globalMutex is always to be used when mutual resources for all the Workers may not be used parallel, for example at writing database accesses. This causes these Jobs to be executed sequentially. Jobs for Job definitions without globalMutex or other globalMutex continue to be executed parallel.
[Job definition with workerMutex](javascript:void\(0\);)
    
        <?xml version="1.1"?>
    <jobdefinition name="Generate_P8" workerMutex="P8" model="model.eox" xmlns:xi="http://www.w3.org/2001/XInclude">
    	<webserviceTrigger>
    		<outputFolder value="\output" />
    	</webserviceTrigger>
    	<actions>
    		...
    	</actions>
    </jobdefinition>

[Job definition with globalMutex](javascript:void\(0\);)
    
        <?xml version="1.1"?>
    <jobdefinition name="WriteToDb" globalMutex="DB" model="models\model.eox" xmlns:xi="http://www.w3.org/2001/XInclude">
    	<fileTrigger>
    		<failedFolder value="failed" />
    		<incomingFolder value="input" />
    		<outputFolder value="output" />
    		<filter value="*.px" />
    	</fileTrigger>
    	<actions>
    		...
    	</actions>
    </jobdefinition>
