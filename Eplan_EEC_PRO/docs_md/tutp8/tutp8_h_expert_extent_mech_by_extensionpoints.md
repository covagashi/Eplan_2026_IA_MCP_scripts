---
title: "Installing the extension points in mechatronic components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_expert_extent_mech_by_extensionpoints.htm"
file: "tutp8_h_expert_extent_mech_by_extensionpoints"
category: "tutp8"
---

# Installing the extension points in mechatronic components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Installing the extension points in mechatronic components Extension points are now installed in all mechatronic components in which Eplan Electric P8 components were installed fixed. This affects the following mechatronic components:
     * Feeder,
     * Positionsensor_Inductive,
     * Pressuresensor,
     * Positionsensor_optical.
[Creating the extension point for the schematic](javascript:void\(0\);)
    1. Open the Feeder component.
    2. Delete the installed components Schematic, PLC-Sensors_1_8 and PLC_Sensors_9_16.
    3. Click  to open the Finder dialog.
    4. Mark the Placeholder.
    5. Confirm with [Finish].
    6. Change the name from Placeholder to Schematic.
    7. Click [...] in the Type field to open the type finder.
    8. Enter the character I in the Name field.
    9. Click [Search].
    10. Select the ISchematic interface.
    11. Confirm with [OK].
    12. Enter the value 0..1 in the Number field.
    13. Mark the Extension point check box.
    14. In the Selection formula field, enter the value =1.
    15. Save the component.
In the future a component that implements the ISchematic interface is installed on the extension point. The quantity is limited to the value 1 and the selection formula only allows a single component. [Creating the extension point for schematic pages whose number is calculated](javascript:void\(0\);) The number of installed sensors is evaluated for the extension point on which the schematic pages are to be installed. To simplify the formula for the evaluation a parameter is required that saves the number of installed sensors. Creating the Sensors parameter:
    1. Mark the Mechatronic.Parameter unit in the T_Mechatronic_ModularSystem library.
    2. Select New > Engineering > Parameter.
    3. Specify the Sensors name.
    4. Specify the Collection type.
    5. Save the parameter.
Insert the Sensors parameter in Feeder:
    1. Open the Feeder component.
    2. Switch to the Parameter editor page.
    3. Drag the Sensors parameter from the Mechatronic.Parameter unit into the editor page.
    4. Enter the following formula as the value:
    
        =rmos('IMechSensor')

    1. Save the Feeder component.
Creating the extension point for schematic pages:
    1. Repeat Steps 2 to 10 of the previous extension point creation, in the process rename the placeholder to SchematicPages and as the type select the ISchematicPage interface.
    2. Leave the asterisk in the Number field.
    3. Mark the Extension point check box.
    4. Enter the following formula in the Selection formula field:
    
        =if (mroot.$Sensors.size.mod(8) > 0) then (mroot.$Sensors.size / 8 + 1) else (mroot.$Sensors.size / 8) endif

    1. Save the component.
Note on the number and selection formula: The value in the number field specifies the overall number of components that can be inserted. The number of components of an insertable type is specified in the Selection formula field. Here the overall number is not restricted. The number of insertable components (schematic pages) is calculated. On one page 8 sensors can be placed. Therefore the overall number modulo 8 is calculated. If a rest remains, the sensors have to be placed on an additional page, so that a 1 has to be added to the result. [Creating the extension points for sensors](javascript:void\(0\);)
    1. Open the Positionsensor_inductive component.
    2. Delete the installed Sensor_Inductive component.
    3. Save the component Positionsensor_inductive.
    4. Click  to open the Finder dialog.
    5. Mark the Placeholder.
    6. Confirm with [Finish].
    7. Change the name from Placeholder to Sensor_inductive.
    8. Click [...] in the Type field to open the type finder.
    9. Enter the character I in the Name field.
    10. Click [Search].
    11. Select the ISensorInductive interface.
    12. Confirm with [OK].
    13. Enter the value 0..1 in the Number field.
    14. Mark the Extension point check box.
    15. In the Selection formula field, enter the value 1.
    16. Save the component.
    17. Repeat steps 1 to 16 with the component Positionsensor_optical, rename the placeholder to Sensor_optical and set the values for Type to ISensorOptical, Number to 0..1 and Selection formula to 1.
    18. Repeat steps 1 to 16 with the component Pressuresensor, rename the placeholder Sensor_pressure and set the values for Type to ISensorPressure, Number to 0..1 and Selection formula to 1.
    19. Through the transition to extension points, the parameters of the sensors are applied to encapsulating mechatronic components and are not part of the T_Mechatronic_ModularSystem anymore.
The parameters have to be removed in the abstract Positionsensor sensor.
    1. Open the component Positionsensor.
    2. Switch to the Parameter editor page.
    3. Mark all parameters.
    4. Click  to delete the parameter.
    5. Save the component.
The number of pages in the projects orientates itself towards the number of sensors that implement the IMechSensor interface. Implementing the IMechSensor interface in Sensors:
    1. Open the Positionsensor_inductive component.
    2. Switch to the Interfaces editor page.
    3. Click  to open the Finder dialog.
    4. Enter the character I in the Name field.
    5. Click [Search].
    6. Mark the IMechSensor.
    7. Confirm with [Finish].
    8. Save the component.
    9. Repeat Steps 1 to 8 for the Positionsensor_optical and Pressuresensor components.
