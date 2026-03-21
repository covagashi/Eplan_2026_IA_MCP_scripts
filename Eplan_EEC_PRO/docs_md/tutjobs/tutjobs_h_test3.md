---
title: "Test 3 - Creating a configuration with updated extension points"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutjobs_h_test3.htm"
file: "tutjobs_h_test3"
category: "tutjobs"
---

# Test 3 - Creating a configuration with updated extension points

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Tutorial Test 3 - Creating a configuration with updated extension points Requirements:
     * EEC as a Job Server with Worker installation Version 2.5.1 or higher.
     * Job Server is started.
     * The Job Server perspective is opened.
The third test is intended to show that the Job definition has been created correctly and a Job can be triggered. Through it a configuration is created in which the Inspect component is placed on the matching placeholder and all the extension points are updated. Since nothing has changed at the Job definition for the Worker, the steps for checking are not required. Stop the Worker:
    1. Click on  to stop the Worker.
In order to carry out the test the IMX file T3_Project.IMX has to be copied to the folder that is specified in the Job definition with the <incomingFolder> tag and the Worker to be started. Start the Worker:
    1. Copy the file <Job Server installation path>\resources\JobServer\IMX\T3_Project.imx to the folder <Job Server installation path>\resources\JobServer\input.
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
The Feeder project is created successfully by the import. The Inspect project component is placed on the Placeholder_Inspect placeholder. The Orientationinspector component i is placed on the ExtensionPoint_Orientationinspector extension point and the Positionsensor_optical component on the ExtensionPoint_Positionsensor_optical extension point.
