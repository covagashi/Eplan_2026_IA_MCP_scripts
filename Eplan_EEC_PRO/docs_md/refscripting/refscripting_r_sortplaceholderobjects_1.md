---
title: "sortPlaceholderObjects(String placeholder, String sortedByFormula)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_sortplaceholderobjects_1.htm"
file: "refscripting_r_sortplaceholderobjects_1"
category: "refscripting"
---

# sortPlaceholderObjects(String placeholder, String sortedByFormula)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  sortPlaceholderObjects(String placeholder, String sortedByFormula) Sorts the instances on the placeholder placeholder according to the result of the sortedByFormula. The formula has the same form as the List.sortedBy(sortedByFormula) formula in the formula language. sortPlaceholderObjects(Placeholder placeholder, string sortedByFormula) throws EvaluationException  
---  
Argument | Placeholder | placeholder | A placeholder of the component.  
String | sortedByFormula | A valid formula that returns a sortedBy formula expression.  
Return value |  |   
Exception error | EvaluationException |  | The specified formula is invalid.  
PlaceholderNotExistingException |  | The specified placeholder does not exist at the specified project component.  
Plug-in |  com.mind8.expressionparser.EvaluationException com.mind8.mechatronic.skill.api.PlaceholderNotExistingException  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.sortPlaceholderObjects1) sorts the project components of the type Axes on the placeholder Axis of the project component Move. In order for the tutorial project Feeder_Extended1 to contain project components on the placeholder Axes, several instances of T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Axis have to be instantiated manually on the placeholder beforehand. The getPlaceholderObjects method determines the order of the project components on the Axes placeholder before and after sorting (see rows 21 and 34). The method sortPlaceholderObjects sorts project components installed in the placeholder Axes with the formula (x | x.name) (see row 21). Information and possible errors are output to the UserMessageCollector (see rows 7, 18, 27, 31, 37, 40 and 43).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.api.PlaceholderNotExistingException;
    import com.mind8.expressionparser.EvaluationException;
    
    String scriptName = "sortPlaceholderObjects1";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    logText1 = "Script error: Cannot sort objects of the given placeholder due to a formula error: ";
    
    try{
    	// Determine placeholders for selected object
    	placeholder = obj.getPlaceholders().get(0);
    	info = "Placeholder: " + placeholder;
    	UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    	
    	listBefore = obj.getPlaceholderObjects(placeholder.name());
    	obj.sortPlaceholderObjects(placeholder,"x | x.name");
    	
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
    listAfter = obj.getPlaceholderObjects(placeholder.name());
    
    info = "listBefore: " + listBefore;
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    
    info = "listAfter: " + listAfter;
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    
    info = "### End of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder.Move of the tutorial, the instances on the placeholder Axes are sorted in alphanumeric order and the following messages are output:
    
        ### Start of script 'sortPlaceholderObjects1' ###
    Placeholder: <<Axes>>
    listBefore: [<<Axis>>, <<Axis3>>, <<Axis2>>, <<Axis4>>]
    listAfter: [<<Axis2>>, <<Axis>>, <<Axis3>>, <<Axis4>>]
    ### End of script 'sortPlaceholderObjects1' ###
