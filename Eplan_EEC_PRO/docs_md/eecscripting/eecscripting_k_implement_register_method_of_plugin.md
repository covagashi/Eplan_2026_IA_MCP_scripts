---
title: "Registering the plug-in method"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecscripting_k_implement_register_method_of_plugin.htm"
file: "eecscripting_k_implement_register_method_of_plugin"
category: "eecscripting"
---

# Registering the plug-in method

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Registering the plug-in method The native implementation must first be registered before it can be applied in the EEC. The registration of the new method is entered in the previously created class NativeMethodExtension. Specifications are required for the registration of the new method that are only available after the creation of the method in EEC. The following figure therefore preempts the following step to illustrate the connection between registration of the native method and the method in EEC. The new method (e.g. IncrementLength) can be registered with the registerMethod method. The new method is registered with the following arguments.
     * Argument 1: Type which provides the method (here Mechatronic.Actions.IncrementValueCommand, meaning the name of the command in EEC).
     * Argument 2: Name of the method (here execute).
     * Argument 3: Array of the parameter types (here new String[]{"Engineering.Object"}, any EO is therefore expected).
     * Argument 4: true for method on class level, false for method on instance level (here true, the method is implemented in the modular system).
     * Argument 5: Class which implements the method (here IncrementLength.class, meaning the name of the class in Line 12 of the implementation, see [Creating a class for the extension](eecscripting_k_implement_create_class_for_extension.htm)).
Note If the type of the method, for example the library name, is changed in EEC, the type must be adjusted in this method and the plug-in must be compiled and exported again.
