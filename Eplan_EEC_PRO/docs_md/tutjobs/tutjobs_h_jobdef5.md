---
title: "Changing a Job definition to import key-value pairs"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutjobs_h_jobdef5.htm"
file: "tutjobs_h_jobdef5"
category: "tutjobs"
---

# Changing a Job definition to import key-value pairs

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Changing a Job definition to import key-value pairs Requirements:
     * EEC as a Job Server with Worker installation Version 2.5.1 or higher.
A configuration could be created successfully with the fourth Job definition. The Job was triggered by a webserviceTrigger, i.e. a URL with POST parameter was entered in the browser that triggered the Job and simultaneously passed an argument for an action. This section shows how several arguments are passed so that key-value pairs are stored in a parameter of the Map type. To this purpose the EOX file Feeder.eox that was created with Test 4 is to be used as the basic model. Copy the basic model:
    1. Open the Jobs page in the Job Server.
    2. Click the  symbol in the line of the preceding Job (Job4_<Job-ID>) to open the File download dialog.
    3. Specify the <Job Server installation path>\resources\JobServer\EOX directory as the download target.
Create an action:
    1. Start EEC
    2. Select the <Job Server installation path>\resources\JobServer\EOX file as the data basis.
    3. Remove the marking of the Open read-only option.
    4. Confirm with [OK].
    5. Navigate to T_Mechatronic_ModularSystem in the library catalog.
    6. Create a unit called Actions.
    7. Navigate to the Actions unit.
    8. Select New > Object... from the popup menu.
    9. Select Action for a new object in the wizard.
    10. Close the wizard with [Finish].
    11. Enter the setFeederParameterMapAction name in the Name field.
    12. Open the Methods editor.
    13. Enter the run name in the Name field.
    14. Select the Java language from the Language drop-down list box.
    15. Click  (Add argument).
    16. In the Name column replace the name New Argument by params.
    17. In the Type column replace the Engineering.Object type by Engineering.Map.
    18. Enter the following Java code in the Code field.
    
        import com.mind8.mechatronic.skill.api.LiteralFormulaBuilder;
    import com.mind8.mechatronic.skill.AbsoluteNameUtil;
    // get Feeder from UnitOfWork
    feederEO = AbsoluteNameUtil.getObjectByAbsolutePath("Feeder.Mechatronic.Feeder",self.getUnitOfWork());
    // get parameter ParameterMap
    parameter = feederEO.getParameter("ParameterMap");
    					
    // set ParameterMap with key-value-pairs
    parameter.setPrettyValue(LiteralFormulaBuilder.buildLiteralFormula(params));
    // save changes
    self.getUnitOfWork().saveChanges();

    1. Save the action.
The action should have this appearance: Change the existing Job definition:
    1. Create a copy of the existing JMX file jobdef4.jmx called jobdef5.jmx.
    2. Open the JMX file jobdef5.jmx with any editor, for example Notepad++.
    3. Change the name of the Job definition from <jobdefinition name="Job4" to <jobdefinition name="Job5".
    4. Change the specification of the model to eox\Feeder.eox (customize the file path).
    5. Replace the line <action name="Engineering.ImportIMXCommand" arguments="List{trigger.params.pathToIMX}" /> by the following line:
    
        <action name="T_Mechatronic_ModularSystem.Actions.setFeederParameterMapAction" arguments="List{trigger.params}"/>

    1. Save the JMX file.
The complete JMX file should have the following appearance: [Content of the jobdef_5.jmx:](javascript:void\(0\);)
    
        <?xml version="1.0"?>
    <jobdefinition name="Job5"
    	model="EOX\Feeder.eox"
    	xmlns:xi="http://www.w3.org/2001/XInclude">
    	<webserviceTrigger>
    		<outputFolder value="output" />
    		<failedFolder value="error" />
    	</webserviceTrigger>
    	<actions>
    		<action name="T_Mechatronic_ModularSystem.Actions.setFeederParameterMapAction" arguments="List{trigger.params}"/>
    		<action name="Engineering.ExportEOXCommand" arguments="List{trigger.additionalResultsDir + 'Feeder.eox',List{'Feeder'}}" />
    		<action name="JobServer.MarkFileForDownloadCommand" arguments="=List{trigger.outputFolder + 'results\\Feeder.eox'}" />
    	</actions>
    </jobdefinition>

Description of the JMX file: After the obligatory header data in Line 1, the name of the new Job definition is specified in Line 2 with the name attribute of the <jobdefinition> tag. The model="EOX\Feeder.eoxâ attribute is changed so that the generation of the Job data is to be applied on the basis of the model created with jobdef5.jmx. The directories in which the data are stored in the case of success and failure are specified unchanged in the <webserviceTrigger> block. The <action name="T_Mechatronic_ModularSystem.Actions.setFeederParameterMapAction" arguments="List{trigger.params}"/> action calls up the setFeederParameterMapAction action created beforehand. The action expects key-value pairs as the argument. These are transferred as a URL parameter during the call. The <action name="Engineering.ExportEOXCommand" arguments="List{trigger.additionalResultsDir + 'Feeder.eox',List{'Feeder'}}" /> action calls the ExportEOXCommand command. This has the effect that the created configuration is exported as an EOX file. The command expects the name of the EOX file as the argument. With trigger.additionalResultsDir + 'Feeder.eox' a path is specified that is based on the specification of the <outputFolder> tags, attaches a directory called \results\ to it and specifies the file name as Feeder.eox. The result has to be <Job Server installation path>\resources\JobServer\output\results\Feeder.eox. As the second argument the project name for the configuration is passed to the command. The <action name="JobServer.MarkFileForDownloadCommand" arguments="=List{trigger.outputFolder + 'results\\\Feeder.eox'}" /> action calls the MarkFileForDownloadCommand command. This creates a link for the created file in the Job status view so that this can be downloaded.
    1. Move the Job definition jobdef4.jmx into the directory <Job Server installation path>\resources\JobServer\JMX.
    2. Continue with section [Writing key-value pairs in the Map parameter via a webserviceTrigger](tutjobs_h_test5.htm).
