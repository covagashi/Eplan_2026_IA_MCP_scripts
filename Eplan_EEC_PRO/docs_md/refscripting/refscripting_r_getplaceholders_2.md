---
title: "getPlaceholders(String absoluteTypeName)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_getplaceholders_2.htm"
file: "refscripting_r_getplaceholders_2"
category: "refscripting"
---

# getPlaceholders(String absoluteTypeName)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  getPlaceholders(String absoluteTypeName) Returns a list of all placeholders in this mechatronic component, where classes of the specified type can be placed. The method is executed directly on the component. getPlaceholders(String absoluteTypeName)  
---  
Argument | String | absoluteTypeName | Absolute name of the limited type  
Return value | List | List of placeholders  
Exception error |  |   
Plug-in |   
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.getPlaceholders2) determines all the placeholders on which instances can be installed and that implement the ISchematicPage interface. For the example, the SelectionAction getPlaceholders2 has to be executed on the Feeder project component. The getPlaceholders() method provides a list of all placeholders under the current project component (see row 7). Information is output in the message log (see rows 5, 10 and 13).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    
    String scriptName = "getPlaceholders2";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // Determine placeholders for selected object
    placeholders = obj.getPlaceholders("T_Interfaces.ISchematicPage");
    info = "placeholders: " +  placeholders;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    info = "### End of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);

Result: The SelectionAction determines an extension point applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial.
    
        ### Start of script 'getPlaceholders2' ###
    placeholders: [<<SchematicPages>>]
    ### End of script 'getPlaceholders2' ###
