---
title: "getGlobalResourcePath()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_iutilapi_getglobalresourcepath.htm"
file: "refscripting_r_iutilapi_getglobalresourcepath"
category: "refscripting"
---

# getGlobalResourcePath()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  getGlobalResourcePath() Determine the path to the global resources. The path to the global resources is specified in the initialization file (*.ini) (see [de.eplan.eec.global.resourcePath](admin_r_vmargs_global_resourcePath_new.htm)). getGlobalResourcePath()  
---  
Argument |  |  |   
Return value | String |  | Path to the global resources.  
Exception error |  |   
Plug-in | com.mind8.mechatronic.skill.api.IUtilAPI  
[Example code for local EEC environment](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.getGlobalResourcePath1) determines the path to the global resources and outputs it in the User Message Collector. The system.getProperty("en.eplan.eec.global.resourcePath") method determines the setting for the path to the global resources (see row 7). Information and possible errors are output in the message log (see rows 5, 11, 15 and 19).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    
    String scriptName = "getGlobalResourcePath";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    
    String globalResourcePath = System.getProperty("de.eplan.eec.global.resourcePath");
    
    if (globalResourcePath == null){
    	info = "Global resource path not set.";
    	UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    }
    else{
    	info = "Global resource path: " + globalResourcePath;
    	UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    }
    
    info = "### End of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);

Result: The SelectionAction outputs the following messages when applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial:
    
        ### Start of script 'getGlobalResourcePath'  ###
    Global resource path: ../resources/ecad/tutorial/p8
    ### End of script 'getGlobalResourcePath' ###

[Sample code for Job Server environment](javascript:void\(0\);)
    
        import com.mind8.mechatronic.skill.api.IUtilAPI;
    String path = IUtilAPI.DEFAULT.getGlobalResourcePath();
