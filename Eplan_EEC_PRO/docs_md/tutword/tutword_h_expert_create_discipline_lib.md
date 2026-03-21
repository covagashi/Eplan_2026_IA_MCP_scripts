---
title: "Creating a library for the Word discipline"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutword_h_expert_create_discipline_lib.htm"
file: "tutword_h_expert_create_discipline_lib"
category: "tutword"
---

# Creating a library for the Word discipline

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating a library for the Word discipline Previously, the discipline components were inserted in the mechatronic modular system T_Mechatronic_ModularSystem below the Word_Components unit. The discipline components is now to be collected in their own library. Create a library with the name T_Office_Word, which imports the system library Word and the libraries already created Word_Ui, T_Mechatronic_Architecture, T_Images and T_Interfaces. See [Creating libraries](eecbase_k_libraries.htm). [Removing discipline components](javascript:void\(0\);) As long as instances of the discipline components are still installed in the mechatronic components, they cannot be moved into the new libraries T_Office_Word. Therefore all instances have to be removed first.
    1. Open the component Cylinder.
    2. Select the discipline component Row.
    3. Delete the discipline components with .
    4. Repeat Steps 1 to 3 for Valve, Posistionsensor_inductive, Positionsensor_optical and Pressuresensor.
    5. Repeat steps 1 to 3 for Feeder with the instances ListOfComponents, Actuators_Table and Sensors_Table.
Repeat Steps 1 to 3 for Valve, Posistionsensor_inductive, Positionsensor_optical and Pressuresensor. [Moving discipline components and parameters in the T_Office_Word library](javascript:void\(0\);) Making the T_Office_Word library visible for T_Mechatronic_ModularSystem
    1. Open the T_Mechatronic_ModularSystem library.
    2. Open the editor page Imported libraries.
    3. Click the symbol [Add library].
    4. In the Library finder dialog click [Search].
    5. Select the T_Office_Word library.
    6. Confirm with [OK].
    7. Save the library.
    8. The visibility is established.
Moving discipline components and parameters
    1. In the T_Mechatronic_ModularSystem library select the units Word, and Word_Components.
    2. Drag the units into the T_Office_Word library.
Undoing visibilities
    1. Open the T_Mechatronic_ModularSystem library.
    2. Open the editor page Imported libraries.
    3. Select the T_Office_Word library.
    4. Press the key [Del].
    5. Select the Word_Ui library.
    6. Press the key [Del].
    7. Save the library.
