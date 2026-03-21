---
title: "de.eplan.eec.jobserver.worker.maxconcurrentjobs"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_worker_maxconcurrentjobs.htm"
file: "admin_r_vmargs_worker_maxconcurrentjobs"
category: "admin"
---

# de.eplan.eec.jobserver.worker.maxconcurrentjobs

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## de.eplan.eec.jobserver.worker.maxconcurrentjobs

The following EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
      
        -Dde.eplan.eec.jobserver.worker.maxconcurrentjobs=<Maximale Anzahl der Threads>

|   
**Annotation**  
Specifies the maximum number of threads, that are used for execution of job definitions. The value 1 is specified for disciplines, which do not support multithreading. Valid values are within the range of 1 to 99. Example:
    
        -Dde.eplan.eec.jobserver.worker.maxconcurrentjobs=4
