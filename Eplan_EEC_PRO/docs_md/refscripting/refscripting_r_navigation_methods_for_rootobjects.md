---
title: "Navigation methods for root objects"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_navigation_methods_for_rootobjects.htm"
file: "refscripting_r_navigation_methods_for_rootobjects"
category: "refscripting"
---

# Navigation methods for root objects

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Navigation methods for root objects The following methods of mechatronic components are available in the scripts also for mechatronic root objects (not discipline root objects):
     * mos
     * rmos
     * existsRelRef
These methods are available for mechatronic and discipline root objects:
     * relRef
[Example code for mos()](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.getMosOfSelectedMechatronicRootObject) lists all project components directly under the selected root component. The selected root component is transferred as the obj argument when the script is started. The listOfMos = obj.getMos() method determines all subordinate mechatronic components under the root component (see row 15). Information and possible errors are output to the message log and to the console (see rows 8, 17, 20 and 24).
    
        import org.foederal.eobroker.core.IUnitOfWork;
    import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.expressionparser.EvaluationException;
    import org.foederal.eobroker.core.IEngineeringObject;
    
    String scriptName = "getMosOfSelectedMechatronicRootObject";
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

Result: Applied to the root component Mechatronic of the tutorial, the SelectionAction supplies a list of all directly subordinate mechatronic components.
    
        ### Start of script 'getMosOfSelectedMechatronicRootObject' ###
    listOfMos: [<<Feeder>>]
    ### End of script 'getMosOfSelectedMechatronicRootObject' ###

[Example code for rmos()](javascript:void\(0\);) Attributes for a SelectionAction:
     * SelectionType = MechatronicRoot
Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example ( ScriptingExamples.getRmosOfSelectedMechatronicRootObject) lists all project components under the selected root component. The selected root component is transferred as the obj argument when the script is started. The listOfRmos = obj.getRmos() method determines all subordinate mechatronic components under the root component (see row 15). Information and possible errors are output to the message log and to the console (see rows 8, 17, 20 and 24).
    
        import org.foederal.eobroker.core.IUnitOfWork;
    import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.expressionparser.EvaluationException;
    import org.foederal.eobroker.core.IEngineeringObject;
    
    String scriptName = "getRmosOfSelectedMechatronicRootObject";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    try{
    	// get child objects of selected root object
    	listOfMos = obj.getRmos();
    	info = "listOfRmos: " + listOfRmos;
    	UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    }
    catch (EvaluationException ex){
    	UserMessageCollector.addError(PROJECT,'self',null,"Scripting",ex);
    }
    finally{
    	info = "### End of script '" + scriptName + "' ###";
    	UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    }

Result: Applied to the root object Feeder.Mechatronic of the tutorial, the SelectionAction supplies a list of all subordinate components.
    
        ### Start of script 'getRmosOfSelectedMechatronicRootObject' ### <Info>
    listOfRmos: [<<Feeder>>, <<Insert>>, <<Stack>>, <<Positionsensor_optical>>, <<Separator>>, <<Cylinder>>, <<Valve_1>>, <<Valve>>, <<Position_1>>, <<Position_2>>, <<Inspect>>, <<Orientationinspector>>, <<Positionsensor_optical>>, <<Move>>, <<X_Axis>>, <<Cylinder>>, <<Valve_1>>, <<Valve>>, <<Position_1>>, <<Position_2>>, <<Position_3>>, <<Position_4>>, <<Y_Axis>>, <<Cylinder>>, <<Valve_1>>, <<Valve>>, <<Position_1>>, <<Gripper>>, <<Valve>>, <<Pressuresensor>>, <<Axis>>, <<Cylinder>>, <<Valve_1>>, <<Valve>>, <<Position_1>>, <<Position_2>>, <<Position_3>>, <<Position_4>>, <<Axis2>>, <<Cylinder>>, <<Valve_1>>, <<Valve>>, <<Position_1>>, <<Position_2>>, <<Position_3>>, <<Position_4>>, <<Axis5>>, <<Cylinder>>, <<Valve_1>>, <<Valve>>, <<Position_1>>, <<Position_2>>, <<Position_3>>, <<Position_4>>, <<Store>>, <<Discard>>, <<Move2>>, <<X_Axis>>, <<Cylinder>>, <<Valve_1>>, <<Valve>>, <<Position_1>>, <<Position_2>>, <<Position_3>>, <<Position_4>>, <<Y_Axis>>, <<Cylinder>>, <<Valve_1>>, <<Valve>>, <<Position_1>>, <<Gripper>>, <<Valve>>, <<Pressuresensor>>, <<Move3>>, <<X_Axis>>, <<Cylinder>>, <<Valve_1>>, <<Valve>>, <<Position_1>>, <<Position_2>>, <<Position_3>>, <<Position_4>>, <<Y_Axis>>, <<Cylinder>>, <<Valve_1>>, <<Valve>>, <<Position_1>>, <<Gripper>>, <<Valve>>, <<Pressuresensor>>] <Info>
    ### End of script 'getRmosOfSelectedMechatronicRootObject' ### <Info>

[Example code for existsRelRef()](javascript:void\(0\);) Attributes for a SelectionAction:
     * SelectionType = DisciplineRoot
Code:
    
        import org.foederal.apache.log4j.SpaceLogger;
    SpaceLogger logger = SpaceLogger.getSpaceLogger("My logger");
    									
    existsRelRef = obj.existsRelRef('Schematic_Feeder_M_Schematic.Page_Feeder_M_SchematicPage2');
    									
    methodName = "Method name: existsRelRef()";
    logger.info(methodName);
    logger.info(existsRelRef)

Result: Applied to the root object ECAD of the tutorial, the SelectionAction supplies true or false depending on whether the specified discipline component exists.
    
        Method name: existsRelRef() <My logger>
    true <My logger>

[Example code for relRef()](javascript:void\(0\);) Attributes for a SelectionAction:
     * SelectionType = DisciplineRoot
Code:
    
        import org.foederal.apache.log4j.SpaceLogger;
    SpaceLogger logger = SpaceLogger.getSpaceLogger("My logger");
    									
    relRef = obj.relRef('Schematic_Feeder_M_Schematic.Page_Feeder_M_SchematicPage2');
    									
    methodName = "Method name: relRef()";
    logger.info(methodName);
    logger.info(relRef)

Result: Applied to the root object ECAD of the tutorial, the SelectionAction supplies the specified discipline component.
    
        Method name: relRef() <My logger>
    <<Page_Feeder_M_SchematicPage2>> <My logger>
