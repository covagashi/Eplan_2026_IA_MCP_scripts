---
title: "getPlaceholders()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_getplaceholders_1.htm"
file: "refscripting_r_getplaceholders_1"
category: "refscripting"
---

# getPlaceholders()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  getPlaceholders() Returns a list of names of all placeholders in the mechatronic project component. The method is executed directly on the component. getPlaceholders()  
---  
Argument |  |  |   
Return value | List | List of placeholders  
Exception error |  |   
Plug-in |   
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.getPlaceholders1) determines all placeholders of a project component. For the example, the SelectionAction getPlaceholders1 has to be executed on the Feeder project component. The getPlaceholders() method provides a list of all placeholders under the current project component (see row 9). Information is output in the message log (see rows 5, 10 and 13).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    
    String scriptName = "getPlaceholders1";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    
    // Determine placeholders for selected object
    placeholders = obj.getPlaceholders();
    info = "placeholders: " +  placeholders;
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    
    info = "### End of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial, the SelectionAction determines the value of the parameter Option_Inspect_available and then inverts it.
    
        ### Start of script 'getPlaceholders1' ###
    placeholders: [<<Schematic>>, <<SchematicPages>>, <<Mover>>]
    ### End of script 'getPlaceholders1' ###
