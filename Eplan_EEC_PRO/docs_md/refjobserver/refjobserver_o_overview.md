---
title: "Trigger: Overview"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_o_overview.htm"
file: "refjobserver_o_overview"
category: "refjobserver"
---

# Trigger: Overview

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Trigger: Overview The following table provides an overview of all fileTriggers and webserviceTriggers that can be used in a job definition. Method | Trigger type | Usage  
---|---|---  
trigger.additionalResultsDir | fileTrigger and webserviceTrigger | Folder for additional data, for example a PX file.  
trigger.failedFolder | fileTrigger and webserviceTrigger | Returns the path to the defined output folder for the storage of the data in case of failure.  
trigger.fileExtension | fileTrigger | Returns the file extension, for example xls.  
trigger.fileName | fileTrigger | Returns the file name without extension, for example Job2010916.  
trigger.filePath | fileTrigger | Returns the absolute path to the file that triggered the job processing, for example C:\input\Job20140916.xls.  
trigger.fullFileName | fileTrigger | Returns the file name with extension, for example Job20140916.xls.  
trigger.getAdditionalResultsDir |  fileTrigger and webserviceTrigger | Folder for additional data, for example a PX file.  
trigger.getFailedFolder | fileTrigger and webserviceTrigger | Returns the path to the defined output folder for the storage of the data in case of failure.  
trigger.getFileExtension | fileTrigger | Returns the file extension, for example xls.  
trigger.getFileName | fileTrigger | Returns the file name without extension, for example Job2010916.  
trigger.getFilePath |  fileTrigger | Returns the absolute path to the file that triggered the job processing, for example C:\input\Job20140916.xls.  
trigger.getFullFileName | fileTrigger | Returns the file name with extension, for example Job20140916.xls.  
trigger.getJobName |  fileTrigger and webserviceTrigger | Returns the unique name of the Job to be executed. Consists of the value of the name attribute of the tag <jobdefinition> \+ <_TimeStamp (yyMMdd_HHmm_ssSSS)>  
trigger.getOutputFolder |  fileTrigger and webserviceTrigger | Returns the path to the defined output folder for the storage of the data in case of success.  
trigger.getParams | webserviceTrigger | Returns the value of an URL parameter.  
trigger.jobName | fileTrigger and webserviceTrigger | Returns the unique name of the Job to be executed. Consists of the value of the name attribute of the tag <jobdefinition> \+ <_TimeStamp (yyMMdd_HHmm_ssSSS)>  
trigger.outputFolder | fileTrigger and webserviceTrigger | Returns the path to the defined output folder for the storage of the data in case of success.  
trigger.params | webserviceTrigger | Returns the value of an URL parameter.
