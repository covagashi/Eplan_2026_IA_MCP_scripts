---
title: "getPlaceholderNames(TypeClass type)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_getplaceholdernames_3.htm"
file: "refscripting_r_getplaceholdernames_3"
category: "refscripting"
---

# getPlaceholderNames(TypeClass type)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  getPlaceholderNames(TypeClass type) Provides a list of all placeholders of a project component for the specified type. The method is executed directly on the component. getPlaceholderNames(TypeClass type)  
---  
Argument | TypeClass | type | Limited type  
Return value | List | List of placeholders  
Exception error |  |   
Plug-in | com.mind8.mechatronic.skill.eos.TypeClass  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.getPlaceholderNames3) determines all the placeholders on which instances can be installed and that implement the ISchematicPage interface. For the example, the SelectionAction getPlaceholderNames2 has to be executed on the Feeder project component. The getPlaceholderNames() method provides a list of all names of the placeholders under the current project component (see row 13). Information is output in the message log (see rows 5, 10 and 13).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.eos.TypeClass;
    
    String scriptName = "getPlaceholderNames3";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    
    // Determine placeholder names for selected object
    String placeholderType = "T_Interfaces.ISchematicPage";
    info = "placeholderType: " +  placeholderType;
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    
    placeholderNames = obj.getPlaceholderNames(placeholderType);
    info = "placeholderNames: " +  placeholderNames;
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    
    info = "### End of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial, the SelectionAction determines the names of all the placeholders directly in the current project component.
    
        ### Start of script 'getPlaceholderNames3' ###
    placeholderType: T_Interfaces.ISchematicPage
    placeholderNames: [SchematicPages]
    ### End of script 'getPlaceholderNames3' ###
