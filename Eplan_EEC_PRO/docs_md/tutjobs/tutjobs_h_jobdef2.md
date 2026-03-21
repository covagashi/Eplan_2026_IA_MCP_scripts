---
title: "Extending the Job definition to save the result"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutjobs_h_jobdef2.htm"
file: "tutjobs_h_jobdef2"
category: "tutjobs"
---

# Extending the Job definition to save the result

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Extending the Job definition to save the result Requirements:
     * EEC as a Job Server with Worker installation Version 2.5.1 or higher.
Although a configuration could be created in the first Job definition, these were not saved in the file systems. The existing configuration of the preceding section is to be extended so that a configuration is created on the basis of the EOX file Tutorial_JobServer.eox and is saved on c:\temp\. To this purpose the IMX file T1_Project.imx is to be imported by means of the command Engineering.ImportIMXCommand. Subsequently the command Engineering.ExportEOXCommand is executed in order to store the created configuration as a file Feeder.eox auf c:\temp\. Proceed as follows to extend the existing Job definition:
    1. Create a copy of the existing Job definition jobdef1.jmx called jobdef2.jmx.
    2. Open the Job definition jobdef2.jmx with any editor, for example Notepad++.
    3. Change the name of the Job definition from <jobdefinition name="Job1" to <jobdefinition name="Job2".
    4. Insert the following line below the line <action name="Engineering.ImportIMXCommand" arguments="List{trigger.filePath}" />:
    
        <action name="Engineering.ExportEOXCommand" arguments="List{'C:\\TEMP\\Feeder.eox',List{'Feeder'}}" />

    1. Save the Job definition.
The complete Job definition should have the following appearance: [Contents of the jobDef2.jmx](javascript:void\(0\);)
    
        <?xml version="1.0" encoding="utf-8"?>
    <jobdefinition name="Job1"
    	model="EOX\Tutorial_JobServer.eox"
    	xmlns:xi="http://www.w3.org/2001/XInclude">
    	<fileTrigger>
    		<failedFolder value="error" />
    		<incomingFolder value="input" />
    		<outputFolder value="output" />
    		<filter value="*.imx" />
    	</fileTrigger>
    	<actions>
    		<action name="Engineering.ImportIMXCommand" arguments="List{trigger.filePath}" />
    		<action name="Engineering.ExportEOXCommand" arguments="List{'C:\\TEMP\\Feeder.eox',List{'Feeder'}}" />
    	</actions>
    </jobdefinition>

    1. Move the Job definition jobdef1.jmx into the directory <Job Server installation path>\resources\JobServer\JMX.
    2. Continue with section [Test 2 - Creating and storing a configuration](tutjobs_h_test2.htm).
