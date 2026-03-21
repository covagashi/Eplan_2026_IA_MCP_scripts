---
title: "delete(IEngineeringObject eo)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_delete_iengineeringobject_eo.htm"
file: "refscripting_r_delete_iengineeringobject_eo"
category: "refscripting"
---

# delete(IEngineeringObject eo)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  delete(IEngineeringObject eo) Deletes an EO in the Unit-Of-Work. The EO is removed from the project after executing the saveChanges method. Note Mechatronic objects have the method isPlaceholderPlaced. This returns true if the object is installed on a placeholder instead of directly in another object. Only objects that return the value true for isPlaceholderPlaced can be deleted from the mechatronic project structure. delete(IEngineeringObject eo)  
---  
Argument | IEngineeringObject | eo | A project component that is installed into a placeholder or insertion point.  
Return value | void |  |   
Exception error | EvaluationException | The specified formula is invalid.  
PlaceholderNotExistingException | The specified placeholder does not exist at the specified project component.  
Plug-in |  org.foederal.eobroker.core.IUnitOfWork com.mind8.expressionparser.EvaluationException com.mind8.mechatronic.skill.api.PlaceholderNotExistingException  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
     * At least one component is installed on a placeholder, for example a component Axis on the placeholder Feeder.Move.Axes .
The following script example (ScriptingExamples.deleteSelectedObject) removes a selected instance from a placeholder. The selected instance is transferred as the obj argument when the script is started. The method sequence obj.getMc().getPlaceholders().getAt(0).getName() determines the name of the placeholder in which the instance is installed (see row 16). If the condition if(moToDelete.isPlaceholderPlaced()) is met, the uow.delete(moToDelete) method deletes the selected instance (see row 27). The uow.saveChanges() method is used to make the change effective in the Unit-Of-Work in the project (see row 32). The output of information and possible errors is carried out in the message log (see rows 9, 18, 23, 29, 33, 37, 40 and 44).
    
        import org.foederal.eobroker.core.IUnitOfWork;
    import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.api.PlaceholderNotExistingException;
    import com.mind8.expressionparser.EvaluationException;
    import org.foederal.eobroker.core.IEngineeringObject;
    
    String scriptName = "deleteSelectedObject";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    try{
    	// get placeholder
    	String placeholderName = obj.getMc().getPlaceholders().getAt(0).getName();
    	info = "placeholderName: " + placeholderName;
    	UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    
    	// object to delete							
    	moToDelete = obj;
    	info = "moToDelete: " + moToDelete;
    	UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    
    	// Delete object if placed on placeholder
    	if(moToDelete.isPlaceholderPlaced()){
    		uow.delete(moToDelete);
    		info = "Object is deleted.";
    		UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    
    		// save the change
    		uow.saveChanges();
    		UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting","UOW saved");
    	}
    }
    catch (EvaluationException ex){
    	UserMessageCollector.addError(PROJECT,'self',null,"Scripting",ex);
    }
    catch (PlaceholderNotExistingException ex){
    	UserMessageCollector.addError(PROJECT,'self',null,"Scripting",ex);
    }
    finally{
    	info = "### End of script '" + scriptName + "' ###";
    	UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    }

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder.Move.Axis2 of the tutorial removes this instance and outputs the following messages:
    
        ### Start of script 'deleteSelectedObject' ###
    placeholderName: Axes
    moToDelete: <<Axis2>>
    Object is deleted.
    UOW saved
    ### End of script 'deleteSelectedObject' ###
