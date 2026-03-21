---
title: "Job Server Worker"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecjobserver_k_worker.htm"
file: "eecjobserver_k_worker"
category: "eecjobserver"
---

# Job Server Worker

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Job Server Worker

An EEC with activated Worker plugin on the same computer on which the Job Server is also installed is called a Local Worker. If the installation with activated Job Server Worker plugin is on a different computer, it is called a Remote Worker.

The following figure shows the Job Server Worker variants.

Job Server Workers can generate files or execute long-running processes asynchronously in the configuration phase, on the basis of a model with corresponding actions and commands. These processes are called Jobs below.

The Job Server assigns the Jobs to be processed to registered Job Server Workers. Job Server Workers are registered automatically at a Job Server. For automatic registration a corresponding entry has to be carried out in the initialization file (see [de.eplan.eec.jobserver.aliasurl](admin_r_vmargs_jobserver_aliasurl.htm)).

The initial bases for the Jobs to be processed are so-called Job definitions (see [Job definitions](refjobserver_r_jobdefinitions.htm)). Job definitions are XML files with the extension .JMX.

A folder in which the Job definitions are stored has to be specified in the settings for each Job Server Worker (see [Preferences for the Job Server Worker](admin_r_prefs_js_worker.htm)).

The Job Server Worker reads these Job definitions in once at the start. Reading in of the Job definitions can be triggered manually through the user interface of the Job Server and of the Job Server Worker.

A Job definition always contains the following specifications:

     * Name of the Job definition.
     * Name of the model.
     * Type of the trigger that triggers a Job (for example the file extension .px).
     * Directory specification for storing the created files in case of success and failure.
     * Names of actions or commands that are to be executed for a Job.

Depending on the contents of the Job definition, the Job Server Worker expects either a file with a defined file extension in an incoming folder (File Trigger) or a specification within the calling URL (Web Service Trigger) to start a Job (see [action](refjobserver_r_action.htm)).

If several files are contained in an incoming folder in the case of a File Trigger, the files are processed in their chronological order (FIFO principle).

The data created are stored in a folder, which is also specified in the job definition (see [Storing created files](eecjobserver_k_job_results.htm) and [Job definitions](refjobserver_r_jobdefinitions.htm)).
