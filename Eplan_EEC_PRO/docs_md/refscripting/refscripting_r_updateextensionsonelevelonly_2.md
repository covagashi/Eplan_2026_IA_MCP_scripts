---
title: "updateExtensionsOneLevelOnly(Object obj, IMechatronicInstantiationContext context)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_updateextensionsonelevelonly_2.htm"
file: "refscripting_r_updateextensionsonelevelonly_2"
category: "refscripting"
---

# updateExtensionsOneLevelOnly(Object obj, IMechatronicInstantiationContext context)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  updateExtensionsOneLevelOnly(Object obj, IMechatronicInstantiationContext context) Updates all extension points under the specified object, but not within existing or new child objects. obj can be a mechatronic component, Engineering.MechatronicRoot or a placeholder. An instantiation context can be provided for reuse, which makes sense, if several updates should be processed during one script run. It is important, to observe the application of pattern of the example code. updateExtensionsOneLevelOnly(Object obj, IMechatronicInstantiationContext context) throws PlaceholderNotExistingException  
---  
Argument | Object | obj | A mechatronic component, MechatronicRoot or placeholder, for which the extension points should be updated.  
IMechatronicInstantiationContext | context | A reusable context for instantiation.  
Return value |  |   
Exception error | PlaceholderNotExistingException |  | The specified placeholder does not exist at the specified project component.  
Plug-in |  com.mind8.mechatronic.skill.api.PlaceholderNotExistingException com.mind8.mechatronic.skill.api.IMechatronicExtensionsAPI com.mind8.mechatronic.skill.api.IMechatronicInstantiationAPI  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
     * With the call Extensions > Remove extensions all instances on extension points of the project Feeder_Extended1 have been removed.
The following script example (ScriptingExamples.updateExtensionsOneLevelOnly2) updates all extension points of the selected project components. For the example the SelectionAction updateExtensionsOneLevelOnly2 has to be executed on the project components Feeder_Extended1.Mechatronic.Feeder.Insert to Feeder_Extended1.Mechatronic.Feeder.Discard. The method instantiationTarget = objects.get(0) determines the first selected object in order to create a context object (see rows 19 and 20). A loop iterates across the marked objects and updates the direct extension points with the method updateExtensionsOneLevelOnly(instantiationTarget,context) (see row 27). The uow.saveChanges() method is used to make the change effective in the Unit-Of-Work in the project (see row 33). Information and errors are output in the message log (see rows 9, 30, 45, 50 and 53).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.api.PlaceholderNotExistingException;
    import com.mind8.mechatronic.skill.api.IMechatronicExtensionsAPI;
    import com.mind8.mechatronic.skill.api.IMechatronicInstantiationAPI;
    import java.util.ArrayList;
    
    String scriptName = "updateExtensionsOneLevelOnly2";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    
    // Global variables
    List children = new ArrayList();
    Integer numberOfChildren;
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    // create context
    instantiationTarget = objects.get(0);
    context = IMechatronicInstantiationAPI.DEFAULT.createInstantiationContext(instantiationTarget);
    
    try{
    	// Iterate over selected objects to update their extensions one level
    	for (Iterator iterator = objects.iterator(); iterator.hasNext();){
    		obj = iterator.next();
    		
    		IMechatronicExtensionsAPI.DEFAULT.updateExtensionsOneLevelOnly(instantiationTarget,context);
    		
    		info = "Updated extensions of: " + obj;
    		UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    	}
    	// save the change
    	uow.saveChanges();
    	
    	// Gather all children of project
    	if(instantiationTarget != instantiationTarget.getMroot()){
    		children = instantiationTarget.getMroot().getRmos();
    	}
    	else{
    		children = instantiationTarget.getRmos();
    	}
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

Result: Applied to the project components Feeder_Extended1.Mechatronic.Insert to Feeder_Extended1.Mechatronic.Discard of the tutorial, the SelectionAction updates all extension points of these project components. The difference to the method updateExtensions is evident from the number of project components (see [updateExtensions(Object obj)](refscripting_r_updateextensions_1.htm)).
    
        ### Start of script 'updateExtensionsOneLevelOnly2' ###
    Updated extensions of: <<Insert>>
    Updated extensions of: <<Inspect>>
    Updated extensions of: <<Move>>
    Updated extensions of: <<Store>>
    Updated extensions of: <<Discard>>
    numberOfChildren: 63
    ### End of script 'updateExtensionsOneLevelOnly2' ###
