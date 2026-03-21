---
title: "sortPlaceholderObjects(String placeholderName, String sortedByFormula)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_sortplaceholderobjects_2.htm"
file: "refscripting_r_sortplaceholderobjects_2"
category: "refscripting"
---

# sortPlaceholderObjects(String placeholderName, String sortedByFormula)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  sortPlaceholderObjects(String placeholderName, String sortedByFormula) Sorts the instances on the placeholder named placeholderName according to the result of the sortedByFormula. The formula has the same form as the List.sortedBy(sortedByFormula) formula in the formula language. sortPlaceholderObjects (string placeholderName, string sortedByFormula) throws EvaluationException PlaceholderNotExistingException  
---  
Argument | String | placeholderName | The name of the placeholder of the component.  
String | sortedByFormula | A valid formula, which returns a sortedBy formula expression  
Return value |  |   
Exception | EvaluationException |  | The specified formula is invalid.  
PlaceholderNotExistingException |  | The specified placeholder does not exist at the specified project component.  
Plug-in |  com.mind8.mechatronic.skill.api.PlaceholderNotExistingException com.mind8.expressionparser.EvaluationException  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.sortPlaceholderObjects2) sorts the project components of the type Axis on the placeholder Axis of the project component Move. The getPlaceholderObjects method determines the order of the project components on the Axis placeholder before and after sorting (see rows 22 and 35). The method sortPlaceholderObjects sorts project components installed in the placeholder Axis with the formula (x | x.name) (see row 22). Information and possible errors are output to the UserMessageCollector (see rows 7, 19, 28, 32, 38, 41 and 44).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.api.PlaceholderNotExistingException;
    import com.mind8.expressionparser.EvaluationException;
    
    String scriptName = "sortPlaceholderObjects2";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    logText1 = "Script error: Cannot sort objects of the given placeholder due to a formula error: "
    
    try{
    	// Determine placeholders for selected object
    	placeholder = obj.getPlaceholders().get(0);
    	placeholderName  = placeholder.name();
    	info = "Placeholder name: " + placeholderName;
    	UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    	
    	listBefore = obj.getPlaceholderObjects(placeholderName);
    	obj.sortPlaceholderObjects(placeholderName,"x | x.name");
    	
    	// save the change
    	uow.saveChanges();
    }
    catch (EvaluationException ex){
    	UserMessageCollector.addError(LIBRARY, self, null, "Scripting", logText1 + ex);
    	return;
    }
    catch (PlaceholderNotExistingException pne){
    	UserMessageCollector.addError(LIBRARY, self, null, "Scripting", pne);
    	return;
    }
    listAfter = obj.getPlaceholderObjects(placeholderName);
    
    info = "listBefore: " + listBefore;
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    
    info = "listAfter: " + listAfter;
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    
    info = "### End of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder.Move of the tutorial, the instances on the placeholder Axes are sorted in alphanumeric order and the following messages are output:
    
        ### Start of script 'sortPlaceholderObjects2' ###
    Placeholder name: Axes
    listBefore: [<<Axis>>, <<Axis3>>, <<Axis2>>, <<Axis4>>]
    listAfter: [<<Axis2>>, <<Axis>>, <<Axis3>>, <<Axis4>>]
    ### End of script 'sortPlaceholderObjects2' ###
