---
title: "isExtension()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_isextension.htm"
file: "refscripting_r_isextension"
category: "refscripting"
---

# isExtension()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  isExtension() Returns true if the placeholder object is an extension point. isExtension()  
---  
Argument |  |  |   
Return value | Boolean | true | Placeholder object is an extension point  
false | Placeholder object is a placeholder  
Exception error |  |   
Plug-in |   
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.isExtension) determines for each instance under the current project component whether it is inserted on an extension point. The obj.getPlaceholders() method determines all placeholders below the current project component (see row 7). A FOR loop iterates across the list of the determined placeholders (see row 9). The isExtension method checks whether the placeholder of the current iteration is an extension point (see row 11). Information is output in the message log (see rows 5, 13 and 18).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    
    String scriptName = "isExtension";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    placeholders = obj.getPlaceholders();
    
    for (iter = placeholders.iterator();iter.hasNext(); ) {
    	placeholders = iter.next();
    	if (placeholders.isExtension()) {
    		info = "Extension: " + placeholders;
    		UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    	}
    }
    
    info = "### End of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial, the SelectionAction determines all extension points directly below Feeder.
    
        ### Start of script 'isExtension' ###
    Placed on extension: <<M_Schematic>>
    Placed on extension: <<M_SchematicPage>>
    Placed on extension: <<M_SchematicPage2>>
    ### End of script 'isExtension' ###
