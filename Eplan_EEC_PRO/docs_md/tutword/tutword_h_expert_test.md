---
title: "Testing upgrade"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutword_h_expert_test.htm"
file: "tutword_h_expert_test"
category: "tutword"
---

# Testing upgrade

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Testing upgrade The test of the upgrade is intended to show that the configuration can be first performed without the participation of discipline components. After the configuration a discipline can be added by importing a library. [Creating a project](javascript:void\(0\);)
    1. In the Project Catalog click .
    2. Specify Feeder1 as the name.
    3. Select the T_Mechatronic_ModularSystem library. The T_Office_Word and T_Images libraries are not automatically marked and should also not be.
    4. Click [Next >].
    5. The Feeder level component is automatically marked.
    6. Confirm with [Finish].
The Feeder1 project now exists in the Project catalog.
    1. Select the Feeder1 project.
    2. In the popup menu select Expand all.
Depending on the filter settings all project components and the extension points are now shown in the tree view. For this tutorial we recommend the following objects per filter setting:
     * Non-active objects
     * Categories
     * AutomationWorX
     * CoDeSys
     * ECAD
     * STEP 7
[Configuring a project without the option "Add workpiece inspection"](javascript:void\(0\);) Now open the Form-UI to configure the project.
    1. Select the Feeder project component.
    2. Select Form-UIs > Feeder in the popup menu.
    3. By default the value of the parameter Option_Inspect_available is false and the Add workpiece inspection check box is not activated.
[Importing a discipline library](javascript:void\(0\);) Which libraries are involved in the Feeder1 project shall be checked before and after the import. Before:
    1. Open the Feeder1 project library.
    2. Change to the Imported libraries editor.
Imported libraries: Import a discipline library per Form-UI:
    1. Select the Feeder component.
    2. Select Form-UIs > Feeder in the popup menu.
    3. Click the button [Import Word Discipline].
    4. Save the Form-UI.
After:
    1. Open the Feeder1 library.
    2. Change to the Imported libraries editor.
Imported libraries: After the import the discipline components of the T_ECAD_P8 library are available. [Updating extension points](javascript:void\(0\);) In the tree view of the project catalog you can see that no discipline components are inserted on the extension points.
    1. Select the Feeder component.
    2. Select Form-UIs > Feeder in the popup menu.
    3. Click the [Update Extensions] button.
    4. Save the Form-UI.
In the tree view of the project catalog you now can see that discipline components are inserted on all extension points. Note Discipline components are also inserted on the hidden extension points. However, these are not considered during the generation of the discipline documentation. [Generating discipline documents](javascript:void\(0\);) A Word document is generated from the existing discipline components with the following steps.
    1. Select the component Mechatronic.
    2. In the popup menu select Word > Generate Word Document.
Subsequently the structure of the Word components is created in the project catalog. It consists of the discipline components Body, two chapters with eight rows each.
    1. Select the component Mechatronic.
    2. In the popup menu select Word > Generate and open Word document.
Microsoft Word is opened and the generated document is displayed. The document contains a cover sheet, a table of contents and a page with tables of the actuators and sensors. Only the table of contents does not correspond to the current content. The table of contents for the field must be updated to this purpose.
    1. Close the Word document and exit Word.
    2. Select the component Mechatronic.
    3. In the popup menu select Word > Update Word document fields.
Microsoft Word is opened and the generated document is displayed. The table of contents now corresponds to the current content. [Configuring a project with the option "Add workpiece inspection"](javascript:void\(0\);) Open the Form-UI change again, to change the configuration.
    1. Select the Feeder component.
    2. Select Form-UIs > Feeder in the popup menu.
    3. Select the Add Workpiece Inspection check box.
    4. Save the Form-UI.
The Discard and Inspect components including extension points and discipline components placed on them are now included in the tree view of the Project catalog. Note The previous update of the extension points had an affect on the extension points of non-active components! Because of the filtering these have not been visible since then. [Re-generating a discipline component](javascript:void\(0\);) A Word document is re-generated with the added discipline components with the following steps.
    1. Select the component Mechatronic.
    2. In the popup menu select Word > Generate Word Document.
Subsequently the structure of the Word components is recreated in the project catalog. It consists of the discipline components body, two chapters, eight rows below chapter and 11 rows below the second chapter.
    1. Select the component Mechatronic.
    2. In the popup menu select Word > Generate and open Word document.
Microsoft Word is opened and the generated document is displayed. The document contains a cover sheet, a table of contents and a page with tables of the actuators and sensors. Only the table of contents does not correspond to the current content. The table of contents for the field must be updated to this purpose.
    1. Close the Word document and exit Word.
    2. Select the component Mechatronic.
    3. In the popup menu select Word > Update Word document fields.
Microsoft Word is opened and the generated document is displayed. The table of contents now corresponds to the current content. [Summary](javascript:void\(0\);) The advantage that extension points entail have no effect for smaller models in connection with an individual discipline. The bigger the model becomes and the more disciplines are added, the bigger the advantage of extension points becomes. The mechatronic modular system remains slim and clear. Discipline libraries can be changed and extended independently of each other.
