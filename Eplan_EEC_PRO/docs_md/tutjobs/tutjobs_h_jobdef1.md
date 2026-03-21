---
title: "Creating a Job definition with file triggers for creating a configuration"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutjobs_h_jobdef1.htm"
file: "tutjobs_h_jobdef1"
category: "tutjobs"
---

# Creating a Job definition with file triggers for creating a configuration

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating a Job definition with file triggers for creating a configuration Requirements:
     * EEC as a Job Server with Worker installation Version 2.5.1 or higher.
The first Job definition is intended to achieve that a configuration is created on the basis of the EOX file Tutorial_JobServer.eox. To this purpose the IMX file T1_Project.imx is to be imported by means of the command Engineering.ImportIMXCommand. The execution is to be triggered by a file trigger that responds to the IMX file. The subsequent Job definition contains file paths that have to be customized to the own installation. Proceed as follows to create the first Job definition:
    1. Open any editor, for example Notepad++.
    2. If appropriate, set the encoding to UTF-8.
    3. Insert the following line as header data into the first row:
    
        <?xml version="1.0" encoding="utf-8"?>

    1. After the header data insert the tag <jobdefinition> in order to specify the name of the Job definition and the basic model. To do this enter the following rows (the path specifications are relative to the set path to the Job Server resources):
    
        <jobdefinition name="Job1"
    	model="EOX\Tutorial_JobServer.eox"
    	xmlns:xi="http://www.w3.org/2001/XInclude">

    1. Under <jobdefinition> use the following lines to specify in which folder of the Job Server incoming files are to be expected and in which folders files are stored in the case of success or faults. In addition, the filter is specified so that the file trigger responds to incoming IMX files:
    
        <fileTrigger>
    	<failedFolder value="error" />
    	<incomingFolder value="input" />
    	<outputFolder value="output" />
    	<filter value="*.imx" />
    </fileTrigger>

    1. On the same level use the following lines to specify that the command [Engineering.ImportIMXCommand](refcommands_r_engineering_importimxcommand.htm) is to be executed. The IMX file that is copied into the incoming folder is to be passed as the argument:
    
        <actions>
    	<action name="Engineering.ImportIMXCommand" arguments="List{trigger.filePath}" />
    </actions>

    1. The last line completes the <jobdefinition> tag:
    
        </jobdefinition>

    1. Save the Job definition under <Job Server installation path>\resources\JobServer\jobs\jobdef1.jmx (customize the file path).
The complete Job definition should have the following appearance: [Contents of the jobDef1.jmx](javascript:void\(0\);)
    
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
    	</actions>
    </jobdefinition>

    1. Continue with section [Test 1 - Konfiguration erstellen](tutsap_h_test1.htm).
