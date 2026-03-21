---
title: "Job Server"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_installation_variant_job_server.htm"
file: "admin_r_installation_variant_job_server"
category: "admin"
---

# Job Server

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Job Server

The installation option Job Server installation is created on a workstation computer or a server.

Stand-alone installation with EOX file or EECX file for data storage:

After the installation of the application as a Stand-Alone installation on the computer, further manual installation steps are required.

Manual installation steps:

     * Install [EEC Job Server Add-On](admin_h_installation_optionalfeature_jobserver.htm).

To run the Job Server, at least three folders must be set up that can be named in any manner (the following names have been chosen freely):

     * Job definitions: This folder must also be specified as the directory for JMX files in the settings. This is where job definitions in the JMX format are stored that trigger a defined job.
     * Successful jobs: In this folder, or its subfolders, the job definition is stored, as are the data created after successfully processing a job definition.
     * Failed jobs: In this folder, or its subfolders, the job definition is stored, as are the data created after a failed processing of a job definition.

If the generation of target data requires further resources, another, random, folder must be provided for this as well.

### Note

The Job Server can be set up as a Windows server and can be run without a user interface.

### Note

Up to four Workers together with a Job Server can be run on a workstation or server to create schematics and 3D graphics with Eplan Electric P8 and Eplan Pro Panel. To do this at least four different ports have to be specified for P8 (see [Open ports for Eplan P8 connection](admin_h_maintenance_p8_port_registration.htm)).
