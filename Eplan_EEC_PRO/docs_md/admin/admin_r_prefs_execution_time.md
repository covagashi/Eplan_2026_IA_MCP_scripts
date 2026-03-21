---
title: "Settings for profiling"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_prefs_execution_time.htm"
file: "admin_r_prefs_execution_time"
category: "admin"
---

# Settings for profiling

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Settings for profiling

Path to the settings:

Menu Window > Settings

Dialog Settings > Formulas > Profiling

If the Enable performance measurement option is selected, all the performances that exceed a specific threshold are logged.

A time value that has to be exceeded by a performance in order to log it is to be specified in the Performance measurement threshold (ms) field. 10 ms are specified as the default value. An execution is logged in the workspace\\.metadata\Formulatrace_<running number>.csv file if it is exceeded, for example workspace\\.metadata\Formulatrace_0.csv.

Each log entry contains the name of the object (Object), the name of the parameter (Parameter), the formula (Formula), the execution time (ExecutionTime) and the calculation time (ComputationTime).
