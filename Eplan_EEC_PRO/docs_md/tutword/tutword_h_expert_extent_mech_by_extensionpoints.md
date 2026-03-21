---
title: "Installing extension points into mechatronic components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutword_h_expert_extent_mech_by_extensionpoints.htm"
file: "tutword_h_expert_extent_mech_by_extensionpoints"
category: "tutword"
---

# Installing extension points into mechatronic components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Installing extension points into mechatronic components You now have to install extensions points in all mechatronic components in which Word components have already been installed fixed. This affects the following mechatronic components:
     * Feeder,
     * Cylinder,
     * Valve,
     * Positionsensor_Inductive,
     * Pressuresensor,
     * Positionsensor_optical.
[Installing extension point for the main document](javascript:void\(0\);)
    1. Open the Feeder component.
    2. Click  in the component editor to open the Finder dialog.
    3. Mark the Placeholder.
    4. Confirm with [Finish].
    5. Change the name from Placeholder to Bodies.
    6. Click [...] in the Type field to open the type finder.
    7. Enter the character I in the Name field.
    8. Click [Search].
    9. Select the IBody interface.
    10. Confirm with [OK].
    11. Enter the value 0..1 in the Number field.
    12. Mark the Extension point check box.
    13. In the Selection formula field, enter the value =1.
    14. Save the component.
In the future a component that implements the IBody interface is installed on the extension point. The quantity is limited to the value 1 and the selection formula only allows a single component. Later an instance of M_Body is placed on this extension point through the update of the extension point. [Installing extension point for two chapters](javascript:void\(0\);) Two chapters are to be inserted into the Word document, one for the actuators and one for the sensors. Previously the discipline component Chapter was installed twice in the Feeder. A placeholder for chapters is now installed at the same place.
    1. Open the Feeder component.
    2. Click  in the component editor to open the Finder dialog.
    3. Mark the Placeholder.
    4. Confirm with [Finish].
    5. Change the name from Placeholder to Chapters.
    6. Click [...] in the Type field to open the type finder.
    7. Enter the character I in the Name field.
    8. Click [Search].
    9. Select the IChapter interface.
    10. Confirm with [OK].
    11. Enter the value 0..2 in the Number field.
    12. Mark the Extension point check box.
    13. In the Selection formula field, enter the value =2.
    14. Save the component.
[Installing an extension point for a row in all sensors and actuators](javascript:void\(0\);)
    1. Open the component Cylinder.
    2. Click  in the component editor to open the Finder dialog.
    3. Mark the Placeholder.
    4. Move the placeholder to the uppermost position with .
    5. Confirm with [Finish].
    6. Change the name from Placeholder to Rows.
    7. Click [...] in the Type field to open the type finder.
    8. Enter the character I in the Name field.
    9. Click [Search].
    10. Select the IRow interface.
    11. Confirm with [OK].
    12. Enter the value 0..1 in the Number field.
    13. Mark the Extension point check box.
    14. In the Selection formula field, enter the value =1.
    15. Save the component.
    16. Repeat Steps 1 to 15 for all other sensors and actuators.
