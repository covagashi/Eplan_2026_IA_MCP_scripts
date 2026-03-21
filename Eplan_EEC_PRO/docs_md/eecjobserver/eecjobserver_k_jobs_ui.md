---
title: "User interface of the Jobs"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecjobserver_k_jobs_ui.htm"
file: "eecjobserver_k_jobs_ui"
category: "eecjobserver"
---

# User interface of the Jobs

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## User interface of the Jobs

The user interface for the Jobs shows all the Jobs with their current status, the Job name, the associated Job definition, the Worker, who is carrying out or has carried out the Job and the actions currently possible. The number of days after which Jobs are removed is displayed below the list. Jobs that are older than the displayed number of days are removed. The number of days can be set through an entry in the initialization file (ec.ini) (see [de.eplan.eec.jobserver.cleanup.days](admin_r_vmargs_jobserver_cleanupdays.htm)).

By default, the list shows all the Jobs sorted chronologically, with the most recent ones at the top.

The entries in the list can be filtered according to Status, Priority, Job name, Job definition and Worker. The number of entries per page can be limited by using the buttons [10], [25], [50] and [100].

The list of jobs can be manipulated by means of actions. The arrangement of the jobs in the list changes through the actions:

Action/priority | Symbol | Meaning  
---|---|---  
Normal priority |  |  Every job initially has a normal priority. All jobs with the priority are processed according to the FIFO principle.  
Delete Job |  | Removes a Job from the list.  
Processed with highest priority |  |  No job is being processed currently: Moves the job to the highest position. This action moves other jobs with this priority one position downwards. A job is currently being processed: Moves the job to the position below the running job. This does not cause a running job to be aborted. This action moves other jobs with this priority one position downwards.  
Process with next highest priority |  |  No job with highest priority is available currently: Moves the job to the highest position. If this priority is assigned to further jobs, they are positioned below. A job with the highest priority is available: Moves the job to the position below a job with the highest priority. If this priority is assigned to further jobs, they are positioned below.  
Process with next lowest priority |  |  Moves the job to the lowest position. This action moves other jobs with this priority one position upwards.  
Open Job progress window |  | Opens a popup window with the progress information for the Job.  
Open Job log window |  | Opens the Job-specific log.  
  
The following statuses can be displayed for the Jobs:

Status | Symbol | Meaning  
---|---|---  
Queued |  | The Job Server has been started, the Job is located in the queue. As soon as a slot in the Job Server becomes free, the next Job in the queue is started.  
Running |  | The Job Server is executing a pending Job.  
FinishedSuccessfully |  | The Job has been completed successfully by the Job Server. The files of the Job have been copied into the agreed directory.  
FinishedInError |  | The Job Server reported an error while processing the Job. Processing has been aborted and the files of the Job have been copied into the agreed directory (see [failedFolder](refjobserver_r_failedfolder.htm)). An e-mail has been sent to predefined addresses. The contents of the error log can be inserted as a text into the e-mail (see [jobdefinition](refjobserver_r_jobdefinition.htm)).  
Cancelled |  | A Job was cancelled by the user during the execution.  
  
Additionally to these states, the job can

     * display a unique Job id,
     * display a Job name. There are two case differentiations:
       * fileTrigger: If the Job is located in the queue, the name of the file that triggered the FileTrigger is displayed. As soon as the Job leaves the queue, the Job name that is specified in the Job definition is displayed, extended by the time stamp.
       * webserviceTrigger: If the Job is located in the queue, a file name cannot be displayed. The post parameter js.queuedJobName can be used to transfer a Job name that is displayed during this state. For example, the URL http://localhost:8787/request/jobdef_web?js.queuedJobName=Job with SAP-ID: 2029338&file=C:\noscan\models\import-export-model\sample\MyProj.px is used to display the Job name Job with SAP-ID: 2029338. As soon as the Job leaves the queue, the Job name that is specified in the Job definition is displayed, extended by the time stamp.
     * List created files for the download (see [JobServer.MarkFileForDownloadCommand](refcommands_r_jobserver_markfilefordownload.htm)).
     * Own a detailed status text. This can be modified during the execution by means of a command (see [JobServer.SetProgressMessageCommand](refcommands_r_jobserver_setprogressmessagecommand.htm)).

In addition to these statuses a free status text can be output through a native command.

In addition, further information can be displayed that is created by a script during the execution of the Job and transferred to the browser.

For example, various results of the generation can be listed:

The data for the display are transferred as a Map. The API IJobAPI implements a method called getResultData() that initially returns a Map. The following Information to be displayed are to be attached to this Map.

### [Example code in Groovy](javascript:void\(0\);)
    
        import com.mind8.mechatronic.skill.api.IJobAPI;
    resultData = IJobAPI.DEFAULT.getResultData();
    data = [
    ["Station 1 Ã¼berprÃ¼ft": "Material vorhanden"],
    ["Station 2 Ã¼berprÃ¼ft": "Material nicht vorhanden"],
    ["Station 3 Ã¼berprÃ¼ft": "Material vorhanden"]
    ];
    resultData.put("MaterialÃ¼berprÃ¼fung der Stationen", data);

### Tip

In principle the method resultData.put() can process any objects. Since the transferred objects are converted into the JSON format, only simple objects such as List, Map and String should be used.

By means of a HTML file the look of the status indication is adjusted to customer-specific requirements (see [jobStatusHtml](refjobserver_r_jobstatushtml.htm)).
