---
title: "de.eplan.eec.jobserver.cleanup.days"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_jobserver_cleanupdays.htm"
file: "admin_r_vmargs_jobserver_cleanupdays"
category: "admin"
---

# de.eplan.eec.jobserver.cleanup.days

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## de.eplan.eec.jobserver.cleanup.days

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dde.eplan.eec.jobserver.cleanup.days=<number of days> |  Only for Job Server  
**Annotation**  
The EEC argument is to be used optionally only for the Job Server. The EEC Argument defines a number of days. All Jobs that are older than the specified number of days are removed. Valid values lie between 1 and 99. The default value is 30. When an invalid value is specified, the default value is used automatically. The specified number is displayed in the log view at the end of this log. Example:
    
        -Dde.eplan.eec.jobserver.cleanup.days=7
