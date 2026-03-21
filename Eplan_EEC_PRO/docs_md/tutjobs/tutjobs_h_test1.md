---
title: "Test 1 - Creating a configuration"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutjobs_h_test1.htm"
file: "tutjobs_h_test1"
category: "tutjobs"
---

# Test 1 - Creating a configuration

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Tutorial Test 1 - Creating a configuration Requirements:
     * EEC as a Job Server with Worker installation Version 2.5.1 or higher.
     * Job Server is started.
     * The Job Server perspective is opened.
The first test is intended to show that the Job definition has been created correctly and a Job can be triggered in order to create a configuration. First the Job definition for the Worker is to be checked:
    1. Open the Workers page.
    2. Open the Job definition by clicking > in the tab for Worker #1 in the jobdef1 line.
If information that is not correct is listed, adapt the Job definition. If required, update the Job definition:
    1. Start the Worker with  (Start worker).
    2. Update the list of the Job definitions for the Worker with  (Update Job definitions).
Stop the Worker:
    1. Stop the Worker with  (Stop worker).
In order to carry out the test the IMX file T1_Project.IMX has to be copied to the folder that is specified in the Job definition with the <incomingFolder> tag and the Worker to be started. Start the Worker:
    1. Copy the file <Job Server installation path>\resources\JobServer\IMX\T1_Project.imx to the folder <Job Server installation path>\resources\JobServer\\() input. (Customize the file path)
    2. Start the Worker with  (Start worker).
The job is executed immediately. The status of the Job can be checked on the Jobs page:
    1. Open the Jobs page.
All the Jobs are listed with their name. The status of the successfully completed Job is identified by a green check mark. The address of the Worker that executed this Job is listed in the Worker column. Further information about this Job is displayed in an external browser when the symbol  in the Actions column is clicked.
    1. Open the Windows Explorer.
    2. Navigate the c:\temp directory.
Result: Although the Job has been executed successfully, a created file does not exist. The result therefore has to be saved with a further action on c:\temp. The next section shows how the result of the generation is saved.
