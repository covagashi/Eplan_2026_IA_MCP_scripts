---
title: "evaluate(String formula)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_evaluate.htm"
file: "refscripting_r_evaluate"
category: "refscripting"
---

# evaluate(String formula)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  evaluate(String formula) The evaluate method calculates a formula for a mechatronic object. The return value is the result of the formula. Results of the Integer and Double types are returned as objects and not as primitive types (for example, java.lang.double and not double). A conversion to the String type is therefore required. evaluate(String formula)  
---  
Argument | String | formula | Formula for a mechatronic object  
Return value | String | Result of formula  
Exception |  |  |   
Plug-in |  |  |   
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.evaluateParameterValue) determines a value that is stored in the ISensors parameter of the mechatronic component Feeder. The formula mroot.$Sensors.size().toString() to be executed is first saved as a string in the variables formula (see row 16). The method string sensors = obj.evaluate(formula); calculates the parameter value and converts it into a string (see row 20). The method objectName.getParameter(parameterName).setPrettyValue(Sensors); stores the determined value in the parameter ISensors of the mechatronic component Feeder (see row 32). The uow.saveChanges()'); method saves the change to the Unit-Of-Work in the project (see row 36). Information and possible errors are output to the message log and to the console (see rows 9, 18, 22, 27, 31, 39 and 43).
    
        import org.foederal.eobroker.core.IUnitOfWork;
    import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.expressionparser.EvaluationException;
    import org.foederal.eobroker.core.IEngineeringObject;
    import com.mind8.mechatronic.skill.AbsoluteNameUtil;
    
    String scriptName = "evaluateParameterValue";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT,'self',null,'Scripting',info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    try{
    	// evaluate the value like the parameter $ISensors does regularly
    	String formula = 'mroot.$Sensors.size().toString()';
    	info = "formula: " + formula;
    	UserMessageCollector.addInfo(PROJECT,'self',null,'Scripting',info);
    									
    	String sensors = obj.evaluate(formula);
    	info = "sensors: " + sensors;
    	UserMessageCollector.addInfo(PROJECT,'self',null,'Scripting',info);
    	
    	String absName = "Feeder_Extended1.Mechatronic.Feeder";
    	objectName = AbsoluteNameUtil.getObjectByAbsolutePath(absName,uow);
    	info = "objectName: " + objectName;
    	UserMessageCollector.addInfo(PROJECT,'self',null,'Scripting',info);
    	
    	String parameterName = "ISensors";
    	info = "parameterName: " + parameterName;
    	UserMessageCollector.addInfo(PROJECT,'self',null,'Scripting',info);
    	
    	objectName.getParameter(parameterName).setPrettyValue(sensors);
    	
    	// save the change
    	uow.saveChanges();
    }
    catch (EvaluationException ex){
    	UserMessageCollector.addError(LIBRARY,'self',null,'Scripting',ex);
    }
    finally{
    	info = "### End of script '" + scriptName + "' ###";
    	UserMessageCollector.addInfo(PROJECT,'self',null,'Scripting',info);
    }

Result: Applied to the component Feeder_Extended1.Mechatronic.Feeder of the tutorial, the script calculates the value of the formula mroot.$Sensors.size().toString() and stores it in the ISensors parameter.
    
        ### Start of script 'evaluateParameterValue' ###
    formula: mroot.$Sensors.size().toString()
    sensors: 23
    objectName: <<Feeder>>
    parameterName: ISensors
    ### End of script 'evaluateParameterValue' ###
