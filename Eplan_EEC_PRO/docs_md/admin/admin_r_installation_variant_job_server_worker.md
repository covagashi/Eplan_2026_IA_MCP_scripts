---
title: "Job Server with Worker"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_installation_variant_job_server_worker.htm"
file: "admin_r_installation_variant_job_server_worker"
category: "admin"
---

# Job Server with Worker

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Job Server with Worker

The installation option Job Server with Worker is created on a workstation computer or a server. The Job Server and Worker run in a joint process. If a restart of the Job Server is required, the Worker is also restarted and the other way around.

Stand-alone installation with EOX file or EECX file for data storage:

After the installation of the application as a Stand-Alone installation on the computer, further manual installation steps are required.

Manual installation steps:

     * Install [EEC Job Server Add-On](admin_h_installation_optionalfeature_jobserver.htm).
     * Install [EEC Job Server Worker Add-On](admin_h_installation_optionalfeature_jobserverworker.htm).

To run the Job Server with Worker, at least three folders must be set up that can be named freely (the following names have been chosen freely):

     * Job definitions: This folder must also be specified as the directory for JMX files in the settings. This is where job definitions in the JMX format are stored that trigger a defined job.
     * Successful jobs: In this folder, or its subfolders, the job definition is stored, as are the data created after successfully processing a job definition.
     * Failed jobs: In this folder, or its subfolders, the job definition is stored, as are the data created after a failed processing of a job definition.

If the generation of target data requires further resources, another, random, folder must be provided for this as well.

The Job Server with Worker can be set up as a Windows service and can be run without a user interface.
