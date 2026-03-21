---
title: "User interface of the Job Server Worker"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecjobserver_k_worker_ui.htm"
file: "eecjobserver_k_worker_ui"
category: "eecjobserver"
---

# User interface of the Job Server Worker

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## User interface of the Job Server Worker

In the Workers category of the Job Server perspective a list of all registered Job Server Workers is displayed.

The identically view is displayed in a browser. Therefore the URL shown in the address field of the Job Server perspective is copied to the browsers address field.

Each worker automatically registers in the initialization file via specification of de.eplan.jobserver.private.aliasURL at the Job Server (see [de.eplan.eec.jobserver.aliasurl](admin_r_vmargs_jobserver_aliasurl.htm)).

Each registered Job Server Worker is displayed in a tab with its status, name, its address and its Job definitions (see also [Status indication for Job Server Worker](eecjobserver_k_worker_ui_health.htm)).

The list of job definitions of all the registered Job Server Workers is updated by using [Update job definitions]. If a Job Server Worker can not be reached at this time (for example offline), this is indicated by a message for a limited time. The list of Job definitions is also updated when the Job Server or the Job Server Worker is restarted.

Details of a Job definition are displayed when expanding the Job definition (see [Information on Job definitions](eecjobserver_k_worker_ui_jobdef.htm)).

An existing job definition can be deleted from the Job Server Worker by using [Remove].

### [Uploading a job definition to a Job Server Worker](javascript:void\(0\);)

Use the [Upload] button to upload a job definition to a connected Job Server Worker. In the process an existing job definition of the same name is updated.

The job definition is then available immediately.

### [Uploading a job definition to several Job Server Workers](javascript:void\(0\);)

A job definition can be updated on the Job Server by using the [Replace JMX] button and can be distributed from the Job Server to all Job Server Workers on which the job definition of the same name exists.

### Note

A job definition must be created in the UTF-8 without BOM format.
