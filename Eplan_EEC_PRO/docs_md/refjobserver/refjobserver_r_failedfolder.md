---
title: "failedFolder"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_r_failedfolder.htm"
file: "refjobserver_r_failedfolder"
category: "refjobserver"
---

# failedFolder

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  failedFolder The <failedFolder> tag defines which file folder (also possible as UNC path) the job definition and the data that have already been created should be output to in the event of an error, for example \\\myShare\jobserver\failed. If a repository folder is specified in the settings for the Job Server or in the initialization file (for example ec.ini), the path specification is evaluated relative to the repository folder. If no repository folder is agreed, an absolute path has to be specified (see [de.eplan.eec.jobserver.worker.autostart](admin_r_vmargs_worker_autostart.htm) and [Preferences for the Job Server](admin_r_prefs_js.htm)). This specification is optional. If it is not specified, output data are not stored in case of an error. Attribute | Usage | Values | Default value | Description  
---|---|---|---|---  
value | required |  |  | Specification of the file to a folder (also possible as a UNC path). A relative path specification is possible if a path is specified for the repository folder in the user specifications or the initialization file.
