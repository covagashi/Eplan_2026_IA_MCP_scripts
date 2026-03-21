---
title: "Writing key-value pairs in the Map parameter via a webserviceTrigger"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutjobs_h_test5.htm"
file: "tutjobs_h_test5"
category: "tutjobs"
---

# Writing key-value pairs in the Map parameter via a webserviceTrigger

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Writing key-value pairs in the Map parameter via a webserviceTrigger Requirements:
     * EEC as a Job Server with Worker installation Version 2.5.1 or higher.
     * Job Server is started.
     * The Job Server perspective is opened.
The fifth test is intended to show that the Job definition has been created correctly and a Job can be triggered in a browser via URL. The Job is triggered by calling a URL. The URL must pass one or more key-value pairs as an argument for the setFeederParameterMapAction action. These key-value pairs are to be stored in the ParameterMap parameter of the Station Feeder. Start the Worker:
    1. Start the Worker with  (Worker startup).
    2. Update the list of the Job definitions for the Worker with [Update Job definitions].
    3. Open the Job definition by clicking > in the tab for Worker #1 in the jobdef5 line.
If information that is not correct is listed, adapt the Job definition.
    1. Copy the Post Job URL into the Clipboard.
    2. Open a browser.
    3. Insert the Post Job URL into the address field of the browser.
    4. Enter the key-value pairs with the syntax ?Key1=Value1&Key2=Value2&Key3=Value3 directly at the end of the Post Job URL. Use the following text for the tutorial:
    
        ?EAN=4016779578639&Weight=4t&MaxSpeed=240&MaxFunctiongroups=5&Option=Inspect

The complete URL should have this content (adjust Post Job URL):
    
        http://jobserver:8686/jobs/request/jobdef5?EAN=4016779578639&Weight=4t&MaxSpeed=240&MaxFunctiongroups=5&Option=Inspect

    1. Complete the entry with [Enter].
The Worker begins with the execution of the Job. After successful Job processing a link to the file Feeder.eox is offered below the specification File(s):. A click on the link opens the dialog File download of the operating system in order to save the file.
    1. Open the Jobs page in the Job Server.
A click on the symbol  opens a browser in which the Job status is displayed (see the figure in the preceding step. A click on the symbol  opens the dialog File download of the operating system in order to save the created file. Result: The Job is executed successfully. The result can be downloaded as the file Feeder.eox. Since this is a local installation, the file is also stored in the directory <Job Server installation path>\resources\JobServer\JobServer\output\Job5_151106_1130_39326\results. The directory varies on the basis of the time stamp. The content of Feeder.eox can be checked by means of a stand-alone installation of the EEC:
    1. Start EEC
    2. Select the <Job Server installation path>\resources\JobServer\output\Job5_151106_1130_39326\results\Feeder.eox file as the data basis.
    3. If necessary, mark the Open read-only option.
    4. Open the Feeder component in the Project catalog.
    5. Open the Parameter editor.
The key-value pairs that were passed with the URL are stored in the ParameterMap parameter.
