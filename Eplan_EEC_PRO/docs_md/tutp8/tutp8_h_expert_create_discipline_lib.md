---
title: "Creating the library for the discipline ECAD P8"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_expert_create_discipline_lib.htm"
file: "tutp8_h_expert_create_discipline_lib"
category: "tutp8"
---

# Creating the library for the discipline ECAD P8

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating the library for the discipline ECAD P8 Previously, the discipline components were inserted in the mechatronic modular system T_Mechatronic_ModularSystem below the ECAD unit. The discipline components is now to be collected in their own library. Create a library with the name T_ECAD_P8, which imports the system library ECAD and the self-created libraries already created T_Mechatronic_Architecture and T_Interfaces. See [Creating libraries](eecbase_k_libraries.htm). [Moving the discipline components into the library T_ECAD_P8](javascript:void\(0\);) Making the T_ECAD_P8 library visible for T_Mechatronic_ModularSystem
    1. Open the T_Mechatronic_ModularSystem library.
    2. Open the editor page Imported libraries.
    3. Click the symbol [Add library].
    4. In the Library finder dialog click [Search].
    5. Select the T_ECAD_P8 library.
    6. Confirm with [OK].
    7. Save the library.
    8. The visibility is established.
Moving the discipline components
    1. Mark the ECAD unit in the T_Mechatronic_ModularSystem library.
    2. Drag the unit into the T_ECAD_P8 library.
Undoing the visibility
    1. Open the T_Mechatronic_ModularSystem library.
    2. Open the editor page Imported libraries.
    3. Select the T_ECAD_P8 library.
    4. Press the key [Del].
    5. Save the library.
