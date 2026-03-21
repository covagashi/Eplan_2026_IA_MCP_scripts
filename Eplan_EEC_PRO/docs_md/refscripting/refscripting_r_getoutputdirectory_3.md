---
title: "getOutputDirectory(IProject project)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_getoutputdirectory_3.htm"
file: "refscripting_r_getoutputdirectory_3"
category: "refscripting"
---

# getOutputDirectory(IProject project)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  getOutputDirectory(IProject project) Returns a string that contains the path to the project folder in the workspace. In the event of an error, an exception is thrown. getOutputDirectory(IProject project) throws CoreException  
---  
Argument | IProject | project | Project object  
Return value | String | Path to the project folder in the workspace.  
Exception error | CoreException |  | The status object of the exception error.  
Plug-in |  com.mind8.mechatronic.skill.api.IUtilAPI org.eclipse.core.runtime.CoreException  
The path to the project folder in the workspace. This path differs depending on whether a desktop or job server installation has been performed. [Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.getOutputDirectory3) determines the working directory for the selected discipline component. The IUtilAPI.DEFAULT.getOutputDirectory(project) method finds the working directory of the discipline root (see rows 10 and 14). Information and possible errors are output in the message log (see rows 7, 12, 16, 19 and 24).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import org.eclipse.core.runtime.CoreException;
    import com.mind8.mechatronic.skill.api.IUtilAPI;
    
    String scriptName = "getOutputDirectory3";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    
    try{
    	project = obj.getProject();
    	info = "project: "+ project;
    	UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    	
    	outputDirectory = IUtilAPI.DEFAULT.getOutputDirectory(project);
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

Result: Applied to the project component Feeder_Extended1.Mechatronic.ECAD.Schematic_Feeder_M_Schematic.Page_Feeder_M_SchematicPage of the tutorial, the SelectionAction outputs the working directory of the discipline ECAD.
    
        ### Start of script 'getOutputDirectory3' ###
    project: <<Feeder_Extended1>>
    outputDirectory: E:\Users\Public\EPLAN\EngineeringConfiguration\2025\workspace_SCRIPTING\Feeder_Extended1\ECAD
    ### End of script 'getOutputDirectory3' ###
