---
title: "setValue(String string)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_setvalue.htm"
file: "refscripting_r_setvalue"
category: "refscripting"
---

# setValue(String string)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  setValue(String string) Sets any string as a parameter value. setValue(String string)  
---  
Argument | String | string | Any string as a parameter value.  
Return value |  |   
Exception error |  |  |   
Plug-in |  com.mind8.mechatronic.skill.AbsoluteNameUtil  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.setParameterValue1) determines the value of the parameter Option_Inspect_available of the project component Feeder. If the value of the parameter true, it is set to the value false and vice versa. For the example the SelectionAction setParameterValue1 has to be executed on any project component. The name of the project component is specified (see row 12). The name of the parameter is also specified (see row 15). The determination of the mechatronic object is carried out with the method AbsoluteNameUtil.getObjectByAbsolutePath() (see row 22). The getParameter() and getCalculatedValue() methods determine the specified parameter and its value (see row 27). The setValue() method sets the value of the parameter either to true or to false (see rows 33 and 38). The uow.saveChanges() method is used to make the change effective in the Unit-Of-Work in the project (see row 44). Information is output in the message log (see rows 6, 14, 19, 24, 29, 35, 40 and 47).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.AbsoluteNameUtil;
    
    String scriptName = "setParameterValue1";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    // Absolute name of component containing the parameter
    String absName = "Feeder_Extended1.Mechatronic.Feeder";
    info = "absName: " + absName;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // Name of parameter
    String parameterName = "Option_Inspect_available";
    info = "parameterName: " + parameterName;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // Determine the mechatronic component
    objectName = AbsoluteNameUtil.getObjectByAbsolutePath(absName,uow);
    info = "objectName: " + objectName;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // Determine the current parameter value
    parameterValue = objectName.getParameter(parameterName).getCalculatedValue();
    info = "parameterValue: " + parameterValue;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // Toggle the parameter value of parameter "Option_Inspect_available" to "false" if "true" and vice versa
    if(parameterValue == true){
    	objectName.getParameter(parameterName).setValue("false");
    	info = "Parameter set to 'false'";
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    }
    else{
    	objectName.getParameter(parameterName).setValue("true");
    	info = "Parameter set to 'true'";
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    }
    
    // save the change
    uow.saveChanges();
    
    info = "### End of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial, the SelectionAction determines the value of the parameter Option_Inspect_available and then inverts it.
    
        ### Start of script 'setParameterValue1' ###
    absName: Feeder_Extended1.Mechatronic.Feeder
    parameterName: Option_Inspect_available
    objectName: <<Feeder>>
    parameterValue: false
    Parameter set to 'true'
    ### End of script 'setParameterValue1' ###
