---
title: "JobServer.MarkFileForDownloadCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_jobserver_markfilefordownload.htm"
file: "refcommands_r_jobserver_markfilefordownload"
category: "refcommands"
---

# JobServer.MarkFileForDownloadCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  JobServer.MarkFileForDownloadCommand Only for Job Server. Marks the specified file for downloading. When a Job has been completed, the marked files can be downloaded via the user interface of the Job Server (see also [action](refjobserver_r_action.htm) \- Example code for an action that offers the target file for downloading in the user interface). URLs transferred with the argument pathToFile are simply passed through. By contrast, transferred files are stored in the outputFolder of the Repository directory. Argument |  Type |  Description  
---|---|---  
pathToFile |  String |  Path or URL to the file that is to be marked for downloading. The protocols http and https are supported for URLs.  
Read more
     * [de.eplan.eec.jobserver.repositoryfolder](admin_r_vmargs_jobserver_repositoryfolder.htm)
     * [outputFolder](refjobserver_r_outputfolder.htm)
