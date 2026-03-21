---
title: "getAllMechatronicTopLevelComponents(List libraryNames)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_getallmechatronictoplevelcomponents.htm"
file: "refscripting_r_getallmechatronictoplevelcomponents"
category: "refscripting"
---

# getAllMechatronicTopLevelComponents(List libraryNames)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  getAllMechatronicTopLevelComponents(List libraryNames) Determines all mechatronic components of the highest level of the specified libraries. getAllMechatronicTopLevelComponents(List libraryNames)  
---  
Argument | List | libraryNames | List of libraries  
Return value | List | List of the names of all projects  
Exception error |  |  |   
Plug-in | com.mind8.mechatronic.skill.eos.TypeClass  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.getAllMechatronicTopLevelComponents) finds a list of the imported libraries and from this the mechatronic components of the top level. The method TypeClass.findType() finds the library component Util to execute the method getAllProjectNames contained in it (see row 13). The method TypeClass.findType() finds the library component Util to execute the method getAllMechatronicTopLevelComponents contained in it (see row 19). Information is output in the message log (see rows 7, 17, 22 and 25).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import org.foederal.eobroker.core.IUnitOfWork;
    import com.mind8.mechatronic.skill.eos.TypeClass;
    
    String scriptName = "getAllMechatronicTopLevelComponents";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    void main(obj){
    	String projectName = obj.getProject().name();
    	importedLibraries = TypeClass.findType(uow, "Engineering.Util").perform("getImportedLibraryNames", projectName);
    	
    	info = "Imported libraries: "+ importedLibraries;
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    	
    	List topLevelComponents = TypeClass.findType(uow, "Engineering.Util").perform("getAllMechatronicTopLevelComponents", importedLibraries);
    	
    	info = "Top level components: "+ topLevelComponents;
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    	
    	info = "### End of script '" + scriptName + "' ###";
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    }                                    
    main(obj);

Result: The SelectionAction outputs the following messages when applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial:
    
        ### Start of script 'getAllMechatronicTopLevelComponents' ###
    Imported libraries: [T_Mechatronic_ModularSystem, T_ECAD_P8]
    Top level components: [T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder]
    ### End of script 'getAllMechatronicTopLevelComponents' ###
