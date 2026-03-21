---
title: "Preferences for the Job Server Worker"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_prefs_js_worker.htm"
file: "admin_r_prefs_js_worker"
category: "admin"
---

# Preferences for the Job Server Worker

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Preferences for the Job Server Worker

The preferences for the Worker set up the following:

     * The starting behavior of the Worker.
     * The file folder where job definitions for this Worker are stored.
     * The maximum number of parallel jobs.

### Note

The preferences for a Worker can only be changed

     * When the Worker is not processing a Job.
     * When the Worker is stopped.

Path to the preferences:

Menu Window > Preferences

Dialog Preferences > Job Server > Job Server Worker

     * The Automatic Worker startup option specifies that the Worker is started automatically when EEC is started and that the Job Server perspective is displayed. If the input folder contains files that correspond to the file trigger, the Job Server immediately begins to process them.
     * A file folder where the job definitions for this Worker are stored is specified in the JMX file folder field. The folder may be specified as UNC path, e.g., \\\myShare\jobserver\jobdefinitions.
     * The maximum number of jobs to be processed in parallel is specified in the Maximum number of parallel jobs field. Possible values are within the range of positive integers.

### [Example](javascript:void\(0\);)

There are 3 jobs in the input folder and all files needed for the jobs are also present. The Worker should start up immediately at EEC startup and the number of parallel jobs is set to 2.

Flow:

The Worker starts up automatically at EEC startup and the parallel processing of 2 jobs is started immediately. Then the third job is processed by itself.

### Note

Information about the supported version of Eplan Electric P8 and ProPanel is available under the[Software and hardware requirements](admin_r_it_reqs_software.htm).

The Automatic Job Server startup and Maximum number of parallel jobs preferences can also be specified in the initialization file, for example, ec.ini (see[de.eplan.eec.jobserver.worker.autostart](admin_r_vmargs_worker_autostart.htm)and[de.eplan.eec.jobserver.worker.maxconcurrentjobs](admin_r_vmargs_worker_maxconcurrentjobs.htm)). The values specified in the initialization file overrule the values of the preferences. If the initialization file contains a value, this is displayed in the preferences.
