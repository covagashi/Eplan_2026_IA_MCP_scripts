---
title: "de.eplan.eec.jobserver.repositoryfolder"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_jobserver_repositoryfolder.htm"
file: "admin_r_vmargs_jobserver_repositoryfolder"
category: "admin"
---

# de.eplan.eec.jobserver.repositoryfolder

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## de.eplan.eec.jobserver.repositoryfolder

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dde.eplan.eec.jobserver.repositoryfolder=<Path> |  Only for Job Server  
**Annotation**  
By means of repositoryfolder, a central directory for the different storage locations of the Job Server is specified. The directory can be specified as a UNC path or a local path. A UNC path is specified both for the Job Server and for all Workers (read and write permissions). A local path can only be accessed by the Job Server and the local Workers. Path specifications for incomingFolder, failedFolder, outputFolder and model in the job definitions could then be specified relative to this directory (see also [Job definitions](refjobserver_r_jobdefinitions.htm)). Absolute path specifications for the Job Server can be made as well. If this specification is missing and relative path specifications are provided in the job definitions, then error messages will occur. Example of an initialization file (e.g., ec.ini):
    
        -Dde.eplan.eec.jobserver.repositoryfolder=\\myShare\jobserver\

Resulting specifications in a job definition (extract):
    
        <fileTrigger>
    	<incomingFolder value="input" />
    	<failedFolder value="failed" />
    	<outputFolder value="output" />
    	<filter value="*.px2" />
    </fileTrigger>	  
  
### Tip

Environment variables of Windows are supported for this specification. Environment variables are enclosed by percentage signs, e.g. %WINDIR%. A percentage sign is masked by %% and can be used as part of a path specification.

Environment variables that cannot be broken up are listed in the ec.log log file and EEC terminates.

### Note

If the Repository directory is set as a local path, jobs cannot be executed on remote Workers, but only on local Workers. In order for this limitation to be recognized a warning is output in the log when the Job Server is started and when the job definitions are updated. Similarly an error message is displayed in the browser in the user interface during registration or during updating of the job definitions of a remote Worker.

### Further information

     * [Information on Job definitions](eecjobserver_k_worker_ui_jobdef.htm)
