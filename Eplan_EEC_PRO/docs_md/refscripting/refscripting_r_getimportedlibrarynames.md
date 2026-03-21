---
title: "getImportedLibraryNames(String projectName)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_getimportedlibrarynames.htm"
file: "refscripting_r_getimportedlibrarynames"
category: "refscripting"
---

# getImportedLibraryNames(String projectName)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  getImportedLibraryNames(String projectName) Determines all names of the directly imported libraries for the specified project name. getImportedLibraryNames(String projectName)  
---  
Argument | String | projectName | Project name  
Return value | List | List of all directly imported libraries  
Exception error |  |   
Plug-in |  |  |   
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.getImportedLibraryNames) determines all names of the directly imported libraries for the current project. The obj.getProject().name() method determines the name of the project containing the selected project component (see row 13). The method TypeClass.findType() finds the library component Util to execute the method getImportedLibraryNames contained in it (see row 18). Information is output in the message log (see rows 7, 16, 21 and 24).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import org.foederal.eobroker.core.IUnitOfWork;
    import com.mind8.mechatronic.skill.eos.TypeClass;
    
    String scriptName = "getImportedLibraryNames";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    void main(obj){
    	String projectName = obj.getProject().name();
    	
    	info = "Project name: "+ projectName;
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    	
    	importedLibraries = TypeClass.findType(uow, "Engineering.Util").perform("getImportedLibraryNames", projectName);
    	
    	info = "Imported libraries: "+ importedLibraries;
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    	
    	info = "### End of script '" + scriptName + "' ###";
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    }                                    
    main(obj);

Result: The SelectionAction outputs the following messages when applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial:
    
        ### Start of script 'getImportedLibraryNames' ###
    Project name: Feeder_Extended1
    Imported libraries: [T_Mechatronic_ModularSystem, T_ECAD_P8]
    ### End of script 'getImportedLibraryNames' ###
