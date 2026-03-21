---
title: "Job Server with Job Server Worker installation"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_h_installation_jobserver_worker.htm"
file: "admin_h_installation_jobserver_worker"
category: "admin"
---

# Job Server with Job Server Worker installation

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Job Server with Job Server Worker installation

The installation of the Job Server with Worker is based on the Stand-Alone installation (see [Stand-Alone installation](admin_h_installation_stand_alone.htm)).

The optional functions (Optional Features) for the Job Server and Job Server Worker have to be installed (see [EEC Job Server Add-On](admin_h_installation_optionalfeature_jobserver.htm) and [EEC Job Server Worker Add-On](admin_h_installation_optionalfeature_jobserverworker.htm)).

To enable the Job Server to communicate with the Workers, the initialization file (for example ec.ini) should contain an argument with the Port number, where the Job Server listens, for example 8686 (see [de.eplan.eec.jobserver.port](admin_r_vmargs_jobserver_port.htm)):
    
    
    -Dde.eplan.eec.jobserver.port=8686

### Note

The specifications for -Dde.eplan.eec.jobsrever.port and -Dde.eplan.eec.jobserver.aliasurl should match so that the communication between the administration website and the Job Server is ensured. The port specifications can be different when a reverse proxy is interconnected.

Example scenario for different port specifications:

The Job Server has the settings de.eplan.eec.jobserver.port=80 and ‑Dde.eplan.eec.jobserver.aliasurl=https://www.company.de (port number 443 is the default).

A reverse proxy transfers the HTTPS request to the Job Server with http://www.company.de (port number 80 is the default).

In order to make the Job Server accessible for Workers, the initialization file (for example ec.ini) has to contain a private.aliasurl entry, for example http://jobserverstation:8686 (see [de.eplan.eec.jobserver.private.aliasurl](admin_r_vmargs_jobserver_privatealiasurl.htm)). Workers that also have this address entered in the initialization file (for example ec.ini) can register themselves automatically during the start:
    
    
    -Dde.eplan.eec.jobserver.private.aliasurl=http://jobserverstation:8686

In order to make the Job Server accessible for clients (for example browsers), the initialization file (for example ec.ini) can contain the aliasUrl argument, for example http://jobserverstation:8686 (see [de.eplan.eec.jobserver.aliasurl](admin_r_vmargs_jobserver_aliasurl.htm)).
    
    
    -Dde.eplan.eec.jobserver.aliasurl=http://jobserverstation:8686

To enable the Job Server to receive queries from Workers the initialization file (for example ec.ini) should contain an argument with the Port number, where the Worker listens, for example 8989 (see [de.eplan.eec.jobserver.worker.port](admin_r_vmargs_worker_port.htm)):
    
    
    -Dde.eplan.eec.jobserver.worker.port=8989

The Worker is started automatically when EEC is started, if the value for autostart is set to the value true in the initialization file (for example ec.ini) (see [de.eplan.eec.jobserver.worker.autostart](admin_r_vmargs_worker_autostart.htm)):
    
    
    -Dde.eplan.eec.jobserver.worker.autostart=true

You can also specify in the initialization file the language in which the user interface of the Worker is to be started, for example German (see [-osgi.nl](admin_r_eclipse_args_nl.htm)):
    
    
    -Dosgi.nl=de_DE

Further settings can be made in the settings for the Worker:

  * A directory (UNC path is possible), where the job definitions for the Worker are stored.
  * The maximum number of parallel jobs.
  * E-mail preferences, to send e-mails to particular addresses in case of successful or failed jobs.
