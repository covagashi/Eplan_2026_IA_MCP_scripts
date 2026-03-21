---
title: "incomingFolder"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_r_incomingfolder.htm"
file: "refjobserver_r_incomingfolder"
category: "refjobserver"
---

# incomingFolder

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  incomingFolder Job definition The <incomingFolder> tag defines the file folder (also possible as UNC path) into which the import data for the job to be executed with File Trigger are to be stored, for example \\\myShare\jobserver\incoming. If a repository folder is specified in the settings for the Job Server or in the initialization file (for example ec.ini), the path specification is evaluated relative to the repository folder. If no repository folder is agreed, an absolute path has to be specified (see [de.eplan.eec.jobserver.worker.autostart](admin_r_vmargs_worker_autostart.htm) and [Preferences for the Job Server](admin_r_prefs_js.htm)). Attribute | Usage | Values | Default value | Description  
---|---|---|---|---  
value | required |  |  | Specification of the file to a folder (also possible as a UNC path). A relative path specification is possible if a path is specified for the repository folder in the user specifications or the initialization file.  
Note Blocked files (for example DOCX files that are still being processed in an active Word process) are ignored until they are no longer blocked. Hidden files are ignored.
