---
title: "Encapsulating the discipline components in mechatronic components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_expert_encapsulate_discipline_comps.htm"
file: "tutp8_h_expert_encapsulate_discipline_comps"
category: "tutp8"
---

# Encapsulating the discipline components in mechatronic components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Encapsulating the discipline components in mechatronic components In the course of the tutorial discipline components were created once through a mass import. Then formulas (for example to calculate a plug) were entered for the parameter values. If a macro was changed, for example through another parameter and the discipline component synchronized with the changed macro, the parameter values were lost. For this reason each discipline component is enclosed (encapsulated) in a mechatronic component. In the mechatronic component the same parameters are created and the formulas inserted as values. The parameters of the discipline components then always reference the parameters (interface parameters) of the same name of the encapsulating mechatronic components. After a synchronization you then only have to insert the references on the interface parameter again. [Creating the unit structure for mechatronic components](javascript:void\(0\);) The mechatronic components are to be created in a unit structure, analog to ECAD.
    1. Select the T_ECAD_P8 library.
    2. Select New > Engineering > Unit in the popup menu.
    3. Enter the Mechatronic name.
    4. Save the unit.
    5. Select the Mechatronic unit.
    6. Repeat Steps 2 to 4 with the names Page, Schematic, PLC_Inputs.
[Creating the mechatronic components](javascript:void\(0\);) For each mechatronic component an encapsulating mechatronic component now has to be created. Creating the capsule for the Schematic discipline component
    1. Select the new Mechatronic > Schematic unit.
    2. From the popup menu select New > Mechatronic > Function.
    3. Specify the M_Schematic name.
    4. Switch to the Interfaces editor page.
    5. Click  to open the Finder dialog.
    6. Click [Search].
    7. Select ISchematic.
    8. Confirm with [OK].
    9. Drag the Schematic discipline component into the component editor.
    10. Select the installed discipline component Schematic.
    11. Mark all parameters.
    12. Select Add interface temperature from the popup menu.
    13. Save the component.
    14. A reference to the parameter of the superior component (capsule) by the same name is now entered as the value. These parameters were inserted into the capsule during the same step. The parameter values are entered at a later step.
Creating the capsule for the Page discipline component The Page discipline component inherits the Page parameter from the abstractPage. A constellation could result due to the capsuling through which the system would not be able to differentiate between the component and the Page parameter anymore. A error would be reported and the capsule as a result could not be saved. In addition, the type of the parameter has to be switched from String to Integer. Therefore the Page parameter first has to be renamed.
    1. In the ECAD.Parameter unit, open the Page parameter.
    2. Change the name to PageNo.
    3. Change the type to Integer.
    4. Save the parameter.
Subsequently create the encapsulating component.
    1. Select the new Mechatronic.Page unit.
    2. From the popup menu select New > Mechatronic > Function.
    3. Specify the M_SchematicPage name.
    4. Switch to the Interfaces editor page.
    5. Click  to open the Finder dialog.
    6. Click [Search].
    7. Select ISchematicPage.
    8. Confirm with [OK].
    9. Drag the Page discipline component into the component editor.
    10. Select the installed discipline component Page.
    11. Mark all parameters.
    12. Select Add interface parameter in the popup menu.
    13. Save the component.
Create one capsule each for the discipline components Sensor_Inductive, Sensor_optical and Sensor_Pressure.
    1. Select the new Mechatronic.PLC_Inputs unit.
    2. From the popup menu select New > Mechatronic > Function.
    3. Specify the M_Sensor_Inductive name.
    4. Switch to the Interfaces editor page.
    5. Click  to open the Finder dialog.
    6. Click [Search].
    7. Select ISensorInductive and ISensor.
    8. Confirm with [OK].
    9. Drag the Sensor_Inductive discipline component into the component editor.
    10. Select the installed discipline component Sensor_Inductive.
    11. Mark all parameters.
    12. Select Add interface parameter in the popup menu.
    13. Repeat Steps 1 to 12 with the names M_Sensor_optical and M_Sensor_Pressure as well as the interfaces ISensorOptical and ISensorPressure.
    14. Save the component.
    15. For sensors the Isensor interface has been inserted in addition to the specific interface to later determine the number of available sensors per formula.
