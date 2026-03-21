---
title: "ECAD P8 actions"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_ecad_actions.htm"
file: "eececad_k_ecad_actions"
category: "eececad"
---

# ECAD P8 actions

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## ECAD P8 actions

The following commands are available in Actions for the generation of the ECAD structure and of wiring diagrams:

    1. [ECAD.GenerateECADCodeCommand](refcommands_r_ecad_generateecadcodecommand.htm): Generates the schematic.
    2. [ECAD.GenerateEcadStructureCommand](refcommands_r_ecad_generateecadstructurecommand.htm): Generates the ECAD structure.
    3. [ECAD.OpenECADComponentCommand](refcommands_r_ecad_openecadcomponentcommand.htm): Generates and opens the schematic for the passed ECAD component. The created schematic only includes the passed components and all superordinate components.
    4. [ECAD.OpenECADPagesCommand](refcommands_r_ecad_openecadpagescommand.htm): Generates and opens the passed wiring diagrams of the project.
       * If the project is not existing yet, it is created, as by OpenECADComponentCommand.
       * If the project already exists, so the pages are created in it. If the pages already exist, the command replaces the existing pages by new ones.
    5. [ECAD.OpenProjectDiagramsCommand](refcommands_r_ecad_openprojectdiagramscommand.htm): Generates and opens all the wiring diagrams of a project.
    6. [ECAD.GenerateEcadProjectCommand](refcommands_r_ecad_generateecadprojectcommand.htm): Generates the ECAD project
    7. [ECAD.OpenEcadProjectCommand](refcommands_r_ecad_openecadprojectcommand.htm): Opens the relevant ECAD project
    8. [ECAD.UpdateEcadPagesCommand](refcommands_r_ecad_updateecadpagescommand.htm): Updates pages in the ECAD project
    9. [ECAD.GenerateEdzForEcadProjectCommand](refcommands_r_ecad_generateedzforecadprojectcommand.htm): Generates an EDZ file of the specified project components of the WiringDiagram type.
    10. [ECAD.GenerateXmlForEcadProjectCommand](refcommands_r_ecad_generatexmlforecadprojectcommand.htm): Creates a XML file ec-instructions.xml, as well as the macro files of the project which should be created in the specified folder.
