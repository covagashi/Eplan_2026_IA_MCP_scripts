---
title: "Catch formula errors"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_formula_error_handling.htm"
file: "refscripting_r_formula_error_handling"
category: "refscripting"
---

# Catch formula errors

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Catch formula errors Formula errors for a mechatronic object formula error cause the script to be canceled without handling. To avoid this and to handle the formula error within the script, the 'EvaluationException' is caught. [Example code for EvaluationException():](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.evaluateException) generates an exception error. The formula string formula = 'mc.Â§M_Schematic.$Reports'; is to determine the value of the parameter report, but this parameter does not exist (see row 9). In the branch try{} the method plant = obj.evaluate(formula); executes the formula and generates an exception error (see row 13). The exception error is caught in the catch{} branch and output as an error message in the message log (see row 17). To complete the script, for example, a default value can be set and, if necessary, returned (see rows 20 and 27).
    
        import com.mind8.expressionparser.EvaluationException;
    import org.foederal.util.ui.messages.UserMessageCollector;
    
    String scriptName = "evaluateExeption";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    Object plant;
    String formula = 'mc.Â§M_Schematic.$Reports';
    
    try{
    	UserMessageCollector.addInfo(PROJECT,self,null,"Scripting","Trying to evaluate '$formula'");
    	plant = obj.evaluate(formula);
    }
    catch(EvaluationException e){
    	// reaction on the thrown exception
    	UserMessageCollector.addError(LIBRARY,self,null,"Scripting","Exeption occurred: " + e);
    	
    	// Default-Werte initialisieren
    	plant = null;
    }
    if (plant == null){
    	info = "### End of script '" + scriptName + "' ###";
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    	
    	// maybe return a value, if the method has a return type
    	return;
    }

Result: Applied to the project component Feeder.Mechatronic.Feeder.Move of the tutorial, the SelectionAction supplies an error message in the message log:
    
        ### Start of script 'evaluateExeption' ###
    Trying to evaluate 'mc.Â§M_Schematic.$Reports'
    Exeption occurred: com.mind8.expressionparser.EvaluationException: Invoking method '$Reports' on object '<<M_Schematic>>' failed.
    ### End of script 'evaluateExeption' ###
