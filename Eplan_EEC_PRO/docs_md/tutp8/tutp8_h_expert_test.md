---
title: "Generating the finished schematic"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_expert_test.htm"
file: "tutp8_h_expert_test"
category: "tutp8"
---

# Generating the finished schematic

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Generating the finished schematic The test of the upgrade is intended to show that the configuration can be first performed without the participation of discipline components. After the configuration a discipline can be added by importing a library. The test consists of the following steps: [Creating a project](javascript:void\(0\);)
    1. In the Project Catalog click .
    2. Specify Feeder1 as the name.
    3. Select the T_Mechatronic_ModularSystem library. The T_ECAD_P8 library is not automatically marked and should also not be.
    4. Click [Next >].
    5. The Feeder level component is automatically marked.
    6. Confirm with [Finish].
    7. The Feeder1 project now exists in the Project catalog.
    8. Select the Feeder1 project.
    9. Select Expand all from the popup menu.
Depending on the filter settings all project components and the extension points are now shown in the tree view. For this tutorial we recommend the following objects per filter setting:
     * Non-active objects
     * Categories
     * AutomationWorX
     * CoDeSys
     * STEP 7
     * Word
[Configuring a project without the option "Add workpiece inspection"](javascript:void\(0\);) Now open the Form-UI to configure the project.
    1. Select the Feeder component.
    2. Select Form-UIs > Feeder from the popup menu.
By default the value of the parameter Option_Inspect_available is false and the Add workpiece inspection check box is not activated. Since all required components are already installed according to the maximum principle, another configuration is not possible in this case. [Importing a discipline library](javascript:void\(0\);) Which libraries are involved in the Feeder1 project shall be checked before and after the import. Before:
    1. Open the Feeder1 library.
    2. Change to the Imported libraries editor.
Imported libraries: Import a discipline library per Form-UI:
    1. Select the component Feeder1.
    2. Select Form-UIs > Feeder from the popup menu.
    3. Click the button [Import ECAD P8 Discipline].
    4. Save the Form-UI.
After:
    1. Open the Feeder1 library.
    2. Change to the Imported libraries editor.
Imported libraries: After the import the discipline components of the T_ECAD_P8 library are available. [Updating extension points](javascript:void\(0\);) In the tree view of the project catalog you can see that no discipline components are inserted on the extension points.
    1. Select the Feeder component.
    2. Select Form-UIs > Feeder from the popup menu.
    3. Click the [Update Extensions] button.
    4. Save the Form-UI.
[Viewing the project scope](javascript:void\(0\);) In the tree view of the project catalog you can see that discipline components are now inserted on all extension points. Note Discipline components are also inserted on the hidden extension points. However, these are not considered during the generation of the discipline documentation. [Creating a schematic](javascript:void\(0\);) A schematic is created from the existing discipline components with the following steps.
    1. Select the component Mechatronic.
    2. From the popup menu select ECAD > Generate structure.
Subsequently the structure of the ECAD components is created in the project catalog. It consists of the discipline components WiringDiagram, a schematic page and seven sensors.
    1. Select the component Mechatronic.
    2. From the popup menu select ECAD > Generate structure and open.
    3. Eplan Electric P8 is opened and the project is displayed in the page navigator.
    4. One page is currently contained in the project.
    5. Seven sensors are inserted on it.
    6. Close Eplan Electric P8.
[Configuring a project with the option "Add workpiece inspection"](javascript:void\(0\);) Open the Form-UI change again, to change the configuration.
    1. Select the Feeder component.
    2. Select Form-UIs > Feeder in the popup menu.
    3. Select the Add Workpiece Inspection check box.
    4. Save the Form-UI.
The Discard and Inspect components including extension points are now included in the tree view of the Project catalog. [Updating extension points](javascript:void\(0\);) A schematic page is currently inserted on the SchematicPages extension point in the tree view of the Project catalog.
    1. Select the Feeder component.
    2. Select Form-UIs > Feeder from the popup menu.
    3. Click the [Update Extensions] button.
    4. Save the Form-UI.
[Viewing the new project scope](javascript:void\(0\);) Now two schematic pages are inserted on the SchematicPages extension point in the tree view of the Project catalog. Nothing has changed when it comes to the scope of the discipline structure, it has to be recreated. [Recreating a schematic](javascript:void\(0\);) A schematic is created again from the updated discipline components.
    1. Select the component Mechatronic.
    2. In the shortcut menu, select ECAD > Generate_structure.
    3. From the popup menu select ECAD > Generate structure and open.
Eplan Electric P8 is opened and the project is displayed in the page navigator. The project now contains the pages 1 PLC_Sensors_1_8 and 1 PLC_Sensors_9_16. Eight sensors are on the first page, two sensors are inserted on the second page. [Summary](javascript:void\(0\);) The advantage that extension points entail have no effect for smaller models in connection with an individual discipline. The bigger the model becomes and the more disciplines are added, the bigger the advantage of extension points becomes. The mechatronic modular system remains slim and clear. Discipline libraries can be changed and extended independently of each other.
