---
title: "Preferences for the Job Server"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_prefs_js.htm"
file: "admin_r_prefs_js"
category: "admin"
---

# Preferences for the Job Server

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Preferences for the Job Server

Path to the preferences:

Menu Window > Preferences

Dialog Preferences > Job Server

     * A UNC path or a local path to a folder can be specified in the Repository folder field. This folder is used as basis for relative path specifications for the folders incomingFolder, outputFolder and failedFolder, as well as the folder, which contains the model (see[incomingFolder](refjobserver_r_incomingfolder.htm),[outputFolder](refjobserver_r_outputfolder.htm),[failedFolder](refjobserver_r_failedfolder.htm)and[jobdefinition](refjobserver_r_jobdefinition.htm)).

A central directory for the different storage locations of the Job Server is specified by means of the Repository folder.

If a UNC path is specified, it must be accessible both for the Job Server and for all Workers (read and write permissions). A local path can only be accessed by the Job Server and the local Workers.

Absolute path specifications for the Job Server can be made as well.

If this specification is missing and relative path specifications are provided in the job definitions, then error messages will occur.

### Note

If the Repository folder is set as a local path, jobs cannot be executed on remote Workers, but only on local Workers. So that this limitation can be recognized, this limitation is displayed at the start of the Job Server and when the job definitions are updated.
