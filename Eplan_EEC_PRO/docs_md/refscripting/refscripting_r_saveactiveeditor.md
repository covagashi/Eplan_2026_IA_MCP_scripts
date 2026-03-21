---
title: "saveActiveEditor()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_saveactiveeditor.htm"
file: "refscripting_r_saveactiveeditor"
category: "refscripting"
---

# saveActiveEditor()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  saveActiveEditor() Saves the current changes in the active editor. saveActiceEditor()  
---  
Argument |  |  |   
Return value |  |   
Exception error |  |   
Plug-in | com.mind8.mechatronic.skill.api.IUtilAPI |  |   
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.saveActiveEditor) saves the changes to the current editor. Here the script example is executed in the Form-UI of the Feeder project component by clicking [Save changes]. The button with these rows is installed in the Form-UI:
    
        <action name="ScriptingExamples.saveActiveEditor" 
    	arguments="=this" 
    	type="button" 
    	text="Save changes">
    </action>

The IUtilAPI.DEFAULT.saveActiveEditor() method saves the editor (see row 8). Information is output in the message log (see rows 6, 10 and 13).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.api.IUtilAPI;
    
    String scriptName = "saveActiveEditor";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    
    IUtilAPI.DEFAULT.saveActiveEditor();
    info = "Editor saved";
    UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    
    info = "### End of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);

Result: The SelectionAction outputs the following messages when applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial:
    
        ### Start of script 'saveActiveEditor'  ###
    Editor saved
    ### End of script 'saveActiveEditor' ###
