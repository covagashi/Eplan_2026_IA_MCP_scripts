---
title: "updateExtensions(Object obj)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_updateextensions_1.htm"
file: "refscripting_r_updateextensions_1"
category: "refscripting"
---

# updateExtensions(Object obj)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  updateExtensions(Object obj) Updates all extension points under the specified object. This can be a mechatronic component, Engineering.MechatronicRoot or a placeholder. updateExtensions(Object obj) throws PlaceholderNotExistingException  
---  
Argument | Object | obj | A mechatronic component, MechatronicRoot or placeholder, for which the extension points should be updated.  
Return value |  |   
Exception error | PlaceholderNotExistingException |  | The specified placeholder does not exist at the specified project component.  
Plug-in |  com.mind8.mechatronic.skill.api.PlaceholderNotExistingException com.mind8.mechatronic.skill.api.IMechatronicExtensionsAPI  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
     * With the call Extensions > Remove extensions all instances on extension points of the project Feeder_Extended1 have been removed.
The following script example (ScriptingExamples.updateExtensions1) updates all extension points of the project Feeder_Extended1. For the example the SelectionAction updateExtensions1 has to be executed on the mechatronic root of the project, for example Feeder_Extended1.Mechatronic. The updateExtensions(obj) method updates the extension points of the transferred mechatronic root (see row 19). The uow.saveChanges() method is used to make the change effective in the Unit-Of-Work in the project (see row 22). The output of information and errors is carried out in the message log (see rows 8, 29, 34 and 37).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.api.PlaceholderNotExistingException;
    import com.mind8.mechatronic.skill.api.IMechatronicExtensionsAPI;
    import java.util.ArrayList;
    
    String scriptName = "updateExtensions1";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    
    // Global variables
    List children = new ArrayList();
    Integer numberOfChildren;
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    try{
    	// Update extension points
    	IMechatronicExtensionsAPI.DEFAULT.updateExtensions(obj);
    	
    	// save the change
    	uow.saveChanges();
    	
    	// Gather all children of project
    	children = obj.getRmos();
    	numberOfChildren = children.size();
    }
    catch(PlaceholderNotExistingException pne){
    	UserMessageCollector.addError(LIBRARY, self, null, "Scripting", pne);
    	return;
    }
    finally{
    	info = "numberOfChildren: " + numberOfChildren;
    	UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    	
    	info = "### End of script '" + scriptName + "' ###";
    	UserMessageCollector.addInfo(PROJECT,'self',null,'Scripting',info);
    }

Result: Applied to the project component Feeder_Extended1.Mechatronic of the tutorial, the SelectionAction updates all extension points of the project. The difference to the method updateExtensionsOneLevel is evident from the number of project components (see [updateExtensionsOneLevelOnly(Object obj)](refscripting_r_updateextensionsonelevelonly_1.htm)).
    
        ### Start of script 'updateExtensions1' ###
    numberOfChildren: 361
    ### End of script 'updateExtensions1' ###
