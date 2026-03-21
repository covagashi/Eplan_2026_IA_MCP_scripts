---
title: "Perspective Job Server"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecjobserver_k_perspective_jobserver.htm"
file: "eecjobserver_k_perspective_jobserver"
category: "eecjobserver"
---

# Perspective Job Server

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

##  Perspective Job Server

Depending on whether it is being used by the Job Server or by the Worker the Perspective Job Server consists of the views Message Log, Console, Progress and the user interface of the Job Server (also see [Perspectives](eecbase_k_perspectives.htm)).

If the Perspective is used by the Worker, two buttons for controlling the Worker are located in the toolbar:

     * Start Worker : Activates the Worker, i.e. as soon as a Job exists that fulfils the file trigger or Web Service trigger of the Worker, processing is begun.
     * Stop Worker : Ends the Worker, which means that the Job currently being processed is aborted at an appropriate point. After the Job is restarted, it is not continued at the last position, but starts from the beginning.

The Worker is started automatically during the start and opens the Perspective Job Server through the Java VM argument in the initialization file (for example ec.ini) (see [de.eplan.eec.jobserver.worker.autostart](admin_r_vmargs_worker_autostart.htm)).
    
        -Dde.eplan.eec.jobserver.worker.autostart=true

You can also specify in the initialization file the language in which the user interface of the Job Server is to be started, for example German (see [-osgi.nl](admin_r_eclipse_args_nl.htm)):
    
        -Dosgi.nl=de_DE
