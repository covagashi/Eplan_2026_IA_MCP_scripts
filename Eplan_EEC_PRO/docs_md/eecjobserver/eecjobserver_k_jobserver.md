---
title: "Job Server and Job Server Worker"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecjobserver_k_jobserver.htm"
file: "eecjobserver_k_jobserver"
category: "eecjobserver"
---

# Job Server and Job Server Worker

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Job Server and Job Server Worker

The Job Server is used to control one or more Job Server Workers. Job Server Workers can generate files or execute long-running processes asynchronously in the configuration phase, on the basis of a model with corresponding actions and commands.

The Job Server simultaneously serves as a server for a user interface that can be accessed within the EEC through the Perspective Job Server or via a browser.

By default a Job Server Worker is installed and registered with its address at the Job Server. Further Job Server Workers can be installed and registered with their address at the Job Server. If more than one Job Server Worker is registered, the pending Jobs are executed in a distributed fashion.

The status of a Job Server Worker is always queried by the Job Server and is displayed in the user interface.

The created files of a Job can either be displayed for downloading via the user interface or be stored in an agreed folder (see [action](refjobserver_r_action.htm) and Mark file for downloading).

Each Job Server Worker delivers status information:

     * Existing Job definitions,
     * Pending Jobs,
     * Completed Jobs,
     * Aborted Jobs.
