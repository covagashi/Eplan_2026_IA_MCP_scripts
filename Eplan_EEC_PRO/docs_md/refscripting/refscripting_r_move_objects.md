---
title: "MoveHelper.move(IUnitOfWork uow, String sourceAbsoluteName, String targetPlaceholderAbsoluteName)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_move_objects.htm"
file: "refscripting_r_move_objects"
category: "refscripting"
---

# MoveHelper.move(IUnitOfWork uow, String sourceAbsoluteName, String targetPlaceholderAbsoluteName)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  MoveHelper.move(IUnitOfWork uow, String sourceAbsoluteName, String targetPlaceholderAbsoluteName) The MoveHelper.move method moves an instance from a source placeholder to a target placeholder. MoveHelper.move(IUnitOfWork uow, String sourceAbsoluteName, String targetPlaceholderAbsoluteName)  
---  
Argument | IUnitOfWork uow | The UnitOfWork of the script  
String sourceAbsoluteName | Absolute name of the source object  
String targetPlaceholderAbsoluteName | Absolute name of the placeholder on which the source object is inserted.  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
     * Two new instances of Move exist.
     * The placeholder Move2.Axis contains an instance of Axis named Axis2.
The following script example (ScriptingExamples.moveObject) moves the project component Move2.Axis2 to the placeholder Move3.Axis. Both the source and the target are specified directly (see rows 14 and 18). The name of the target component is specified (see row 22). If a project component with the specified name already exists, either a number is appended to the end of the name or an existing number is incremented. The copy is created using the Copyhelper.copy() method (see row 26).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.moving.helper.MoveHelper;
    import org.foederal.eobroker.core.IUnitOfWork;
    
    String scriptName = "moveObject";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    // Absolute name of object to copy
    source = "Feeder_Extended1.Mechatronic.Feeder.Move2.Axis2";
    info = "source: " + source;
    UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    
    // Absolute name of target component
    target = "Feeder_Extended1.Mechatronic.Feeder.Move3.Axes";
    info = "target: " + target;
    UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    
    // Move object
    MoveHelper.move(uow, source, target);
    
    // save the change
    uow.saveChanges();
    
    info = "### End of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder.Move2.Axis2 of the tutorial, the SelectionAction moves the project component Axis2 to the placeholder Feeder_Extended1.Mechatronic.Feeder.Move3.Axes.
    
        ### Start of script 'moveObject' ###
    source: Feeder_Extended1.Mechatronic.Feeder.Move2.Axis2
    target: Feeder_Extended1.Mechatronic.Feeder.Move3.Axes
    ### End of script 'moveObject' ###
