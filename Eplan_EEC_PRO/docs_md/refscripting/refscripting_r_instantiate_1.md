---
title: "instantiate(ITopInstantiationTarget instantiationTarget, MechatronicObjectClass classToInstantiate, String instanceName, boolean instantiateExtensions)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_instantiate_1.htm"
file: "refscripting_r_instantiate_1"
category: "refscripting"
---

# instantiate(ITopInstantiationTarget instantiationTarget, MechatronicObjectClass classToInstantiate, String instanceName, boolean instantiateExtensions)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  instantiate(ITopInstantiationTarget instantiationTarget, MechatronicObjectClass classToInstantiate, String instanceName, boolean instantiateExtensions) Instantiates a component that corresponds to the type classToInstantiate with the given instanceName at the specified instantiationTarget. The Boolean argument instantiateExtensions specifies whether objects are instantiated on contained extension points. The instantiation takes place on the first from the rear fitting placeholder or extension point. If there is no suitable placeholder or extension point, a NoMatchingPlaceholderException is thrown. instantiate(instantiationTarget, MechatronicObjectClass classToInstantiate, String instanceName, boolean instantiateExtensions) throws PlaceholderNotMatchingException, PlaceholderNotExistingException, NoMatchingPlaceholderException  
---  
Argument | ITopInstantiationTarget | instantiationTarget | A mechatronic component or the root object of mechatronics (MechatronicRoot) under which the new object is created  
MechatronicObjectClass | classToInstantiate | The class to instantiate  
String | instanceName | The name of the object. If null is returned, the object gets the name of the class.  
Boolean | instantiateExtensions | If the return value is true, internal extension points are calculated during instantiation, if the return value is false no calculation is done.  
Return value | Component | The instantiated object.  
Exception error | NoMatchingPlaceholderException |  | The specified placeholder does not match the specified instance type.  
PlaceholderNotExistingException |  | The specified placeholder does not exist at the specified project component.  
PlaceholderNotMatchingException |  |  No placeholder is specified and a suitable one could not be found.  
Plug-in |  com.mind8.mechatronic.skill.api.NoMatchingPlaceholderException com.mind8.mechatronic.skill.api.PlaceholderNotExistingException com.mind8.mechatronic.skill.api.PlaceholderNotMatchingException  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.instantiate1) generates an instance of the Move library component. The instance is installed below the station Feeder on the placeholder Moves. The method TypeClass.findType() determines the library component (see rows 23 and 33). The AbsoluteNameUtil.getObjectByAbsolutePath() method finds the appropriate placeholder (see row 28). The instantiation is created using the method IMechatronicInstantiationAPI.DEFAULT.instantiate() (see row 45). The uow.saveChanges() method is used to make the change effective in the Unit-Of-Work in the project (see row 50). The output of information and possible errors is carried out in the message log (see rows 12, 20, 25, 30, 35, 47, 54, 57, 61 and 66).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.AbsoluteNameUtil;
    import com.mind8.mechatronic.skill.eos.TypeClass;
    import com.mind8.mechatronic.skill.ResourceUtil;
    import com.mind8.mechatronic.skill.api.IMechatronicInstantiationAPI;
    import com.mind8.mechatronic.skill.api.NoMatchingPlaceholderException
    import com.mind8.mechatronic.skill.api.PlaceholderNotExistingException
    import com.mind8.mechatronic.skill.api.PlaceholderNotMatchingException
    
    String scriptName = "instantiate1";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    // Component containing the placeholder
    String absName = "T_Mechatronic_ModularSystem.Stations.Feeder";
    info = "absName: " + absName;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // Component to instantiate
    String absLibComp = "T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Move"; 
    info = "absLibComp: " + absLibComp;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // Component containing a placeholder or extension point
    instantiationTarget = AbsoluteNameUtil.getObjectByAbsolutePath("Feeder_Extended1.Mechatronic.Feeder",uow);
    info = "instantiationTarget: " + instantiationTarget;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // Library component to instantiate
    classToInstantiate = TypeClass.findType(uow, absLibComp);
    info = "classToInstantiate: " + classToInstantiate;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    //an instance name set to 'null' forces the instantiation API to create a unique name
    String instanceName;
    
    // compute inner extension points
    Boolean instantiateExtensions = false;
    
    try{
    	// instantiate component
    	instance = IMechatronicInstantiationAPI.DEFAULT.instantiate(instantiationTarget, classToInstantiate, instanceName, instantiateExtensions);
    	info = "instance: " + instance;
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    	
    	// save the change
    	uow.saveChanges();
    }
    catch (NoMatchingPlaceholderException nmpe){
    	// error handling
    	UserMessageCollector.addError(LIBRARY,'self',null,"Scripting", nmpe);
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
    	info = "### End of script '" + scriptName + "' ###";
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    }

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder.Move of the tutorial, the SelectionAction installs an instance of Move on the placeholder Moves.
    
        ### Start of script 'instantiate1' ###
    absName: T_Mechatronic_ModularSystem.Stations.Feeder
    absLibComp: T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Move
    instantiationTarget: <<Feeder>>
    classToInstantiate: <<Move>>
    instance: <<Move2>>
    ### End of script 'instantiate1' ###
