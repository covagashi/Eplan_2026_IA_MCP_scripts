---
title: "Commands: Overview"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_o_overview.htm"
file: "refcommands_o_overview"
category: "refcommands"
---

# Commands: Overview

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Commands: Overview Commands are objects, that provide algorithms for certain tasks (e.g. creating of a schematic diagram). The algorithms are implemented in execute methods. Each command has at least one execute method. Several execute methods with different arguments can also be specified. Commands are connected to the user interface within actions (calls by the right mouse key or Form-UI (see also [Commands and actions](concept_k_commands_and_actions.htm)). The plug-ins of the system provide commands via system libraries. Command | Area | Description  
---|---|---  
[AutomationWorX.GenerateAutomationWorXCodeCommand](refcommands_r_automationworx_generateautomationworxcodecommand.htm) | AutomationWorX | Generates the program code for AutomationWorX. The code can be viewed in the navigator.  
[AutomationWorX.GenerateAutomationWorXStructureCommand](refcommands_r_automationworx_generateautomationworxstructurecommand.htm) | AutomationWorX | Generates the AutomationWorX structure.  
[CoDeSys.GenerateCoDeSysCodeCommand](refcommands_r_codesys_generatecodesyscodecommand.htm) | CoDeSys | Generates the program code for CoDeSys. The code can be viewed in the navigator.  
[CoDeSys.GenerateCoDeSysStructureCommand](refcommands_r_codesys_generatecodesysstructurecommand.htm) | CoDeSys | Generates the CoDeSys structure.  
[CoDeSys.GenerateENIProjectCommand](refcommands_r_codesys_generateeniprojectcommand.htm) | CoDeSys | Passes the created CoDeSys program code to the ENI server.  
[ECAD.GenerateECADCodeCommand](refcommands_r_ecad_generateecadcodecommand.htm) | ECAD | Generates the schematic.  
[ECAD.GenerateEcadProjectCommand](refcommands_r_ecad_generateecadprojectcommand.htm) | ECAD | Generates the Eplan Electric P8 project.  
[ECAD.GenerateEcadProjectFromTypicalFileCommand](refcommands_r_ecad_generateecadprojectfromtypicalfilecommand.htm) | ECAD | Generates the Eplan Electric P8 project on the basis of a typical.xml in the format of EEC One.  
[ECAD.GenerateEcadStructureCommand](refcommands_r_ecad_generateecadstructurecommand.htm) | ECAD | Generates the ECAD structure.  
[ECAD.GenerateEdzForEcadProjectCommand](refcommands_r_ecad_generateedzforecadprojectcommand.htm) | ECAD | Generates an EDZ file of the specified project components of the WiringDiagram type.  
[ECAD.GenerateMacroAndEdzForEcadProjectCommand](refcommands_r_ecad_generatemacroandedzforecadprojectcommand.htm) | ECAD | By using the command data are packed into an EDZ file whose contents represent a part for the P8 parts database.  
[ECAD.GenerateXmlForEcadProjectCommand](refcommands_r_ecad_generatexmlforecadprojectcommand.htm) | ECAD | Creates an XML file ec-instructions.xml, as well as the macro files of the project to be created in the specified folder.  
[ECAD.OpenECADComponentCommand](refcommands_r_ecad_openecadcomponentcommand.htm) | ECAD | Generates and opens the schematic for the passed ECAD component.  
[ECAD.OpenECADPagesCommand](refcommands_r_ecad_openecadpagescommand.htm) | ECAD | Generates and opens the passed wiring diagrams of the project.  
[ECAD.OpenEcadProjectCommand](refcommands_r_ecad_openecadprojectcommand.htm) | ECAD | Opens the Eplan Electric P8 project.  
[ECAD.OpenProjectDiagramsCommand](refcommands_r_ecad_openprojectdiagramscommand.htm) | ECAD | Generates and opens all schematic diagrams of a project.  
[ECAD.UpdateEcadPagesCommand](refcommands_r_ecad_updateecadpagescommand.htm) | ECAD | Generates a project with specific pages of an Eplan Electric P8 project depending on the preference Reuse existing project for schematic generation.  
[Engineering.AbortExecutionIfErrorCommand](refcommands_r_engineering_abortexecutionIferrorcommand.htm) | Engineering | Aborts die execution of all following commands, if an error occurred in one of the preceding commands.  
[Engineering.ClearAllParameterValuesCommand](refcommands_r_engineering_clearallparametervaluescommand.htm) | Engineering | Deletes all parameter values of the mechatronic structure.  
[Engineering.CopyFileCommand](refcommands_r_engineering_copyfilecommand.htm) | Engineering | Copies a file or a folder to the specified target.  
[Engineering.CreateInstanceCommand](refcommands_r_engineering_createinstancecommand.htm) | Engineering | Creates a new instance.  
[Engineering.CreateNewProjectBasedOnPXCommand](refcommands_r_engineering_createnewprojectbasedonpxcommand.htm) | Engineering | Creates a new project based on a PX file.  
[Engineering.ExportEOXCommand](refcommands_r_engineering_exporteoxcommand.htm) | Engineering | Exports the selected assemblies to an EOX file.  
[Engineering.ExportProblemReport](refcommands_r_engineering_exportproblemreport.htm) | Engineering | Exports the current model as a ZIP archive with the name Report_<priority>_<YYYY-MM-DD_HH-MM>.zip, creates a Quality Feedback Report and starts the local e-mail client in order to send the Quality Feedback Report.  
[Engineering.ExportPXCommand](refcommands_r_engineering_exportpxcommand.htm) | Engineering | Exports changes to the project to a PX file.  
[Engineering.ForcefulEOXImportCommand](refcommands_r_engineering_forcefuleoximportcommand.htm) | Engineering | Imports an EOX file.  
[Engineering.ImportCSVCommand](refcommands_r_engineering_importcsvcommand.htm) | Engineering | Imports a project according to the assigned CSV file.  
[Engineering.ImportExcelCommand](refcommands_r_engineering_importexcelcommand.htm) | Engineering | Imports an Excel file according to the specified schema and template file into a project or a project component.  
[Engineering.ImportLibrariesCommand](refcommands_r_engineering_importlibrariescommand.htm) | Engineering | Imports the libraries into the project, which are passed by the list.  
[Engineering.ImportIMXCommand](refcommands_r_engineering_importimxcommand.htm) | Engineering | Imports a project according to the assigned IMX file.  
[Engineering.ImportIMXWithTemplateCommand](refcommands_r_engineering_importimxwithtemplatecommand.htm) | Engineering | Imports an IMX file according to the specified template file into a project or a project component.  
[Engineering.ImportPXCommand](refcommands_r_engineering_importpxcommand.htm) | Engineering | Imports all projects occurring in a PX file.  
[Engineering.ImportXMLCommand](refcommands_r_engineering_importxmlcommand.htm) | Engineering | Imports a project according to the assigned XML file.  
[Engineering.NewProjectCommand](refcommands_r_engineering_newprojectcommand.htm) | Engineering | Creates a new project.  
[Engineering.OpenCommand](refcommands_r_engineering_opencommand.htm) | Engineering |  Opens the object that is specified by absoluteName. In the Web EEC environment: Returns an URL of the created file.  
[Engineering.OpenResourceCommand](refcommands_r_engineering_openresourcecommand.htm) | Engineering | Opens the created file with the specified path of the specified project.  
[Engineering.RemoveExtensionsCommand](refcommands_r_engineering_removeextensionscommand.htm) | Engineering | The execute method of this command removes the components, which are inserted on extension points.  
[Engineering.RemoveLibrariesCommand](refcommands_r_engineering_removelibrariescommand.htm) | Engineering | Removes the libraries from the project, which are passed by the list.  
[Engineering.RemoveImportedLibrariesAndExtensionsCommand](refcommands_r_engineering_removeimportedlibrariesandextensionscommand.htm) | Engineering | Deletes from the project all instances of the specified library that were inserted into the project via an extension point.  
[Engineering.SaveObjectCommand](refcommands_r_engineering_saveobjectcommand.htm) | Engineering | Saves the modifications on the model.  
[Engineering.SendMailCommand](refcommands_r_engineering_sendmailcommand.htm) | Engineering | Sends an e-mail with the specified content from the specified sender to the specified addresses with the specified attachments.  
[Engineering.SetParameterValueFromJsonCommand](refcommands_r_engineering_setparametervaluefromjsoncommand.htm) | Engineering | Saves the contents of a JSON structure as a map in a parameter. The JSON structure is transferred to the Job Server as POST data.  
[Engineering.SetParameterValueFromJsonFileCommand](refcommands_r_engineering_setparametervaluefromjsonfilecommand.htm) | Engineering | Saves the contents of a JSON file as map in a parameter.  
[Engineering.StartFormulaCacheCommand](refcommands_r_engineering_startformulacachecommand.htm) | Engineering | Activates the formula cache.  
[Engineering.StopFormulaCacheCommand](refcommands_r_engineering_stopformulacachecommand.htm) | Engineering | Disables the formula cache.  
[Engineering.UpdateExtensionsCommand](refcommands_r_engineering_updateextensionscommand.htm) | Engineering | The execute methods of this command remove the invalid components, which are inserted on extension points and inserts new valid components.  
[Engineering.UpdateStaticDisablerCommand](refcommands_r_engineering_updatestaticdisablercommand.htm) | Engineering | Sets the explicit version update of outdated projects.  
[Engineering.ZipFileCommand](refcommands_r_engineering_zipfilecommand.htm) | Engineering | Packs single files or a folder into a ZIP file.  
[JobServer.MarkFileForDownloadCommand](refcommands_r_jobserver_markfilefordownload.htm) | JobServer | Marks the specified file for downloading.  
[JobServer.PutResultCommand](refcommands_r_jobserver_putresultcommand.htm) | JobServer | Sets the value of a key-value pair in the ResultData object.  
[JobServer.SetProgressMessageCommand](refcommands_r_jobserver_setprogressmessagecommand.htm) | JobServer | Sets the value that is returned in the result of a status query for the "message" key.  
[Plc.GenerateFieldbusCommand](refcommands_r_plc_generatefieldbuscommand.htm) | PLC | Generates all start addresses and connections.  
[Plc.OverwriteAddressesCommand](refcommands_r_plc_overwriteaddressescommand.htm) | PLC | Creates new start addresses, any existing formulas for start addresses are not taken into account, sensors and actuators remain unaffected.  
[Plc.OverwriteConnectionsCommand](refcommands_r_plc_overwriteconnectionscommand.htm) | PLC | Generates all connections new.  
[Plc.OverwriteFieldbusCommand](refcommands_r_plc_overwritefieldbuscommand.htm) | PLC | Generates all start addresses and connections new.  
[Plc.RecreateAddressesCommand](refcommands_r_plc_regenerateaddressescommand.htm) | PLC | Generates all start addresses new.  
[Plc.RegenerateConnectionsCommand](refcommands_r_plc_regenerateconnectionscommand.htm) | PLC | Generates all connections new.  
[Plc.ResetAddressesCommand](refcommands_r_plc_resetaddressescommand.htm) | PLC | Deletes previously calculated start addresses.  
[Plc.ResetConnectionsCommand](refcommands_r_plc_resetconnectionscommand.htm) | PLC | Deletes previously calculated connections.  
[Plc.ResetFieldbusCommand](refcommands_r_plc_resetfieldbuscommand.htm) | PLC | Deletes all start addresses and connections.  
[Plc.UpdateAddressesCommand](refcommands_r_plc_updateaddressescommand.htm) | PLC | Creates new start addresses, any existing formulas for start addresses are not taken into account, sensors and actuators remain unaffected.  
[Plc.UpdateConnectionsCommand](refcommands_r_plc_updateconnectionscommand.htm) | PLC | Creates the non-existing connections.  
[Plc.UpdateFieldbusCommand](refcommands_r_plc_updatefieldbuscommand.htm) | PLC | Generates start addresses and connections of control components, sensors and actuators, which have no connection or start address yet and of sensors and actuators, whose connections do not exist anymore (e.g. because a control component is deleted).  
[Step7.GenerateSimaticProjectCommand](refcommands_r_step7_generatesimaticprojectcommand.htm) | STEP 7 | Passes the created Simatic program code to the Simatic-Manager.  
[Step7.GenerateStep7CodeCommand](refcommands_r_step7_generatestep7codecommand.htm) | STEP 7 | Generates the STEP 7 program code.  
[Step7.GenerateStep7NumbersCommand](refcommands_r_step7_generatestep7numberscommand.htm) | STEP 7 | Generates the block numbers for STEP 7 blocks.  
[Step7.GenerateStep7StructureCommand](refcommands_r_step7_generatestep7structurecommand.htm) | STEP 7 | Generates the STEP 7 structure.  
[TextDiscipline.GenerateTextDisciplineCodeCommand](refcommands_r_textdiscipline_generatetextdisciplinecodecommand.htm) | TextDiscipline | Generates the text discipline files.  
[TextDiscipline.GenerateTextDisciplineStructureCommand](refcommands_r_textdiscipline_generatetextdisciplinestructurecommand.htm) | TextDiscipline | Generates the structure of the text discipline components.  
[TextDiscipline.OpenTextDisciplineComponentsWithEclipseCommand](refcommands_r_textdiscipline_opentextdisciplinecomponentswitheclipsecommand.htm) | TextDiscipline | Opens the text discipline component with the EEC-internal editor.  
[TextDiscipline.OpenTextDisciplineComponentsWithOSCommand](refcommands_r_textdiscipline_opentextdisciplinecomponentswithsocommand.htm) | TextDiscipline | Opens the text discipline component in the editor which is assigned in the operating system to open text files.  
[Word.GenerateWordCodeCommand](refcommands_r_word_generatewordcodecommand.htm) | Word | Generates a Word document from the active discipline components.  
[Word.GenerateWordPDFCommand](refcommands_r_word_generatewordpdfcommand.htm) | Word | Opens the PDF file which was created by Word in the editor which is assigned in the operating system to open PDF files.  
[Word.GenerateWordStructureCommand](refcommands_r_word_generatewordstructurecommand.htm) | Word | Generates the discipline structure for a Word document from the active discipline components.  
[Word.OpenWordDisciplineCommand](refcommands_r_word_disciplinecommand.htm) | Word | Opens the Word discipline component in the editor which is assigned in the operating system to open Word files.  
[Word.OpenWordPDFCommand](refcommands_r_word_openwordpdfcommand.htm) | Word | Opens the PDF file which was created by Word in the editor which is assigned in the operating system to open PDF files.  
[Word.UpdateWordFieldsCommand](refcommands_r_word_updatefieldscommand.htm) | Word | Updates the field contents of all fields within a created Word document.
