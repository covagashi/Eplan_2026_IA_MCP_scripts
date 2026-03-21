---
title: "Information on Job definitions"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecjobserver_k_worker_ui_jobdef.htm"
file: "eecjobserver_k_worker_ui_jobdef"
category: "eecjobserver"
---

# Information on Job definitions

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Information on Job definitions

The Workers tab contains a list of job definition names. Multiple Workers may have job definitions with identical names, which then must have the same content. This ensures, that each Worker creates the same result for a specific job.

Colored marker beside the name of the job definitions have the following meaning:

     * Yellow marker indicate, that two ore more job definitions with the same name exist, which differ in content.
     * Red maker indicate errors in the job definition, which prevent job execution.

By means of the > symbol, the detailed information on a job definition are unfolded.

If the input folder, base model, output folder, failed folder and the job status html are specified as UNC paths, then these entries are used as links. This feature is supported by the following browsers:

     * Firefox (only with plugins)
     * Chrome (only with plugins)

If two or more Worker have job definitions with identical names, but different content, it is indicated by a yellow marker beside the job definition name. The difference between the first job definition, which operates as reference and the following job definition is indicated by a yellow exclamation sign. The tooltip displays the expected specification.

An error in the job definition is indicated by a red exclamation sign. By clicking the exclamation sign, detailed information on the error is displayed.

The information on a job definition are logged and displayed in the user interface of the logs (see [User interface of the Logs](eecjobserver_k_logs_ui.htm)).

Job definitions, which contain errors, are logged as errors, error-free job definitions as details.

### Note

If an error occurs during the initialization of Eplan Electric P8, the associated job definition is disabled. The failed job is marked accordingly.
