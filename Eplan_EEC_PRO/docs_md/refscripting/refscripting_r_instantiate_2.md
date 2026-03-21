---
title: "instantiate(instantiationTarget, MechatronicObjectClass classToInstantiate, String instanceName, boolean instantiateExtensions, String placeholderName)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_instantiate_2.htm"
file: "refscripting_r_instantiate_2"
category: "refscripting"
---

# instantiate(instantiationTarget, MechatronicObjectClass classToInstantiate, String instanceName, boolean instantiateExtensions, String placeholderName)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  instantiate(instantiationTarget, MechatronicObjectClass classToInstantiate, String instanceName, boolean instantiateExtensions, String placeholderName) Instantiates a component that corresponds to the type classToInstantiate with the given instanceName on the placeholder identified by placeholderName at the specified instantiationTarget. The Boolean argument instantiateExtensions specifies whether objects are instantiated on contained extension points. The instantiation takes place on the first from the rear fitting placeholder or extension point. If the delivered placeholder name is null and no fitting one can be determined, a NoMatchingPlaceholderException is thrown. If the classToInstantiate does not fit on the given placeholder, a PlaceholderNotMatchingException is thrown. If there is no placeholder with the given name, a PlaceholderNotExistingException is thrown. instantiate(instantiationTarget, MechatronicObjectClass classToInstantiate, String instanceName, boolean instantiateExtensions, String placeholderName) throws PlaceholderNotMatchingException, PlaceholderNotExistingException, NoMatchingPlaceholderException  
---  
Argument | ITopInstantiationTarget | instantiationTarget | A mechatronic component or mechatronic root, under which the new object is placed  
MechatronicObjectClass | classToInstantiate | The class to be instantiated must be specified as an absolute name.  
String | instanceName | The name of the object. If null is returned, the object gets the name of the class.  
Boolean | instantiateExtensions | If the return value is true, internal extension points are calculated during instantiation, if the return value is false no calculation is done.  
String | placeholderName | Defines the placeholder where the instantiated object is placed.  
Return value | Component | The instantiated object  
Exception error | PlaceholderNotMatchingException |  | No placeholder is specified and a suitable one could not be found.  
PlaceholderNotExistingException |  | The specified placeholder does not exist at the specified project component.  
NoMatchingPlaceholderException |  | The specified placeholder does not match the specified instance type.  
Plug-in |  com.mind8.mechatronic.skill.api.NoMatchingPlaceholderException com.mind8.mechatronic.skill.api.PlaceholderNotExistingException com.mind8.mechatronic.skill.api.PlaceholderNotMatchingException  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.instantiate2) generates an instance of the Move library component. The instance is installed below the station Feeder on the placeholder Moves. The method TypeClass.findType() determines the library component (see rows 23 and 33). The AbsoluteNameUtil.getObjectByAbsolutePath() method finds the appropriate placeholder (see row 28). The instantiation is created using the method IMechatronicInstantiationAPI.DEFAULT.instantiate() (see row 52). The uow.saveChanges() method is used to make the change effective in the Unit-Of-Work in the project (see row 57). The output of information and possible errors is carried out in the message log (see rows 12, 20, 25, 30, 35, 43, 48, 54, 60, 64, 68 and 73).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.AbsoluteNameUtil;
    import com.mind8.mechatronic.skill.api.IMechatronicInstantiationAPI;
    import com.mind8.mechatronic.skill.eos.TypeClass;
    import com.mind8.mechatronic.skill.ResourceUtil;
    import com.mind8.mechatronic.skill.api.NoMatchingPlaceholderException
    import com.mind8.mechatronic.skill.api.PlaceholderNotExistingException
    import com.mind8.mechatronic.skill.api.PlaceholderNotMatchingException
    
    String scriptName = "instantiate2";
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
    
    // an instance name set to 'null' forces the instantiation API to create a unique name
    String instanceName;
    
    // compute inner extension points
    Boolean instantiateExtensions = false;
    info = "instantiateExtensions: " + instantiateExtensions;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    // Name of placeholder or extension point
    String placeholderName = "Mover";
    info = "placeholderName: " + placeholderName;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    try{
    	// instantiate component
    	instance = IMechatronicInstantiationAPI.DEFAULT.instantiate(instantiationTarget, classToInstantiate, instanceName, instantiateExtensions, placeholderName);
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
    	info = "### End of script '" + scriptName + "' ###";
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    }

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder.Move of the tutorial, the SelectionAction installs an instance of Move on the placeholder Moves.
    
        ### Start of script 'instantiate2' ###
    absName: T_Mechatronic_ModularSystem.Stations.Feeder
    absLibComp: T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Move
    instantiationTarget: <<Feeder>>
    classToInstantiate: <<Move>>
    instantiateExtensions: false
    placeholderName: Mover
    instance: <<Move2>>
    ### End of script 'instantiate2' ###
