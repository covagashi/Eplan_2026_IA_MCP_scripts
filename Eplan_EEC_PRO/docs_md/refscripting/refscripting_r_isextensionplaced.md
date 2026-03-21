---
title: "isExtensionPlaced()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_isextensionplaced.htm"
file: "refscripting_r_isextensionplaced"
category: "refscripting"
---

# isExtensionPlaced()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  isExtensionPlaced() Returns true if the instance is mounted on an extension point. isExtensionPlaced()  
---  
Argument |  |  |   
Return value | Boolean | true | Instance is installed on an extension point  
false | Instance is installed on a placeholder  
Exception error |  |   
Plug-in |   
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.isExtensionPlaced) determines for each instance under the current project component whether it is inserted on an extension point. The obj.getMos() method determines all project components directly below the current project component (see row 7). A FOR loop iterates across the list of the determined project components (see row 9). The isExtensionPlaced method checks whether the project component of the current iteration is inserted on an extension point (see row 10). Information is output in the message log (see rows 5, 12 and 17).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    
    String scriptName = "isExtensionPlaced";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    objects = obj.getMos();
    for (iter = objects.iterator();iter.hasNext(); ) {
    	object = iter.next();
    	if(object.isExtensionPlaced()) {
    		info = "Placed on extension: " + object;
    		UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    	}
    }
    
    info = "### End of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial, the SelectionAction determines all extension points of the project directly below Feeder.
    
        ### Start of script 'isExtensionPlaced' ###
    Placed on extension: <<M_Schematic>>
    Placed on extension: <<M_SchematicPage>>
    Placed on extension: <<M_SchematicPage2>>
    ### End of script 'isExtensionPlaced' ###
