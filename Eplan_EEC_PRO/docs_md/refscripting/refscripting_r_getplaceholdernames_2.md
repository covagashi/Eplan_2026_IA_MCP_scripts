---
title: "getPlaceholderNames(String absoluteTypeName)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_getplaceholdernames_2.htm"
file: "refscripting_r_getplaceholdernames_2"
category: "refscripting"
---

# getPlaceholderNames(String absoluteTypeName)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  getPlaceholderNames(String absoluteTypeName) Returns a list of names of all placeholders in this mechatronic component, where classes of the specified type name can be placed. The method is executed directly on the component. getPlaceholderNames(String absoluteTypeName)  
---  
Argument | String | absoluteTypeName | Absolute name of the limited type  
Return value | List | List of placeholder names  
Exception error |  |   
Plug-in | com.mind8.mechatronic.skill.eos.TypeClass;  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.getPlaceholderNames3) determines the names all the placeholders on which instances can be installed and that implement the ISchematicPage interface. For the example, the SelectionAction getPlaceholderNames3 has to be executed on the Feeder project component. The getPlaceholderNames() method provides a list of all names of the placeholders under the current project component (see row 16). Information is output in the message log (see rows 6, 14, 18 and 21).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.eos.TypeClass;
    
    String scriptName = "getPlaceholderNames2";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    // Determine placeholder names for selected object
    placeholderNames = obj.getPlaceholderNames(TypeClass.findType(uow,"T_Interfaces.ISchematicPage"));
    info = "placeholderNames: " +  placeholderNames;
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    
    info = "### End of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial, the SelectionAction determines the names of all the placeholders directly in the current project component.
    
        ### Start of script 'getPlaceholderNames2' ###
    placeholderTypeName: T_Interfaces.ISchematicPage
    placeholderNames: [SchematicPages]
    ### End of script 'getPlaceholderNames2' ###
