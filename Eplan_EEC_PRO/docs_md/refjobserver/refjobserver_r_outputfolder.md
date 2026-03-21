---
title: "outputFolder"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_r_outputfolder.htm"
file: "refjobserver_r_outputfolder"
category: "refjobserver"
---

# outputFolder

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  outputFolder The <outputFolder> tag defines which file folder (also possible as UNC path) the job definition and the created data should be output to in the event of success, for example \\\myShare\jobserver\outgoing. If a repository folder is specified in the settings for the Job Server or in the initialization file (for example ec.ini), the path specification is evaluated relative to the repository folder. If no repository folder is agreed, an absolute path has to be specified (see [de.eplan.eec.jobserver.worker.autostart](admin_r_vmargs_worker_autostart.htm) and [Preferences for the Job Server](admin_r_prefs_js.htm)). This specification is optional. If it is not specified, output data are not stored in the event of success. The specification outputFolder is required for the registration of files for downloading (see [JobServer.MarkFileForDownloadCommand](refcommands_r_jobserver_markfilefordownload.htm)). Attribute | Usage | Values | Default value | Description  
---|---|---|---|---  
value | required |  |  | Specification of the file to a folder (also possible as a UNC path). A relative path specification is possible if a path is specified for the repository folder in the user specifications or the initialization file.
