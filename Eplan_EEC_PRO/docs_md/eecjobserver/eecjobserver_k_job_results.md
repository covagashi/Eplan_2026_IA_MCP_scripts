---
title: "Storing created files"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecjobserver_k_job_results.htm"
file: "eecjobserver_k_job_results"
category: "eecjobserver"
---

# Storing created files

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Storing created files

The created files of a Job are stored in a folder that is specified in the job definition (see [Job definitions](refjobserver_r_jobdefinitions.htm)). A distinction is made as to whether the job was completed successfully or whether an error has occurred.

### Note

The Job Server generally works on the basis of a model that is specified as an EOX file.

The Job Server only has read rights for the EOX file.

To save the changed model data, execute the command [Engineering.SaveObjectCommand](refcommands_r_engineering_saveobjectcommand.htm) and then export by using the command [Engineering.ExportEOXCommand](refcommands_r_engineering_exporteoxcommand.htm) as an EOX file. The exported EOX file can be offered for download with the command [JobServer.MarkFileForDownloadCommand](refcommands_r_jobserver_markfilefordownload.htm).

The commands have to be declared as [action](refjobserver_r_action.htm) in the job definition.

Below the folders specified, the Worker creates for each job a subfolder with the name of the job, followed by the timestamp.

### [Example](javascript:void\(0\);)
    
        \\myShare\jobserver\Out\Job1234_1_140827_1523_55119\1234_Project.jmx

If the job instantiates a project, a result folder with subfolders for each instantiated project will be created below this folder. The name of the subfolder corresponds to the name of the project.

### [Example](javascript:void\(0\);)
    
        \\myShare\jobserver\Out\Job1234_1_140827_1523_55119\results\1234_Project_1
    \\myShare\jobserver\Out\Job1234_1_140827_1523_55119\results\1234_Project_2

If the job creates target data for a discipline, they will be stored in subfolders named after the disciplines.

### [Example](javascript:void\(0\);)
    
        \\myShare\jobserver\Out\Job1234_1_140827_1523_55119\results\Project_1\BOM\BOM1.txt
    \\myShare\jobserver\Out\Job1234_1_140827_1523_55119\results\Project_1\P8\Feeder.elk

Automatic deleting of files

The Job Server disposes of a time-controlled service for removing files. The service continuously deletes the following files and data whose moment of editing is older than 30 days:

     * Generated files of a Job.
     * All the log entries belonging to a Job.
