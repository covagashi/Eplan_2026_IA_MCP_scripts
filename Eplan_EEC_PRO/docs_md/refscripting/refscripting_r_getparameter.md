---
title: "getParameter(String parameterName)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_getparameter.htm"
file: "refscripting_r_getparameter"
category: "refscripting"
---

# getParameter(String parameterName)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  getParameter(String parameterName) Determines the parameter with the specified name. getParameter(String parameterName)  
---  
Argument | String | parameterName | Name of the parameter  
Return value | EngineeringObject | Result of formula  
Exceptions |  |   
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.getParameterValue) determines the value of the Sensors parameter of the project component Feeder. For the example the SelectionAction getParameterValue can be executed on each project component. The name of the project component is specified (see row 12). The name of the parameter is also specified (see row 17). The determination of the mechatronic object is carried out with the method AbsoluteNameUtil.getObjectByAbsolutePath() (see row 22). The getParameter() and getCalculatedValue() methods determine the specified parameter and its value (see row 27). Information is output in the message log (see rows 6, 14, 19, 24, 29 and 32).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.AbsoluteNameUtil;
    
    String scriptName = "getParameterValue";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    // Absolute name of component containing the parameter
    String absName = "Feeder_Extended1.Mechatronic.Feeder";
    info = "absName: " + absName;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // Name of parameter
    String parameterName = "Sensors";
    info = "parameterName: " + parameterName;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // Determine the mechatronic component
    objectName = AbsoluteNameUtil.getObjectByAbsolutePath(absName,uow);
    info = "objectName: " + objectName;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // Determine the paramter value of parameter "Sensors"
    parameterValue = objectName.getParameter(parameterName).getCalculatedValue();
    info = "parameterValue: " + parameterValue;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    info = "### End of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial, the SelectionAction supplies the value of the parameter Sensor.
    
        ### Start of script 'getParameterValue' ###
    absName: Feeder_Extended1.Mechatronic.Feeder
    parameterName: Sensors
    objectName: <<Feeder>>
    parameterValue: [<<Positionsensor_optical>>, <<Position_1>>, <<Position_2>>, <<Positionsensor_optical>>, <<Position_1>>, <<Position_2>>, <<Position_3>>, <<Position_4>>, <<Position_1>>, <<Pressuresensor>>, <<Position_1>>, <<Position_2>>, <<Position_3>>, <<Position_4>>, <<Position_1>>, <<Position_2>>, <<Position_3>>, <<Position_4>>, <<Position_1>>, <<Position_2>>, <<Position_3>>, <<Position_4>>, <<Position_1>>, <<Position_2>>, <<Position_3>>, <<Position_4>>, <<Position_1>>, <<Pressuresensor>>, <<Position_1>>, <<Position_2>>, <<Position_3>>, <<Position_4>>, <<Position_1>>, <<Pressuresensor>>]
    ### End of script 'getParameterValue' ###
