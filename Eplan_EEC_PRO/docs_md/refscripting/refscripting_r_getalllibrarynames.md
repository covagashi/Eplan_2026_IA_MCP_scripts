---
title: "getAllLibraryNames()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_getalllibrarynames.htm"
file: "refscripting_r_getalllibrarynames"
category: "refscripting"
---

# getAllLibraryNames()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  getAllLibraryNames() Determined for the names of all imported libraries. getAllLibraryNames()  
---  
Argument |  |  |   
Return value | List | List of the names of all projects  
Exception error |  |  |   
Plug-in | com.mind8.mechatronic.skill.eos.TypeClass  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.getAllLibraryNames) determines the names of all imported libraries for the current project. The method TypeClass.findType() finds the library component Util to execute the method getAllLibraryNames contained in it (see row 13). Information is output in the message log (see rows 7, 16 and 19).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import org.foederal.eobroker.core.IUnitOfWork;
    import com.mind8.mechatronic.skill.eos.TypeClass;
    
    String scriptName = "getAllLibraryNames";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    void main(obj){
    	List libraryNames = TypeClass.findType(uow, "Engineering.Util").perform("getAllLibraryNames");
    	
    	info = "Library names: "+ libraryNames;
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    	
    	info = "### End of script '" + scriptName + "' ###";
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    }                                    
    main(obj);

Result: The SelectionAction outputs the following messages when applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial:
    
        ### Start of script 'getAllLibraryNames' ###
    Library names: [T_Ecad_Ui, T_ECAD_P8, T_Mechatronic_ModularSystem, ScriptingExamples, T_Interfaces, T_Mechatronic_Architecture]
    ### End of script 'getAllLibraryNames' ###
