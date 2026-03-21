---
title: "Creating a method in EEC"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecscripting_k_create_method_in_eec.htm"
file: "eecscripting_k_create_method_in_eec"
category: "eecscripting"
---

# Creating a method in EEC

This functionality is only available for certain module packages. [This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Debugging via a command line The debugging can also be executed via the console. To do this enter the following command in the console:
    
        jdb -connect com.sun.jdi.SocketAttach:hostname=localhost,port=8000htr

The specification of the port must match the entry in the initialization file (for example -agentlib:jdwp=transport=dt_socket,address=8000,server=y,suspend=n). This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating a method in EEC The method of a new plug-in is created in a library component or a command.
     * Methods that are created in a command are usually executed at a specific time by the project engineer.
     * Methods that are created in a library component are executed after the end of the instantiation.
[Creating a method in a command](javascript:void\(0\);) For the example the method is created in the Mechatronic.Actions.IncrementValueCommand command. This name was specified during the registration of the native Java method. If the name is to be changed, the new name must be specified for the registration (see [Registering the plug-in method](eecscripting_k_implement_register_method_of_plugin.htm)). This is how the command is created (the library and unit is required):
    1. Mark the unit in which the new SequenceSelectionAction is created (here Actions).
    2. Select New > Object... from the popup menu.
    3. Navigate the selection dialog to Object > Command.
    4. Confirm with [Finish].
    5. Enter a name for the new command (here IncrementValueCommand).
    6. Open the Method tab.
    1. By clicking Add, add a new method to the list of methods..
    2. Specify the name of the method (here execute, this name has been specified for the registration of the method, see [Registering the plug-in method](eecscripting_k_implement_register_method_of_plugin.htm)).
    3. Select the Native language type.
    4. If applicable, mark the Static option.
    5. Add the arguments that are to be passed to the method and assign the respective type (here obj with the type Engineering.Object. This type has been specified for the registration, see [Registering the plug-in method](eecscripting_k_implement_register_method_of_plugin.htm)).
[Creating SequenceSelectionAction for starting the command](javascript:void\(0\);) An action is required, for example SequenceSelectionAction, to be able to execute the new command. This can be started from the popup menu of a component. This is how the SequenceSelectionAction is created:
    1. Mark the unit in which the new SequenceSelectionAction is created (here Actions).
    2. Select New > Object... from the popup menu.
    3. Navigate the selection dialog to Object > Action > SelectionAction > SequenceSelectionAction.
    4. Confirm with [Finish].
    1. Enter a name for the new SequenceSelectionAction (here IncrementValueSelectionAction).
    2. In the Selected object field, select the project component that owns the length parameter (here Station).
    3. Select the Visible in projects check box.
    4. In the Displayed Name field specify a name for the SequenceSelectionAction that is shown in the popup menu of the station (here Increment Value).
    5. Open the Methods editor page.
    1. Click .
    2. To insert the commands in the list, select the following commands one by one:
Object > Command > FrameworkCommand > StartFormulaCacheCommand Object > Command > IncrementValueCommand Object > Command > FrameworkCommand > StopFormulaCacheCommand Object > Command > FrameworkCommand > SaveObjectCommand
    1. Save the editor.
Subsequently the method can be started by calling up Increment Value from the popup menu of the station.
