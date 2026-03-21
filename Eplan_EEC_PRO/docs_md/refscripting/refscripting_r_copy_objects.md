---
title: "CopyHelper.copy(IUnitOfWork, String sourceName, String targetName, String newName)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_copy_objects.htm"
file: "refscripting_r_copy_objects"
category: "refscripting"
---

# CopyHelper.copy(IUnitOfWork, String sourceName, String targetName, String newName)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  CopyHelper.copy(IUnitOfWork, String sourceName, String targetName, String newName) Creates the copy of an instance and inserts it at the specified position of a project. If the name is identical, a number is attached to the name of the copy. CopyHelper.copy(IUnitOfWork, String sourceName, String targetName, String newName)  
---  
Argument | IUnitOfWork uow | The UnitOfWork of the script  
String sourceName | Absolute name of the source object  
String targetName | Absolute name of the superordinate target component, i.e., of the object to which the copy is mounted. This may be a project, a mechatronic component or a placeholder.  
String newName | The name to be assigned to the copy at the target location. If the name is already taken, a number is added at the end and incremented until a free name has been found.  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.copyObject) generates a copy of the Move project component. The copy is installed underneath the station Feeder_Extended1.Mechatronic.Feeder on the placeholder Mover. Both the source and the target are specified directly (see rows 13 and 18). The name of the target component is specified (see row 23). If a project component with the specified name already exists, either a number is appended to the end of the name or an existing number is incremented. The copy is created using the Copyhelper.copy() method (see row 28). The uow.saveChanges() method (see row 31) is used to make the change effective in the Unit-Of-Work in the project. Information and possible errors are output in the message log (see rows 7, 15, 20, 25 and 34).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.copying.helper.CopyHelper;
    import org.foederal.eobroker.core.IUnitOfWork;
    
    String scriptName = "copyObject";
    String info = "### Start of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);
    
    // determine the UnitOfWork
    uow = self.getUnitOfWork();
    
    // Absolute name of object to copy
    source = "Feeder_Extended1.Mechatronic.Feeder.Move";
    info = "source: " + source;
    UserMessageCollector.addInfo(PROJECT,'self',null,'Scripting',info);
    
    // Absolute name of target component
    target = "Feeder_Extended1.Mechatronic.Feeder";
    info = "target: " + target;
    UserMessageCollector.addInfo(PROJECT,'self',null,'Scripting',info);
    
    // New name of the target instance
    newName = "Move";
    info = "newName: " + newName;
    UserMessageCollector.addInfo(PROJECT,'self',null,'Scripting',info);
    
    // Create copy
    CopyHelper.copy(uow, source, target, newName);
    
    // save the change
    uow.saveChanges();
    
    info = "### End of script '" + scriptName + "' ###";
    UserMessageCollector.addInfo(PROJECT,'self',null,"Scripting",info);

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder.Move of the tutorial, the SelectionAction builds a copy of Move on the placeholder Mover.
    
        ### Start of script 'copyObject' ###
    source: Feeder_Extended1.Mechatronic.Feeder.Move
    target: Feeder_Extended1.Mechatronic.Feeder
    newName: Move
    ### End of script 'copyObject' ###
