---
title: "instantiate(instantiationTarget, MechatronicObjectClass classToInstantiate, String instanceName, boolean instantiateExtensions, Placeholder placeholder)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_instantiate_3.htm"
file: "refscripting_r_instantiate_3"
category: "refscripting"
---

# instantiate(instantiationTarget, MechatronicObjectClass classToInstantiate, String instanceName, boolean instantiateExtensions, Placeholder placeholder)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  instantiate(instantiationTarget, MechatronicObjectClass classToInstantiate, String instanceName, boolean instantiateExtensions, Placeholder placeholder) Instantiates a component that corresponds to the type classToInstantiate with the given instanceName on the placeholder identified by placeholder at the specified instantiationTarget. The Boolean argument instantiateExtensions specifies whether objects are instantiated on contained extension points. If the delivered placeholder is null and no fitting one can be determined, a NoMatchingPlaceholderException is thrown. If the classToInstantiate does not fit on the given placeholder, a PlaceholderNotMatchingException is thrown. instantiate(instantiationTarget, MechatronicObjectClass classToInstantiate, String instanceName, boolean instantiateExtensions, Placeholder placeholder) throws PlaceholderNotMatchingException, PlaceholderNotExistingException, NoMatchingPlaceholderException  
---  
Argument | ITopInstantiationTarget | instantiationTarget | A mechatronic component or mechatronic root, under which the new object is placed  
MechatronicObjectClass | classToInstantiate | The class to instantiate  
String | instanceName | The name of the object. If null is returned, the object gets the name of the class.  
Boolean | instantiateExtensions | If the return value is true, internal extension points are calculated during instantiation, if the return value is false no calculation is done.  
Placeholder | placeholder | Defines the placeholder where the instantiated object is placed.  
Return value | Component | The instantiated object  
Exception error |  PlaceholderNotMatchingException |  |  No placeholder is specified and a suitable one could not be found.  
PlaceholderNotExistingException |  | The specified placeholder does not exist at the specified project component.  
NoMatchingPlaceholderException |  | The specified placeholder does not match the specified instance type.  
Plug-in |  com.mind8.mechatronic.skill.api.NoMatchingPlaceholderException com.mind8.mechatronic.skill.api.PlaceholderNotExistingException com.mind8.mechatronic.skill.api.PlaceholderNotMatchingException com.mind8.mechatronic.skill.AbsoluteNameUtil com.mind8.mechatronic.skill.api.IMechatronicInstantiationAPI com.mind8.mechatronic.skill.eos.TypeClass com.mind8.mechatronic.skill.ResourceUtil  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.instantiate3) generates an instance of the Move library component. The instance is installed below the station Feeder on the placeholder Mover. The library component is determined with the method TypeClass.findType() (see rows 23 and 33). The method AbsoluteNameUtil.getObjectByAbsolutePath() finds the component with a placeholder (see row 28). The getPlaceholders() navigation method determines all placeholders of the component feeder (row 43). In this example the instance is to be installed on the last placeholder of the list. The last() method determines it from the list. The instantiation is created using the method IMechatronicInstantiationAPI.DEFAULT.instantiate() (see row 50). The uow.saveChanges() method is used to make the change effective in the Unit-Of-Work in the project (see row 55). The output of information and possible errors is carried out in the message log (see rows 12, 20, 25, 30, 35, 46, 52, 58, 62, 66 and 71).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.AbsoluteNameUtil;
    import com.mind8.mechatronic.skill.api.IMechatronicInstantiationAPI;
    import com.mind8.mechatronic.skill.eos.TypeClass;
    import com.mind8.mechatronic.skill.ResourceUtil;
    import com.mind8.mechatronic.skill.api.NoMatchingPlaceholderException
    import com.mind8.mechatronic.skill.api.PlaceholderNotExistingException
    import com.mind8.mechatronic.skill.api.PlaceholderNotMatchingException
    
    String scriptName = "instantiate3";
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
    
    // placeholder or extension point
    placeholder = instantiationTarget.getPlaceholders().last();
    info = "placeholder: " + placeholder;
    UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    
    try{
    	// instantiate component
    	instance = IMechatronicInstantiationAPI.DEFAULT.instantiate(instantiationTarget, classToInstantiate, instanceName, instantiateExtensions, placeholder);
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
    
        ### Start of script 'instantiate3' ###
    absName: T_Mechatronic_ModularSystem.Stations.Feeder
    absLibComp: T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Move
    instantiationTarget: <<Feeder>>
    classToInstantiate: <<Move>>
    placeholderName: Mover
    instance: <<Move2>>
    ### End of script 'instantiate3' ###
