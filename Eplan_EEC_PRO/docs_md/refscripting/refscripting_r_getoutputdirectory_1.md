---
title: "getOutputDirectory(DisciplineObject discObject)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_getoutputdirectory_1.htm"
file: "refscripting_r_getoutputdirectory_1"
category: "refscripting"
---

# getOutputDirectory(DisciplineObject discObject)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  getOutputDirectory(DisciplineObject discObject) Returns a string that contains the path to the work directory of the discipline in the workspace. In the event of an error, an exception is thrown. getOutputDirectory(DisciplineObject discObject) throws CoreException  
---  
Argument | DisciplineObject | discObject | Discipline object for which a folder should be determined.  
Return value | String | Path to the folder of the output data.  
Exception error | CoreException | The status object of the exception error.  
Plug-in |  com.mind8.mechatronic.skill.AbsoluteNameUtil com.mind8.mechatronic.skill.api.IUtilAPI org.eclipse.core.runtime.CoreException |  | com.mind8.mechatronic.skill.AbsoluteNameUtil  
The path to the work directory differs depending on whether a desktop or Job Server installation has been performed. [Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.getOutputDirectory1) determines the working directory for the selected discipline component. The obj.getDroot().parent.getAbsoluteName() method determines the path to the root component of the associated discipline (see row 14). The AbsoluteNameUtil.getObjectByAbsolutePath(disciplineRoot, uow) method determines the object of the root component (see row 18). The IUtilAPI.DEFAULT.getOutputDirectory(droot) method determines the work directory of the discipline (see row 22). Information and possible errors are output in the message log (see rows 8, 16, 20, 24, 27 and 32).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import org.eclipse.core.runtime.CoreException;
    import com.mind8.mechatronic.skill.AbsoluteNameUtil;
    import com.mind8.mechatronic.skill.api.IUtilAPI;
    
    String scriptName = "getOutputDirectory1";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    try{
    	disciplineRoot = obj.getDroot().parent.getAbsoluteName();
    	info = "disciplineRoot: "+ disciplineRoot;
    	UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    	
    	droot = AbsoluteNameUtil.getObjectByAbsolutePath(disciplineRoot, uow);
    	info = "droot: "+ droot;
    	UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    	
    	outputDirectory = IUtilAPI.DEFAULT.getOutputDirectory(droot);
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
    
        ### Start of script 'getOutputDirectory1' ###
    disciplineRoot: Feeder_Extended1.ECAD
    droot: <<ECAD>>
    outputDirectory: E:\Users\Public\EPLAN\EngineeringConfiguration\2025\workspace_SCRIPTING\Feeder_Extended1\ECAD
    ### End of script 'getOutputDirectory1' ###
