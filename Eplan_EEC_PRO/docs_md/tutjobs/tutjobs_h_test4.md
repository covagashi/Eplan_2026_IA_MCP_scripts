---
title: "Creating a configuration with webserviceTrigger"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutjobs_h_test4.htm"
file: "tutjobs_h_test4"
category: "tutjobs"
---

# Creating a configuration with webserviceTrigger

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating a configuration with webserviceTrigger Requirements:
     * EEC as a Job Server with Worker installation Version 2.5.1 or higher.
     * Job Server is started.
     * The Job Server perspective is opened.
The fourth test is intended to show that the Job definition has been created correctly and a Job can be triggered in a browser via URL. The Job is triggered by calling a URL. The URL has to pass the name of the IMX file T1_Project.imx as the argument for the ImportEOXCommand. This is intended to create a configuration as an EOX file called Feeder.eox that is made available as a download. Start the Worker:
    1. Click on  to start the Worker.
    2. Update the list of the Job definitions for the Worker with (Update Job definitions).
    3. Open the Job definition by clicking > in the tab for Worker #1 in the jobdef4 line.
If information that is not correct is listed, adapt the Job definition.
    1. Copy the Post Job URL into the Clipboard.
    2. Open a browser.
    3. Insert the Post Job URL into the address field of the browser.
    4. Enter the following text directly at the end of the Post Job URL:
    
        ?pathToIMX=IMX\T1_Project.imx

The complete URL should have this content (Post Job URL and file path correspondingly):
    
        http://jobserver:8686/jobs/request/jobdef4?pathToIMX=<Job Server installation path>\resources\JobServer\IMX\T1_Project.imx

The Worker begins with the execution of the Job. After successful generation of the configuration a link to the file Feeder.eox is offered below the specification File(s):. A click on the link opens the dialog File download of the operating system in order to save the file.
    1. Open the Jobs page in the Job Server.
A click on the symbol  opens a browser in which the Job status is displayed (see the figure in the preceding step. A click on the symbol  opens the dialog File download of the operating system in order to save the created file. Result: The Job is executed successfully. The result can be downloaded as the file Feeder.eox. Since this is a local installation, the file is also stored in the directory <Job Server installation path>\resources\JobServer\JobServer\output\Job4_151106_1120_19341\results. The directory varies on the basis of the time stamp. The content of Feeder.eox can be checked by means of a stand-alone installation of the EEC:
    1. Start EEC
    2. Select the EOX file of the current Job as the data basis, for example <Job Server installation path>\resources\JobServer\output\Job4_151106_1120_19341\results\Feeder.eox.
    3. If necessary, mark the Open read-only option.
    4. In the Project catalog open the Feeder project:
The Feeder project is created successfully by the Job.
