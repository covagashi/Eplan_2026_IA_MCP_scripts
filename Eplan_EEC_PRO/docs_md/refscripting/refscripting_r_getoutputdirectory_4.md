---
title: "getOutputDirectory(IProject project, boolean create)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_getoutputdirectory_4.htm"
file: "refscripting_r_getoutputdirectory_4"
category: "refscripting"
---

# getOutputDirectory(IProject project, boolean create)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  getOutputDirectory(IProject project, boolean create) Returns an org.eclipse.core.resources.IContainer object as a result. In the event of an error, an exception is thrown. getOutputDirectory(IProject project, boolean create) throws CoreException  
---  
Argument | IProject | project | Project object  
Boolean | create | true = creates a directory if does not exist.  
false = does not create a directory.  
Return value | Object | IContainer | Project folder in the workspace.  
Exception error | CoreException | The status object of the exception error.  
Plug-in | com.mind8.mechatronic.skill.AbsoluteNameUtil  
The IContainer object can be used, for example, to determine the path using the following method. [Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.getOutputDirectory4) determines the working directory for the selected discipline component. The method obj.getProject() determines the project for discipline component (see row 10). The IUtilAPI.DEFAULT.getOutputDirectory(project,createDir) method determines the work directory of the discipline (see row 18). Information and possible errors are output in the message log (see rows 7, 12, 16, 21, 24 and 29).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import org.eclipse.core.runtime.CoreException;
    import com.mind8.mechatronic.skill.api.IUtilAPI;
    
    String scriptName = "getOutputDirectory4";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    
    try{
    	project = obj.getProject();
    	info = "project: "+ project;
    	UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    	
    	Boolean createDir = true;
    	info = "createDir: "+ createDir;
    	UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    	
    	droot = IUtilAPI.DEFAULT.getOutputDirectory(project,createDir);
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

Result: Applied to the project component Feeder_Extended1.Mechatronic.ECAD.Schematic_Feeder_M_Schematic.Page_Feeder_M_SchematicPage of the tutorial, the SelectionAction outputs the working directory of the discipline ECAD.
    
        ### Start of script 'getOutputDirectory4' ###
    project: <<Feeder_Extended1>>
    createDir: true
    outputDirectory: E:\Users\Public\EPLAN\EngineeringConfiguration\2025\workspace_SCRIPTING\Feeder_Extended1\ECAD
    ### End of script 'getOutputDirectory4' ###

Read more
     * Eclipse help for IContainer
