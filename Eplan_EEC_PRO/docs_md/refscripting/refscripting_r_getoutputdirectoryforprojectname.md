---
title: "getOutputDirectoryForProjectName(String projectName, Boolean createFolder)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_getoutputdirectoryforprojectname.htm"
file: "refscripting_r_getoutputdirectoryforprojectname"
category: "refscripting"
---

# getOutputDirectoryForProjectName(String projectName, Boolean createFolder)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  getOutputDirectoryForProjectName(String projectName, Boolean createFolder) Determines the output folder for the created files for the specified project name. If no folder exists, it can be created if required. The output folder is session-specific for the Job Server and Web EEC, meaning that it contains the session ID. getOutputDirectoryForProjectName(String projectName, Boolean createFolder)  
---  
Argument | String | projectName | Project name  
Boolean | createFolder | true = creates an output folder if it does not exist.  
false = does not create an output folder.  
Return value | String | Absolute path of the output folder  
Exception error |  |   
Plug-in |  |  |   
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.getOutputDirectoryForProjectName) determines the absolute path of the output folder for the current project. The obj.getProject().name() method determines the name of the project containing the selected project component (see row 13). The method TypeClass.findType() finds the library component Util to execute the method getOutputDirectoryForProjectName contained in it (see row 18). Information is output in the message log (see rows 7, 16, 21 and 24).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import org.foederal.eobroker.core.IUnitOfWork;
    import com.mind8.mechatronic.skill.eos.TypeClass;
    
    String scriptName = "getOutputDirectoryForProjectName";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    void main(obj){
    	String projectName = obj.getProject().name();
    	
    	info = "Project name: "+ projectName;
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    	
    	outputDirectory = TypeClass.findType(uow, "Engineering.Util").perform("getOutputDirectoryForProjectName", projectName, true);
    	
    	info = "Output directory: "+ outputDirectory;
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    	
    	info = "### End of script '" + scriptName + "' ###";
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    }                                    
    main(obj);

Result: The SelectionAction outputs the following messages when applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial:
    
        ### Start of script 'getOutputDirectoryForProjectName' ###
    Project name: Feeder_Extended1
    Output directory: E:\Users\Public\EPLAN\EngineeringConfiguration\2025\workspace_SCRIPTING\Feeder_Extended1
    ### End of script 'getOutputDirectoryForProjectName' ###
