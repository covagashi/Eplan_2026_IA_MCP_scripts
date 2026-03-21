---
title: "removeExtensions(Object obj)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_removeextensions.htm"
file: "refscripting_r_removeextensions"
category: "refscripting"
---

# removeExtensions(Object obj)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  removeExtensions(Object obj) Deletes all instances placed on extension points under the specified object. The specified object can be a mechatronic component, Engineering.MechatronicRoot, or a placeholder. removeExtensions(Object obj)  
---  
Argument | Object | obj | A mechatronic component, MechatronicRoot or placeholder, for which the instances that are installed on extension points are to be deleted.  
Return value |  |   
Exception error |  |   
Plug-in | com.mind8.mechatronic.skill.api.IMechatronicExtensionsAPI  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.removeExtensions) removes all project components that are installed on extension points below Feeder_Extended1.Mechatronic.Feeder. In order for the tutorial project Feeder_Extended1 to contain project components on extension points, these are to be instantiated via the popup menu Extensions > Update extensions of Feeder_Extended1.Mechatronic. The removeExtensions(obj) method removes all instances that are installed in extension points (see row 15). Information is output in the UserMessageCollector (see rows 6, 13, 21 and 24).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.api.IMechatronicExtensionsAPI;
    
    String scriptName = "removeExtensions";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    // obj is script argument
    info = "Remove instances from extension of: " + obj;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    IMechatronicExtensionsAPI.DEFAULT.removeExtensions(obj);
    
    // save the change
    uow.saveChanges();
    
    info = "Instances removed";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    info = "### End of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial, all instances on extension points are removed and the following messages are output:
    
        ### Start of script 'removeExtensions' ###
    Remove instances from extension of: <<Feeder>>
    Instances removed
    ### End of script 'removeExtensions' ###
