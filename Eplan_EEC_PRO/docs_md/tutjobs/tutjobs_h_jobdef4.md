---
title: "Setting a Job definition to webserviceTrigger"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutjobs_h_jobdef4.htm"
file: "tutjobs_h_jobdef4"
category: "tutjobs"
---

# Setting a Job definition to webserviceTrigger

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Setting a Job definition to webserviceTrigger Requirements:
     * EEC as a Job Server with Worker installation Version 2.5.1 or higher.
A configuration could be created successfully with the third Job definition. In it components were placed on the Placeholder_Inspect placeholder and all extension points. The Job was always triggered by a File-Trigger, i.e. an IMX file that was copied into the <incomingFolder> directory has triggered the processing. This section shows how a webserviceTrigger is defined in the Job definition in order to start the processing by a call in the browser. Proceed as follows to change the existing Job definition:
    1. Create a copy of the existing JMX file jobdef2.jmx called jobdef4.jmx.
    2. Open the JMX file jobdef4.jmx with any editor, for example Notepad++.
    3. Change the name of the Job definition from <jobdefinition name="Job2" to <jobdefinition name="Job4".
    4. Replace the block <fileTrigger> ... </fileTrigger> against the following block:
    
        <webserviceTrigger>
    	<failedFolder value="error" />
    	<outputFolder value="output" />
    </webserviceTrigger>

    1. Adjust the file paths to your installation accordingly.
    2. Replace the block <actions> ... </actions> against the following block:
    
        <actions>
    	<action name="Engineering.ImportIMXCommand" arguments="List{trigger.params.pathToIMX}" />
    	<action name="Engineering.ExportEOXCommand" arguments="List{trigger.additionalResultsDir + 'Feeder.eox',List{'Feeder'}}" />
    	<action name="JobServer.MarkFileForDownloadCommand" arguments="=List{trigger.outputFolder + 'results\\Feeder.eox'}" />
    </actions>

    1. Save the JMX file.
    2. Remove the Job definition jobdef2.jmx from the directory <Job Server installation path>\resources\JobServer\jobs.
The complete JMX file should have the following appearance: [Content of the jobdef4.jmx:](javascript:void\(0\);)
    
        <?xml version="1.0"?>
    <jobdefinition name="Job4"
    	model="eox\Tutorial_JobServer.eox"
    	xmlns:xi="http://www.w3.org/2001/XInclude">
    	<webserviceTrigger>
    		<failedFolder value="error" />
    		<outputFolder value="output" />
    	</webserviceTrigger>
    	<actions>
    		<action name="Engineering.ImportIMXCommand" arguments="List{trigger.params.pathToIMX}" />
    		<action name="Engineering.ExportEOXCommand" arguments="List{trigger.additionalResultsDir + 'Feeder.eox',List{'Feeder'}}" />
    		<action name="JobServer.MarkFileForDownloadCommand" arguments="=List{trigger.outputFolder + 'results\\Feeder.eox'}" />
    	</actions>
    </jobdefinition>

Description of the JMX file: After the obligatory header data in Line 1, the name of the new Job definition is specified in Line 2 with the name attribute of the <jobdefinition> tag. The model="eox\Tutorial_JobServer.eox" attribute specifies which basic model is to be applied for the generation of the Job data. The directories in which the data are stored in the case of success and failure are specified in the <webserviceTrigger> block. The <action name="Engineering.ImportIMXCommand" arguments="List{trigger.params.pathToIMX}" /> action calls up the ImportIMXCommand. The command expected the name of an IMX file as the argument. This is transferred as a URL parameter during the call. The <action name="Engineering.ExportEOXCommand" arguments="List{trigger.additionalResultsDir + 'Feeder.eox',List{'Feeder'}}" /> action calls the ExportEOXCommand command. This has the effect that the created configuration is exported as an EOX file. The command expects the name of the EOX file as the argument. With trigger.additionalResultsDir + 'Feeder.eox' a path is specified that is based on the specification of the <outputFolder> tags, attaches a directory called \results\ to it and specifies the file name as Feeder.eox. The result has to be <Job Server installation path>\resources\JobServer\output\results\Feeder.eox. As the second argument the project name for the configuration is passed to the command. The <action name="JobServer.MarkFileForDownloadCommand" arguments="=List{trigger.outputFolder + 'results\\\Feeder.eox'}" /> action calls the MarkFileForDownloadCommand command. This creates a link for the created file in the Job status view so that this can be downloaded.
    1. Continue with [Creating a configuration with webserviceTrigger](tutjobs_h_test4.htm).
