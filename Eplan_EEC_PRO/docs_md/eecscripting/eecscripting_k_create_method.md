---
title: "Creating a native method"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecscripting_k_create_method.htm"
file: "eecscripting_k_create_method"
category: "eecscripting"
---

# Creating a native method

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Creating a native method

Under the newly created unit (in the example: de.eplan.eec.scripting) create a class for the new method New > Class.

    1. Select the unit (here de.eplan.eec.scripting).
    2. Select New > Class  from the popup menu.

The wizard for the creation of a new Java class starts.

The name of the unit is already entered in the Package field. In accordance with naming conventions, it should be extended by .methods, if more than several methods developed in a package.

    1. Enter a (meaningful) name for the new class in the Name field. This name is usually identical to the name of the method it contains.
    2. Use [Browse...] in the Superclass field to add the class com.mind8.mechatronic.skill.methods.AbstractNativeMethod.
    3. Add the com.mind8.mechatronic.INativeMethod interface in the Interfaces field by using [Add...].
    4. Ensure that the public static void main(String[args]) check box is not activated as well as that the Constructors from superclass and Inherited abstract methods buttons are activated.
    5. Close the wizard via [Finish].

The newly created method is opened in the editor and completed there.

Before this a view of the data structure:

Because of the previous steps the units de.eplan.eec.scripting with the file NativeMethodExtension.java and de.eplan.eec.scripting.methods with the file IncrementLength.java have arisen. In the NativeMethodExtension.java file the connection between the method of the IncrementLength.java file and the method in EEC is later established.

The following figure shows the previously created class IncrementLength.

Explanations on the example code:

The created class must be derived from AbstractNativeMethod (extends AbstractNativeMethod) and the interface INativeMethod implements (implements INativeMethod). See Line 10.

The constructor of the method must be created with the visibility modifier public. If the visibility is not public, an error message occurs during the registration of the method. If creation of the constructor is transferred to the Eclipse, the visibility modifier is protected and thereby prevents the registration and execution of the method. In this case the visibility modifier has to be manually corrected (see Line 12).

In fact this method only consists of the return of zero.

With this the created class is complete. The method contained in it is subsequently registered and the plug-in is compiled.
