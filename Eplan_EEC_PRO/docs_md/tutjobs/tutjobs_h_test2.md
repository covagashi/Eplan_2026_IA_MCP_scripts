---
title: "Test 2 - Creating and storing a configuration"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutjobs_h_test2.htm"
file: "tutjobs_h_test2"
category: "tutjobs"
---

# Test 2 - Creating and storing a configuration

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Tutorial Test 2 - Creating and storing a configuration Requirements:
     * EEC as a Job Server with Worker installation Version 2.5.1 or higher.
     * Job Server is started.
     * The Job Server perspective is opened.
The second test is intended to show that the Job definition has been created correctly and a Job can be triggered in order to create and save a configuration. First the Job definition for the Worker is to be checked:
    1. Open the Workers page.
    2. Start the Worker with  (Start worker).
    3. Update the list of the Job definitions for the Worker with  (Update Job definitions).
    4. Open the Job definition by clicking > in the tab for Worker #1 in the jobdef2 line.
If information that is not correct is listed, adapt the Job definition. If required, update the Job definition:
    1. Click on  to start the Worker.
    2. Click [Update Job definitions].
Stop the Worker:
    1. Click on  to stop the Worker.
In order to carry out the test the IMX file T1_Project.IMX has to be copied to the folder that is specified in the Job definition with the <incomingFolder> tag and the Worker to be started. Start the Worker:
    1. Copy the file <Job Server installation path>\resources\JobServer\IMX\T1_Project.imx to the folder <Job Server installation path>\resources\JobServer\input.
    2. Click on  to start the Worker.
The job is executed immediately. The status of the Job can be checked on the Jobs page:
    1. Open the Jobs page.
All the Jobs are listed with their name. The status of the successfully completed Job is identified by a green check mark. The address of the Worker that executed this Job is listed in the Worker column. Further information about this Job is displayed in an external browser when the symbol  in the Actions column is clicked.
    1. Open the Windows Explorer.
    2. Navigate the c:\temp directory.
Result: The Job is executed successfully. The result is saved as the file Feeder.eox in the directory c:\temp. The content of Feeder.eox can be checked by means of a stand-alone installation of the EEC:
    1. Start EEC
    2. Select the c:\temp\Feeder.eox file as the data basis.
    3. If necessary, mark the Open read-only option.
    4. In the Project catalog open the Feeder project:
The Feeder project is created successfully by the import. No component is placed on the Placeholder_Inspect placeholder. The next section shows how components are placed on the Placeholder_Inspect placeholder and all the extension points.
