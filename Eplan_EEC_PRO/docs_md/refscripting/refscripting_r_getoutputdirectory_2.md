---
title: "getOutputDirectory(DisciplineObject discObject, boolean create)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_getoutputdirectory_2.htm"
file: "refscripting_r_getoutputdirectory_2"
category: "refscripting"
---

# getOutputDirectory(DisciplineObject discObject, boolean create)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  getOutputDirectory(DisciplineObject discObject, boolean create) Returns an org.eclipse.core.runtime.IFolder object as a result. In the event of an error, an exception is thrown. getOutputDirectory(DisciplineObject discObject, boolean create) throws CoreException  
---  
Argument | DisciplineObject | discObject | Discipline object for which a folder should be determined.  
Boolean | create | true = creates a directory if does not exist.  
false = does not create a directory.  
Return value | Object | IFolder | IFolder object  
Exception error | CoreException |  | The status object of the exception error.  
Plug-in |  com.mind8.mechatronic.skill.api.IUtilAPI org.eclipse.core.runtime.CoreException  
The IFolder object can be used, for example, to determine the path using the following method. [Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.getOutputDirectory2) determines the working directory for the selected discipline root. The IUtilAPI.DEFAULT.getOutputDirectory(obj, createDir) method determines the working directory of the discipline root (see row 20). The getLocation().toOSString() method converts the determined working directory into a string in the notation of the operating system (see row 21). Information and possible errors are output in the message log (see rows 7, 11, 20, 23 and 28).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import org.eclipse.core.runtime.CoreException;
    import com.mind8.mechatronic.skill.api.IUtilAPI;
    
    String scriptName = "getOutputDirectory2";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    
    try{
    	info = "obj: "+ obj;
    	UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    	
    	Boolean createDir = true;
    	info = "createDir: "+ createDir;
    	UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    	
    	droot = IUtilAPI.DEFAULT.getOutputDirectory(obj, createDir);
    	outputDirectory = droot.getLocation().toOSString();
    	info = "outputDirectory: "+ outputDirectory;
    	UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    }
    catch(CoreException ce){
    	UserMessageCollector.addError(LIBRARY,'self',null,"Scripting",ce);
    	return;
    }
    finally{
    	String info = "### End of script '" + scriptName + "' ###";
    	UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    }

Result: Applied to the discipline root Feeder_Extended1.Mechatronic.ECAD of the tutorial, the SelectionAction outputs the working directory of the discipline ECAD.
    
        ### Start of script 'getOutputDirectory2' ###
    obj: <<ECAD>>
    createDir: true
    outputDirectory: E:\Users\Public\EPLAN\EngineeringConfiguration\2025\workspace_SCRIPTING\Feeder_Extended1\ECAD
    ### End of script 'getOutputDirectory2' ###

Read more
     * Eclipse Help for IFolder
