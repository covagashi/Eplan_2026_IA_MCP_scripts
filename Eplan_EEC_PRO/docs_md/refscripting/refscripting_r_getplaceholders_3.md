---
title: "getPlaceholders(TypeClass type)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_getplaceholders_3.htm"
file: "refscripting_r_getplaceholders_3"
category: "refscripting"
---

# getPlaceholders(TypeClass type)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  getPlaceholders(TypeClass type) Returns a list of all placeholders in this mechatronic component, where classes of the specified type can be placed. The method is executed directly on the component. getPlaceholders(TypeClass type)  
---  
Argument | TypeClass | type | Limited type  
Return value | List | List of placeholders  
Exception error |  |  |   
Plug-in | com.mind8.mechatronic.skill.eos.TypeClass  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.getPlaceholders3) determines all placeholders of a project component. For the example, the SelectionAction getPlaceholders3 has to be executed on the Feeder project component. The getPlaceholders() method provides a list of all placeholders under the current project component (see row 12). Information is output in the message log (see rows 6, 14 and 17).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.eos.TypeClass;
    
    String scriptName = "getPlaceholders3";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    // Determine placeholders for selected object
    placeholders = obj.getPlaceholders(TypeClass.findType(uow, "T_Interfaces.ISchematicPage"));
    info = "placeholders: " +  placeholders;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    info = "### End of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial, the SelectionAction determines the value of the parameter Option_Inspect_available and then inverts it.
    
        ### Start of script 'getPlaceholders3' ###
    placeholders: [<<SchematicPages>>]
    ### End of script 'getPlaceholders3' ###
