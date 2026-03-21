---
title: "setPrettyValue(String formula)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_setprettyvalue.htm"
file: "refscripting_r_setprettyvalue"
category: "refscripting"
---

# setPrettyValue(String formula)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  setPrettyValue(String formula) Sets the result of a formula as the parameter value. To set formulas as parameter values, the setPrettyValue() method is used. Thus absolute type names become rugged against renaming the referenced classes. setPrettyValue(String formula)  
---  
Argument | String | string | A formula as a parameter value.  
Return value |  |   
Exception error |  |  |   
Plug-in |  com.mind8.expressionparser.EvaluationException com.mind8.mechatronic.skill.AbsoluteNameUtil  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.setParameterValue2) uses the formula =this.name as the value of the FunctionDesignation parameter. For the example the SelectionAction setParameterValue2 has to be executed on any project component. The name of the project component is specified (see row 14). The name of the parameter is also specified (see row 20). The determination of the mechatronic object is carried out with the method AbsoluteNameUtil.getObjectByAbsolutePath() (see row 15). The setPrettyValue() method sets the value of the parameter to the =this.name formula (see row 25). The uow.saveChanges() method is used to make the change effective in the Unit-Of-Work in the project (see row 30). Information is output in the message log (see rows 7, 17, 22, 27, 35, 38 and 42).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.AbsoluteNameUtil;
    import com.mind8.expressionparser.EvaluationException;
    
    String scriptName = "setParameterValue2";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    try{
    	// Determine the mechatronic component
    	String absName = "Feeder_Extended1.Mechatronic.Feeder";
    	objectName = AbsoluteNameUtil.getObjectByAbsolutePath(absName,uow);
    	info = "objectName: " + objectName;
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    	
    	// Name of parameter
    	String parameterName = "FunctionDesignation";
    	info = "parameterName: " + parameterName;
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    	
    	// Set the parameter value to "=this.name"
    	objectName.getParameter(parameterName).setPrettyValue("=this.name");
    	info = "Parameter value set to '=this.name'";
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    	
    	// save the change
    	uow.saveChanges();
    	
    	// Get the calculated parameter value of FunctionalDesignation
    	calculatedParameterValue = objectName.getParameter(parameterName).getCalculatedValue();
    	info = "calculatedParameterValue: "+ calculatedParameterValue;
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    }
    catch (EvaluationException ex){
    	UserMessageCollector.addError(PROJECT,'self',null,"Error",ex);
    }
    
    info = "### End of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial, the SelectionAction inserts a parameter of the name FunctionDesignation into the project component and sets the formula =this.name as the value. The calculated parameter value Feeder is output additionally.
    
        ### Start of script 'setParameterValue2' ###
    objectName: <<Feeder>>
    parameterName: FunctionDesignation
    Parameter value set to '=this.name'
    calculatedParameterValue: Feeder
    ### End of script 'setParameterValue2' ###
