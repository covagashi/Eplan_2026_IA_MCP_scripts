---
title: "getPlaceholderNames"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_getplaceholdernames_1.htm"
file: "refscripting_r_getplaceholdernames_1"
category: "refscripting"
---

# getPlaceholderNames

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  getPlaceholderNames Returns a list of names of all placeholders in this mechatronic component. The method is executed directly on the component. getPlaceholderNames()  
---  
Argument |  |  |   
Return value | List | List of placeholder names  
Exception error |  |   
Plug-in |   
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.getPlaceholderNames1) determines the names of all placeholders directly in a project component. For the example the SelectionAction getPlaceholderNames1 has to be executed on the Feeder project component. The getPlaceholderNames() method provides a list of all names of the placeholders in the current project component (see row 8). Information is output in the message log (see rows 5, 10 and 13).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    
    String scriptName = "getPlaceholderNames1";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    
    // Determine placeholder names for selected object
    placeholderNames = obj.getPlaceholderNames();
    info = "placeholderNames: " +  placeholderNames;
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    
    info = "### End of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial, the SelectionAction determines the names of all the placeholders directly in the current project component.
    
        ### Start of script 'getPlaceholderNames1' ###
    placeholderNames: [Schematic, SchematicPages, Mover]
    ### End of script 'getPlaceholderNames1' ###
