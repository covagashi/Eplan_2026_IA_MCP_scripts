---
title: "Creating project documents"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_generate_project_docu.htm"
file: "eececad_k_generate_project_docu"
category: "eececad"
---

# Creating project documents

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Creating project documents

You open the configured ECAD structure with an action for generating the schematic in the ECAD system.

To this purpose you use a self-created SequenceSelectionAction that, for example, opens the schematic in EPLAN Electric P8 via an entry in the popup menu of the schematic object (see [SequenceSelectionActions](eecbase_k_methodology_sequenceselectionaction.htm)).

Alternatively, you can also execute the action Open schematic for **one** page or fragment.

In addition it is possible to execute the action Open pages to open **several** selected pages.

EEC automatically enters information in each created page stating that it was created by EEC, provided that this feature is available in the Eplan Electric P8 version used. The property name is called Automatically created <11006> and contains the value EEC.

By entering this property, EEC can differentiate between its own created pages and those created externally. Start the Generate Schematic action again. Only the automatically created pages of the schematic will be modified and/or overwritten.

Externally created pages are overwritten only on request.

The commands come with different signatures, which allows them to be combined with each other easily.

Application 1: Action "Generate structure, generate schematic and open"

The object selected for the action is MechatronicRoot.

     * [ECAD.GenerateEcadStructureCommand](refcommands_r_ecad_generateecadstructurecommand.htm): Generates the ECAD structure.
     * [ECAD.GenerateEcadProjectCommand](refcommands_r_ecad_generateecadprojectcommand.htm): Generates the ECAD project.
     * [ECAD.OpenEcadProjectCommand](refcommands_r_ecad_openecadprojectcommand.htm): Opens the relevant ECAD project.

All three commands have a signature that fits the object MechatronicRoot.

The associated action SequenceSelectionAction now has the following methods:

     * [Engineering.StartFormulaCacheCommand](refcommands_r_engineering_startformulacachecommand.htm): Enable cache
     * [ECAD.GenerateEcadStructureCommand](refcommands_r_ecad_generateecadstructurecommand.htm): Generate an ECAD structure
     * [Engineering.StopFormulaCacheCommand](refcommands_r_engineering_stopformulacachecommand.htm): Disable cache
     * [Engineering.AbortExecutionIfErrorCommand](refcommands_r_engineering_abortexecutionIferrorcommand.htm): Termination if error has occurred
     * [Engineering.SaveObjectCommand](refcommands_r_engineering_saveobjectcommand.htm): Save
     * [Engineering.StartFormulaCacheCommand](refcommands_r_engineering_startformulacachecommand.htm): Enable cache
     * [ECAD.GenerateEcadProjectCommand](refcommands_r_ecad_generateecadprojectcommand.htm): Generate an ECAD project
     * [Engineering.StopFormulaCacheCommand](refcommands_r_engineering_stopformulacachecommand.htm): Disable cache
     * [Engineering.AbortExecutionIfErrorCommand](refcommands_r_engineering_abortexecutionIferrorcommand.htm): Termination if error has occurred
     * [Engineering.SaveObjectCommand](refcommands_r_engineering_saveobjectcommand.htm): Save
     * [ECAD.OpenEcadProjectCommand](refcommands_r_ecad_openecadprojectcommand.htm): Open associated ECAD project

Application 2: Action "Generate structure and generate schematic"

The object selected for the action is MechatronicRoot.

     * [ECAD.GenerateEcadStructureCommand](refcommands_r_ecad_generateecadstructurecommand.htm): Generates the ECAD structure.
     * [ECAD.GenerateEcadProjectCommand](refcommands_r_ecad_generateecadprojectcommand.htm): Generates the ECAD project.

Both commands have a signature that fits the object MechatronicRoot.

If the project is already loaded in an instance of Eplan Electric P8, the project only needs to be updated (select project, press the [F5] key) to represent the changes in the instance. To do this, the Eplan Electric P8 version must be configured in such a way that projects are not opened exclusively.

Application 3: Action "Generate schematic"

Depending on the action for the selected object, the command exhibits varying behavior:

If the object selected for the action is MechatronicRoot or EcadRoot, the command will create the entire wiring diagram.

If the object selected for the action is a list, the command will expect pages and or fragments as elements of the list. The command deletes all pages from the schematic, and then creates the selected pages as new again.

If the project is already loaded in an instance of Eplan Electric P8, the project only needs to be updated (select project, press the [F5] key) to represent the changes in the instance. To do this, the Eplan Electric P8 version must be configured in such a way that projects are not opened exclusively.

     * [ECAD.GenerateEcadProjectCommand](refcommands_r_ecad_generateecadprojectcommand.htm): Generates the ECAD project.

Application 4: Action "Update schematic"

The object selected for the action is a list. The command expects pages and / or fragments as elements of the list. It creates the pages and/or the pages with the selected fragments as completely new. Even if only a fragment of a page has been modified and selected the complete page is always regenerated. All other pages remain unchanged.

If the project is already loaded in an instance of Eplan Electric P8, the project only needs to be updated (select project, press the [F5] key) to represent the changes in the instance. To do this, the Eplan Electric P8 version must be configured in such a way that projects are not opened exclusively.

     * [ECAD.UpdateEcadPagesCommand](refcommands_r_ecad_updateecadpagescommand.htm): Updates all the pages of the ECAD project.

Application 5: Action "Open schematic"

The command opens an already created schematic using the Eplan Electric P8 version stated in EEC.

It does not matter which object (page, fragment, schematic, EcadRoot, etc.) has been selected.

The command reports an error if the project has not been created yet.

     * [ECAD.OpenEcadProjectCommand](refcommands_r_ecad_openecadprojectcommand.htm): Opens the relevant ECAD project.

Application 6: Creating an EDZ file for ECAD project

An EDZ file is created, which can be imported by Eplan Electric P8 by means of an add-on (see Description of EDZ format in the Eplan Electric P8 help). Since Eplan Electric P8 is not required to generate the EDZ file, specifying the ECAD settings is not necessary (see [Eplan Electric P8](admin_r_prefs_ecad_p8.htm)).

A root object must be selected for this action. All project components of the WiringDiagram type are affected. An EDZ file is created and its name is returned as the result.

     * [ECAD.GenerateEdzForEcadProjectCommand](refcommands_r_ecad_generateedzforecadprojectcommand.htm): Creates an EDZ file and returns the name of the created file.
