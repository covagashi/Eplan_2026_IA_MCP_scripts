---
title: "Navigating the object model"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_navigating_the_object_model.htm"
file: "refscripting_r_navigating_the_object_model"
category: "refscripting"
---

# Navigating the object model

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Navigating the object model The methods for navigating the object model can be derived from the methods of the formula language. To this purpose you have to start with get and the first character has to be upper.case, for example getMos() (see also [Project component navigation methods](refformulas_r_project_components_navigation.htm)). [Example code for mos()](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.getMosOfSelectedMechatronicObject) lists all the project components directly under the selected project component. The selected project component is passed as an obj argument when the script is started. The method listOfMos = obj.getMos() determines all subordinate mechatronic components under the selected project component (see row 15). Information and possible errors are output to the message log and to the console (see rows 8, 17, 20 and 24).
    
        import org.foederal.eobroker.core.IUnitOfWork;
    import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.expressionparser.EvaluationException;
    import org.foederal.eobroker.core.IEngineeringObject;
    
    String scriptName = "getMosOfSelectedMechatronicObject";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    try{
    	// get child objects of selected root object
    	listOfMos = obj.getMos();
    	info = "listOfMos: " + listOfMos;
    	UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    }
    catch (EvaluationException ex){
    	UserMessageCollector.addError(PROJECT,'self',null,"Scripting",ex);
    }
    finally{
    	info = "### End of script '" + scriptName + "' ###";
    	UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    }

Result: Applied to the project component Feeder.Mechatronic.Feeder.Move of the tutorial, the SelectionAction supplies a list of all directly subordinate mechatronic components.
    
        ### Start of script 'getMosOfSelectedMechatronicObject' ###
    listOfMos: [<<X_Axis>>,<<Y_Axis>>,<<Gripper>>]
    ### End of script 'getMosOfSelectedMechatronicRootObject' ###
