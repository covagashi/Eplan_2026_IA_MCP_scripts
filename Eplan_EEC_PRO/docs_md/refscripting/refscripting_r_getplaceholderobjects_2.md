---
title: "getPlaceholderObjects(Placeholder placeholder)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_getplaceholderobjects_2.htm"
file: "refscripting_r_getplaceholderobjects_2"
category: "refscripting"
---

# getPlaceholderObjects(Placeholder placeholder)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  getPlaceholderObjects(Placeholder placeholder) Returns a list of all objects that are placed on the placeholder placeholder in a mechatronic project component. The method is executed directly on the component. getPlaceholderObjects(Placeholder placeholder) throws PlaceholderNotExistingException  
---  
Argument | Placeholder | placeholder | A placeholder of the component.  
Return value | List | List of mechatronic objects  
Exception error | PlaceholderNotExistingException |  | The specified placeholder does not exist at the specified project component.  
Plug-in | com.mind8.mechatronic.skill.api.PlaceholderNotExistingException  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.getPlaceholderObjects2) finds the names of all project components that are installed in the specified placeholder. For the example, the SelectionAction getPlaceholderObjects2 has to be executed on the Feeder project component. The getPlaceholders method provides a list of all names of the placeholders of the specified type under the current project component. The first entry of the list is adopted with get(0) (see row 14). The getPlaceholderObjects method provides a list of all project components that are installed in the determined placeholder (see row 18). Information and errors are output in the message log (see rows 6, 10, 16, 20, 24 and 28).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.api.PlaceholderNotExistingException;
    
    String scriptName = "getPlaceholderObjects2";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    
    String placeholderType = "T_Interfaces.ISchematicPage";
    info = "placeholderType: " +  placeholderType;
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    
    try{
    	// Determine the placeholder of the given type
    	placeholder = obj.getPlaceholders(placeholderType).get(0);
    	info = "placeholder: " +  placeholder;
    	UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    	
    	objects = obj.getPlaceholderObjects(placeholder);
    	info = "objects: " +  objects;
    	UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    }
    catch (PlaceholderNotExistingException pne){
    	UserMessageCollector.addError(LIBRARY, self, null, "Scripting", pne);
    	return;
    }
    
    info = "### End of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial, the SelectionAction determines all instances that are installed into the placeholder SchematicPages.
    
        ### Start of script 'getPlaceholderObjects2' ###
    placeholderType: T_Interfaces.ISchematicPage
    placeholder: <<SchematicPages>>
    objects: [<<M_SchematicPage>>, <<M_SchematicPage2>>]
    ### End of script 'getPlaceholderObjects2' ###
