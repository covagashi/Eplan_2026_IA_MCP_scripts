---
title: "updateExtensionsOneLevelOnly(Object obj)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_updateextensionsonelevelonly_1.htm"
file: "refscripting_r_updateextensionsonelevelonly_1"
category: "refscripting"
---

# updateExtensionsOneLevelOnly(Object obj)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  updateExtensionsOneLevelOnly(Object obj) Updates all extension points under the specified object, but not within existing or new child objects. A mechatronic component, Engineering.MechatronicRoot or a placeholder, is transferred as an argument. updateExtensionsOneLevelOnly(Object obj) throws PlaceholderNotExistingException  
---  
Argument | Object | obj | A mechatronic component, MechatronicRoot or placeholder, for which the extension points should be updated.  
Return value |  |   
Exception error | PlaceholderNotExistingException |  | The specified placeholder does not exist at the specified project component.  
Plug-in |  com.mind8.mechatronic.skill.api.IMechatronicExtensionsAPI com.mind8.mechatronic.skill.api.PlaceholderNotExistingException  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
     * With the call Extensions > Remove extensions all instances on extension points of the project Feeder_Extended1 have been removed.
The following script example (ScriptingExamples.updateExtensionsOneLevel) updates all extension points of the marked mechatronic component of the project Feeder_Extended1 that are directly installed in this component. For the example the SelectionAction updateExtensionsOneLevel has to be executed on the mechatronic root of the project, for example Feeder_Extended1.Mechatronic. The updateExtensionsOneLevelOnly(obj) method only updates the extension points of the transferred mechatronic root (see Row 19). The output of information and errors is carried out in the message log (see rows 8, 29, 33 and 36).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.api.PlaceholderNotExistingException;
    import com.mind8.mechatronic.skill.api.IMechatronicExtensionsAPI;
    import java.util.ArrayList;
    
    String scriptName = "updateExtensionsOneLevel";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    
    // Global variables
    List children = new ArrayList();
    Integer numberOfChildren;
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    try{
    	// Update extension points
    	IMechatronicExtensionsAPI.DEFAULT.updateExtensionsOneLevelOnly(obj);
    
    	// save the change
    	uow.saveChanges();
    
    	// Gather all children of project
    	children = obj.getRmos();
    	numberOfChildren = children.size();
    	}
    catch(PlaceholderNotExistingException pne){
    	UserMessageCollector.addError(PROJECT,'self',null,"Scripting", pne);
    	}
    finally{
    	info = "numberOfChildren: " + numberOfChildren;
    	UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    
    	info = "### End of script '" + scriptName + "' ###";
    	UserMessageCollector.addInfo(PROJECT,'self',null,'Scripting',info);
    }

Result: Applied to the project component Feeder_Extended1.Mechatronic of the tutorial, the SelectionAction only updates the extension points directly under the mechatronic root of the project. The difference to the method updateExtensions is evident from the number of project components (see [updateExtensions(Object obj)](refscripting_r_updateextensions_1.htm)).
    
        ### Start of script 'updateExtensionsOneLevel' ###
    numberOfChildren: 137
    ### End of script 'updateExtensionsOneLevel' ###
