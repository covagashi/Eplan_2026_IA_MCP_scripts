---
title: "instantiate(instantiationTarget, MechatronicObjectClass classToInstantiate, String instanceName, boolean instantiateExtensions, String placeholderName, IMechatronicInstantiationContext context)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_instantiate_5.htm"
file: "refscripting_r_instantiate_5"
category: "refscripting"
---

# instantiate(instantiationTarget, MechatronicObjectClass classToInstantiate, String instanceName, boolean instantiateExtensions, String placeholderName, IMechatronicInstantiationContext context)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  instantiate(instantiationTarget, MechatronicObjectClass classToInstantiate, String instanceName, boolean instantiateExtensions, String placeholderName, IMechatronicInstantiationContext context) Instantiates a component that corresponds to the type classToInstantiate with the given instanceName on the placeholder identified by placeholderName at the specified instantiationTarget. A reusable context is applied to accelerate multiple instantiations in the same script. The Boolean argument instantiateExtensions specifies whether objects are instantiated on contained extension points. The instantiation takes place on the first from the rear fitting placeholder or extension point. It is important to strictly follow the application of pattern in the example, otherwise may not be saved. instantiate(instantiationTarget, MechatronicObjectClass classToInstantiate, String instanceName, boolean instantiateExtensions, String placeholderName, IMechatronicInstantiationContext context) throws PlaceholderNotMatchingException, PlaceholderNotExistingException, NoMatchingPlaceholderException  
---  
Argument | ITopInstantiationTarget | instantiationTarget | A mechatronic component or mechatronic root, under which the new object is placed  
MechatronicObjectClass | classToInstantiate | The class to instantiate  
String | instanceName | The name of the object. If null is returned, the object gets the name of the class.  
Boolean | instantiateExtensions | If the return value is true, internal extension points are calculated during instantiation, if the return value is false no calculation is done.  
String | placeholderName | Defines the placeholder where the instantiated object is placed.  
IMechatronicInstantiationContext | context | A reusable context for instantiation.  
Return value | Component | The instantiated object  
Exception error | PlaceholderNotMatchingException |  | No placeholder is specified and a suitable one could not be found.  
PlaceholderNotExistingException |  | The specified placeholder does not exist at the specified project component.  
NoMatchingPlaceholderException |  | The specified placeholder does not match the specified instance type.  
Plug-in |  com.mind8.mechatronic.skill.api.NoMatchingPlaceholderException com.mind8.mechatronic.skill.api.PlaceholderNotExistingException com.mind8.mechatronic.skill.api.PlaceholderNotMatchingException com.mind8.mechatronic.skill.AbsoluteNameUtil com.mind8.mechatronic.skill.api.IMechatronicInstantiationAPI com.mind8.mechatronic.skill.eos.TypeClass java.util.ArrayList |  |   
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.instantiate5) generates two instances of the Move library component. The instances are installed below the station Feeder on the placeholder Moves. The method TypeClass.findType() determines the library component (see rows 19 and 29). The AbsoluteNameUtil.getObjectByAbsolutePath() method finds the appropriate placeholder (see row 24). The instantiation is created with the method IMechatronicInstantiationAPI.DEFAULT.instantiate() and uses the context of the first instantiation for the second instantiation (see rows 54 and 59). The uow.saveChanges() method is used to make the change effective in the Unit-Of-Work in the project (see row 65). The output of information and possible errors is carried out in the message log (see rows 13, 21, 26, 31, 41, 46, 50, 57, 62, 68, 72, 76 and 82).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.AbsoluteNameUtil;
    import com.mind8.mechatronic.skill.api.IMechatronicInstantiationAPI;
    import com.mind8.mechatronic.skill.eos.TypeClass;
    import com.mind8.mechatronic.skill.ResourceUtil;
    import java.util.ArrayList;
    import com.mind8.mechatronic.skill.api.NoMatchingPlaceholderException
    import com.mind8.mechatronic.skill.api.PlaceholderNotExistingException
    import com.mind8.mechatronic.skill.api.PlaceholderNotMatchingException
    
    String scriptName = "instantiate5";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    // Component to instantiate
    String absLibComp = "T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Move"; 
    info = "absLibComp: " + absLibComp;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // Component containing a placeholder or extension point
    instantiationTarget = AbsoluteNameUtil.getObjectByAbsolutePath("Feeder_Extended1.Mechatronic.Feeder",uow); // Argument in command
    info = "instantiationTarget: " + instantiationTarget;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // Library component to instantiate
    classToInstantiate = TypeClass.findType(uow, absLibComp);
    info = "classToInstantiate: " + classToInstantiate;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // an instance name set to 'null' forces the instantiation API to create a unique name
    String instanceName;
    
    aList = new ArrayList();
    
    // compute inner extension points
    Boolean instantiateExtensions = false;
    info = "instantiateExtensions: " + instantiateExtensions;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // Name of placeholder or extension point
    String placeholderName = "Mover";
    info = "placeholderName: " + placeholderName;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    context = IMechatronicInstantiationAPI.DEFAULT.createInstantiationContext(instantiationTarget);
    info = "context: " + context;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    try{
    	// instantiate component	
    	instance = IMechatronicInstantiationAPI.DEFAULT.instantiate(instantiationTarget, classToInstantiate, instanceName, instantiateExtensions, placeholderName, context);
    	aList.add(instance);
    	info = "instance: " + instance;
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    	instance = IMechatronicInstantiationAPI.DEFAULT.instantiate(instantiationTarget, classToInstantiate, instanceName, instantiateExtensions, placeholderName, context);
    	aList.add(instance);
    	info = "instance: " + instance;
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    	// save the change
    	uow.saveChanges();
    }
    catch (NoMatchingPlaceholderException nmpe){
    	UserMessageCollector.addError(LIBRARY,'self',null,"Scripting",nmpe);
    	return;
    }
    catch (PlaceholderNotExistingException pne){
    	UserMessageCollector.addError(LIBRARY, self, null, "Scripting", pne);
    	return;
    }
    catch (PlaceholderNotMatchingException pnme){
    	UserMessageCollector.addError(LIBRARY, self, null, "Scripting", pnme);
    	return;
    }
    finally{
    	context.deleteUnusedInstances();
    	info = "### End of script '" + scriptName + "' ###";
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    }
    return aList;

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder.Move of the tutorial, the SelectionAction installs two instances of Move on the placeholder Moves.
    
        ### Start of script 'instantiate5' ###
    absLibComp: T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Move
    instantiationTarget: <<Feeder>>
    classToInstantiate: <<Move>>
    instantiateExtensions: false
    placeholderName: Mover
    context: com.mind8.mechatronic.skill.api.impl.DefaultMechatronicInstantiationContext@31778f7a
    instance: <<Move2>>
    instance: <<Move3>>
    ### End of script 'instantiate5' ###
