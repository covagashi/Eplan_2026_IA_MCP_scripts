---
title: "Job Server Worker installation"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_h_installation_worker.htm"
file: "admin_h_installation_worker"
category: "admin"
---

# Job Server Worker installation

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here: 

# Job Server Worker installation

The installation of the Worker is based on the Stand-Alone installation with EOX data storage (see [Stand-Alone installation](admin_h_installation_stand_alone.htm)). The optional function (Optional Feature) for the Job Server Worker has to be installed (see [EEC Job Server Worker Add-On](admin_h_installation_optionalfeature_jobserverworker.htm)). Further settings can be made in the settings for the Worker:
     * If the Worker should start automatically after EEC has been started.
     * A directory (UNC path is possible), where the job definitions for the Worker are stored.
     * The maximum number of parallel jobs.
     * E-mail preferences, to send e-mails to particular addresses in case of successful or failed jobs.

## [Setting up a Job Server Worker as a service](javascript:void\(0\);)

The following entries in the initialization file (ec.ini) are additionally required to set up a Job Server Worker as a service:
    
        -Dde.eplan.eec.headless=true
    -Dde.eplan.eec.jobserver.worker.autostart=true

Constraints: If the Job Server Worker is set up as a service, you cannot use connected drives for job definitions and paths in the model. The Word discipline can generate the structure and the document, but it cannot update the fields nor generate and open a PDF file.
