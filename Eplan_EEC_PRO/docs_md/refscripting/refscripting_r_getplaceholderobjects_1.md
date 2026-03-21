---
title: "getPlaceholderObjects(String placeholderName)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_getplaceholderobjects_1.htm"
file: "refscripting_r_getplaceholderobjects_1"
category: "refscripting"
---

# getPlaceholderObjects(String placeholderName)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  getPlaceholderObjects(String placeholderName) Returns a list of all objects, which are placed on the placeholder with the name placeholderName in this mechatronic component. The method is executed directly on the component. getPlaceholderObjects(string placeholderName) throws PlaceholderNotExistingException  
---  
Argument | String | placeholderName | The name of the placeholder of the component.  
Return value | List | List of mechatronic objects  
Exception error | PlaceholderNotExistingException |  | The specified placeholder does not exist at the specified project component.  
Plug-in | com.mind8.mechatronic.skill.api.PlaceholderNotExistingException  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.getPlaceholderObjects1) finds the names of all project components that are installed in the specified placeholder. For the example the SelectionAction getPlaceholderObjects1 has to be executed on the Feeder project component. The getPlaceholderObjects method provides a list of all project components that are installed in the placeholder of the specified name (see rows 8 and 14). Errors and information are output in the message log (see rows 6, 10, 16, 20 and 24).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.api.PlaceholderNotExistingException;
    
    String scriptName = "getPlaceholderObjects1";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    
    String placeholderName = "SchematicPages";
    info = "placeholderName: " +  placeholderName;
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    
    try{
    	// Determine objects on placeholder with given name
    	objects = obj.getPlaceholderObjects(placeholderName);
    	info = "objects: " +  objects;
    	UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    }
    catch(PlaceholderNotExistingException ex){
    	info = "Error: " + ex;
    	UserMessageCollector.addError(PROJECT, self, null, "Scripting", info);
    }
    
    info = "### End of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial, the SelectionAction determines all instances that are installed into the placeholder SchematicPages.
    
        ### Start of script 'getPlaceholderObjects1' ###
    placeholderName: SchematicPages
    objects: [<<M_SchematicPage>>, <<M_SchematicPage2>>]
    ### End of script 'getPlaceholderObjects1' ###
