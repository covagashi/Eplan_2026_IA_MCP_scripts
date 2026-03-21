---
title: "Status indication for Job Server Worker"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecjobserver_k_worker_ui_health.htm"
file: "eecjobserver_k_worker_ui_health"
category: "eecjobserver"
---

# Status indication for Job Server Worker

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

User interface of the Job Server Worker

## Status indication for Job Server Worker

The current state of each Job Server Worker is indicated by means of a symbol in the list of Job Server Workers. The state is queried and the display is updated by the Job Server in regular time intervals.

Symbol | Meaning  
---|---  
| The Job Server Worker is not available, for example the connection is lost or the Job Server Worker stopped. If the connection ended due to a timeout, the Job Server tries to contact the Job Server Worker again for three times with a one-second pause. After the third failed connection attempt, the Job Server Worker is indicated as not available.  
| The Job Server Worker is started and is waiting for Jobs.  
| The Job Server Worker is working on one or more Jobs.  
| The Job Server Worker is working on one or more Jobs and has no other free slots. This means that the Job Server Worker cannot accept any further Jobs, but the operation is not disrupted.  
| The Job Server Worker is working on one or more Jobs, but the connection to the Job Server is lost. The Job Server Worker is waiting for a connection after processing the Job to transmit the created data.  
  
If a Job Server Worker is unable to connect to the Job Server, then it waits until the Job Server can be reached again.

The progress display indicates this state by a plain text message:

The processing is completed after a successful connection. If the Job Server Worker is stopped, it tries to transmit the states of the completed jobs to the Job Server after the next start.
