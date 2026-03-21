---
title: "Creating the actions for the import of the discipline library into the modular system"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_expert_create_action_for_import_of_discipline.htm"
file: "tutp8_h_expert_create_action_for_import_of_discipline"
category: "tutp8"
---

# Creating the actions for the import of the discipline library into the modular system

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating the actions for the import of the discipline library into the modular system The upgrade to extension points has the advantage that during the configuration of a machine or plant only mechatronic components are involved and the data model therefore remains smaller. Only when the documents of a discipline have to be created for the completely configured machine or plant, are the discipline components installed per import of the discipline library and update of the extension points. Both the import as well as the update are to be triggered through actions by means of buttons of a user interface. The actions are based on a command and a SequenceSelectionAction that are created in the following steps. [Creating the command for the import of a library](javascript:void\(0\);)
    1. Select the T_Mechatronic_ModularSystem library.
    2. Select New > Engineering > Unit in the popup menu.
    3. Specify the Actions name.
    4. Select the new Actions unit.
    5. Select New > Object in the popup menu.
    6. Click Object > Command.
    7. Confirm with [Finish].
    8. Specify the ImportLibCommand name.
    9. Switch to the Methods editor page.
    10. Click .
    11. The New Name has to be entered in the table and the Name field.
    12. Specify execute as the name.
    13. In the drop-down list select LanguageSequence.
    14. In the Arguments area click on .
    15. The New Argument with the Engineering.Object type is entered in the table of the arguments.
    16. Enter root as the name.
    17. Enter Engineering.Root as the type.
    18. Repeat Steps 13 to 15 with the name libNames and the type Engineering.List.
The new arguments are entered as values for the signature of the method. It is now an execute method that requires the root node of the mechatronic and the list of the libraries to be imported as arguments. A table is shown below with the specification of type names, method names and method arguments.
    1. Click  above the table.
    2. In the Select method dialog, click Object > Command > FrameworkCommand > ImportLibrariesCommand.
    3. Confirm with [Finish].
    4. Repeat Steps 18 to 20 with Object > Command > FrameworkCommand > SaveObjectCommand.
    5. Save the command.
    6. With this command the framework commands for the import of libraries and the subsequent saving are performed.
    7. This concludes the creation of the command for the import of a library.
[Creating the SequenceSelectionAction for the update of extension points](javascript:void\(0\);)
    1. Select the Actions unit.
    2. Select New > Object in the popup menu.
    3. Click Object > Action > SelectionAction > SequenceSelectionAction.
    4. Confirm with [Finish].
    5. Specify the UpdateExtensionPointsAction name.
    6. Specify Update Extension Points in the Displayed Name field.
    7. Switch to the Methods editor page.
    8. Click .
    9. Click Object > Command > FrameworkCommand > StartFormulaCacheCommand.
    10. Confirm with [Finish].
    11. Repeat Steps 8 to 10 with Object > Command > FrameworkCommand > UpdateExtensionsCommand.
    12. Repeat Steps 8 to 10 with Object > Command > FrameworkCommand > StopFormulaCacheCommand.
    13. Repeat Steps 8 to 10 with Object > Command > FrameworkCommand > SaveObjectCommand.
    14. Switch to the Attributes editor page.
    15. Specify Component in the Selected object field.
    16. Save the SequenceSelectionAction.
    17. With this SequenceSelectionAction the framework commands for starting the formula cache, update of extension points, stopping the formula cache and the subsequent saving are performed consecutively.
    18. This completes the creation of the SequenceSelectionAction for updating the extension points.
The created actions are then linked with interfaces in a small user interface. The user interface (Form-UI) is created for the component Feeder and therefore is available directly after the creation of a project. [Creating the Form-UI for Feeder](javascript:void\(0\);) With the user interface you can not only set up the interfaces for the import of the library but you can also make the option for checking workpiece available for selection.
    1. Open the Feeder component.
    2. Change to the UI configuration editor page.
    3. Open the Source tab.
    1. In the <form> tag specify the Feeder title and the ID feeder.
    2. Insert the following lines after the opening tag <form>:
    
        <line>
    	<label font="Arial-20-bold">Feeder configuration</label>
    </line>
    <line>
    	<gap hSizePx="10"/>
    </line>
    <line>
    	<input receiver="=parameter('Option_Inspect_available')" type="check" ></input>
    	<label font="Arial-12">Add workpiece inspection</label>
    </line>
    <line>
    	<gap hSizePx="10"/>
    </line>
    <action name="T_Mechatronic_ModularSystem.Actions.ImportLibCommand" 
    	arguments="=List{this.mroot.parent, List{'T_ECAD_P8'}}" 
    	type="button" 
    	text="Import ECAD P8 Discipline">
    </action>
    <action name="T_Mechatronic_ModularSystem.Actions.UpdateExtensionPointsAction" 
    	arguments="=mroot" 
    	type="button" 
    	text="Update extensions">
    </action>

Through the first three rows the user interface receives the Feeder configuration header. The header is followed by three rows to create space. Below that is a row with a check box, followed by a text. The check box influences the Option_Inspect_available parameter that amongst others is used for the Disabler of the function groups Inspect and Discard. Three further lines follow to create space to the buttons. This is followed by two buttons that can each perform actions. The first button triggers the action to import the library T_ECAD_P8. With the second button the action for updating the extension points is performed. [Setting the default value for the Option_Inspect_available parameter](javascript:void\(0\);) The check box for the Option_Inspect_available parameter in the user interface should always have a defined state at the beginning of the configuration. In this case the check box should not be selected, so that the value is false.
    1. Open the Option_Inspect_available parameter.
    2. Switch to the Formula editor page.
    3. Enter false in the Value field.
    4. Save the parameter.
This value is now specified as the default value. As a result the Add workpiece inspection option will not be selected when opening the user interface for the first time. Read more
     * [Form-UI](refformui_r_formui.htm)
     * [action](refformui_r_action.htm)
