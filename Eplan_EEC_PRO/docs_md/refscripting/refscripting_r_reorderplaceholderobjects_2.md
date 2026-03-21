---
title: "reorderPlaceholderObjects(String placeholderName, int srcIndex, int count, int dstIndex)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_reorderplaceholderobjects_2.htm"
file: "refscripting_r_reorderplaceholderobjects_2"
category: "refscripting"
---

# reorderPlaceholderObjects(String placeholderName, int srcIndex, int count, int dstIndex)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  reorderPlaceholderObjects(String placeholderName, int srcIndex, int count, int dstIndex) Reorganizes instances on the placeholder placeholderName in a way that count instances of index srcIndex are moved to dstIndex. reorderPlaceholderObjects(String placeholderName, int srcIndex,int count, int dstIndex) throws IndexOutOfBoundsException PlaceholderNotExistingException  
---  
Argument | String | placeholderName | The name of the placeholder of the component.  
Integer | srcIndex | A valid source index within the placeholder objects.  
Integer | count | The number of objects to be moved  
Integer | dstIndex | A valid destination index within the placeholder objects.  
Return value |  |   
Exception error | EvaluationException |  | The specified formula is invalid.  
IndexOutOfBoundsException |  | The given index is outside the valid range:  
-1 < srcIndex < getPlaceholderObjects(placeholder).size() and dstIndex + count < getPlaceholderObjects(placeholder).size()  
PlaceholderNotExistingException |  | The specified placeholder does not exist at the specified project component.  
Plug-in |  com.mind8.mechatronic.skill.api.PlaceholderNotExistingException com.mind8.expressionparser.EvaluationException  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.reorderPlaceholderObjects2) changes the order of the project components of the type Axis on the placeholder Axes of the project component Move. In order for the tutorial project Feeder_Extended1 to contain project components on the placeholder Axes, several instances of T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Axis have to be instantiated manually on the placeholder beforehand. The getPlaceholderObjects method determines the order of the project components on the Axes placeholder before and after the change of the order (see rows 22 and 39). The reorderPlaceholderObjects method moves the project component with the list index 0 to the position with the list index 1 on the Axes placeholder (see row 23). Information and possible errors are output to the UserMessageCollector (see rows 7, 20, 29, 33, 39, 42 and 45).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.api.PlaceholderNotExistingException;
    import com.mind8.expressionparser.EvaluationException;
    
    String scriptName = "reorderPlaceholderObjects2";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    logText1 = "Script error: Cannot sort objects of the given placeholder due to a formula error: ";
    
    try{
    	// Determine placeholders for selected object
    	placeholder = obj.getPlaceholders().get(0);
    	String placeholderName  = placeholder.name();
    	info = "Placeholder name: " + placeholderName;
    	UserMessageCollector.addInfo(PROJECT, self, null, "Scripting", info);
    	
    	listBefore = obj.getPlaceholderObjects(placeholderName);
    	obj.reorderPlaceholderObjects(placeholderName,0,1,1);
    	
    	// save the change
    	uow.saveChanges();
    }
    catch (EvaluationException ex){
    	UserMessageCollector.addError(LIBRARY, self, null, "Scripting", logText1 + ex);
    	return;
    }
    catch (IndexOutOfBoundsException ioobe){
    	UserMessageCollector.addError(LIBRARY, self, null, "Scripting", ioobe);
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

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder.Move of the tutorial, the instance <<Axis>> is moved from position 1 to position 2 and outputs the following messages:
    
        ### Start of script 'reorderPlaceholderObjects2' ###
    Placeholder name: Axes
    listBefore: [<<Axis>>, <<Axis2>>, <<Axis3>>, <<Axis4>>]
    listAfter: [<<Axis2>>, <<Axis>>, <<Axis3>>, <<Axis4>>]
    ### End of script 'reorderPlaceholderObjects2' ###
