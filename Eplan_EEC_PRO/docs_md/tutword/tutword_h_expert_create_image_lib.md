---
title: "Creating a library for the image objects"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutword_h_expert_create_image_lib.htm"
file: "tutword_h_expert_create_image_lib"
category: "tutword"
---

# Creating a library for the image objects

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating a library for the image objects Previously, the image objects were directly inserted in the mechatronic modular system T_Mechatronic_ModularSystem below the Images unit. These components are now to be collected in their own library. Create a library with the name T_Images, which imports the system library MediaSource and the library T_Mechatronic_Architecture. See [Creating libraries](eecbase_k_libraries.htm). [Moving image objects in the T_Images library](javascript:void\(0\);) Making the T_Images library visible for T_Mechatronic_ModularSystem
    1. Open the T_Mechatronic_ModularSystem library.
    2. Open the editor page Imported libraries.
    3. Click the symbol [Add library].
    4. In the Library finder dialog click [Search].
    5. Select the T_Images library.
    6. Confirm with [OK].
    7. Save the library.
    8. The visibility is established.
Moving discipline components
    1. Select all the components in the T_Mechatronic_ModularSystem library in the Images unit.
    2. Drag the components into the T_Images library.
    3. Delete the Images unit in the T_Mechatronic_ModularSystem library.
Undoing visibilities The T_Mechatronic_ModularSystem library now does not require the visibility to the T_Images library anymore. The visibility is switched on and switched off later during the configuration. The visibility to the MediaSource library can not be undone yet since there are references to this.
    1. Open the T_Mechatronic_ModularSystem library.
    2. Open the editor page Imported libraries.
    3. Select the T_Images library.
    4. Press the key [Del].
    5. Save the library.
