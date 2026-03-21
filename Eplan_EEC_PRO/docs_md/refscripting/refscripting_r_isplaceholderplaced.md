---
title: "isPlaceholderPlaced()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_isplaceholderplaced.htm"
file: "refscripting_r_isplaceholderplaced"
category: "refscripting"
---

# isPlaceholderPlaced()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  isPlaceholderPlaced() Returns true if the instance is mounted on a placeholder or an extension point. Note To differentiate between instances on placeholders and extension points, isExtensionPlaced() is used. isPlaceholderPlaced()  
---  
Argument |  |  |   
Return value | Boolean | true | Instance is installed on a placeholder or an extension point  
false | Instance is integrated directly  
Exception error |  |   
Plug-in |   
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.isPlaceholderPlaced), applied to Feeder_Extended1.Mechatronic.Feeder determines for each instance under the current project component whether it is inserted on a placeholder or an extension point. In order to find instances on placeholders at all, two instances of T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Axis are manually integrated on the placeholder Feeder_Extended1.Mechatronic.Feeder.Move.Axes for this example. The obj.getRmos() method determines all project components below the current project component (see row 7). A FOR loop iterates across the list of the determined project components (see row 8). The isPlaceholderPlaced method checks whether the project component of the current iteration is inserted on a placeholder or extension point (see row 10). The isExtensionPlaced method then provides a query as to whether the instance is inserted into an extension point (see row 11). Information is output in the message log (see rows 5, 16 and 22).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    
    String scriptName = "isPlaceholderPlaced";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    objects = obj.getRmos();
    for (iter = objects.iterator();iter.hasNext(); ) {
    	object = iter.next();
    	if(object.isPlaceholderPlaced()) {
    		if(object.isExtensionPlaced()) {
    			// no output for instances placed on extensions
    		}
    		else {
    			info = "Placed on placeholder: " + object;
    			UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    		}
    	}
    }
    
    info = "### End of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial, the SelectionAction determines all extension points of the project directly below Feeder.
    
        ### Start of script 'isPlaceholderPlaced' ###
    Placed on placeholder: <<Axis>>
    Placed on placeholder: <<Axis2>>
    ### End of script 'isPlaceholderPlaced' ###

Read more
     * [isExtensionPlaced()](refscripting_r_isextensionplaced.htm)
