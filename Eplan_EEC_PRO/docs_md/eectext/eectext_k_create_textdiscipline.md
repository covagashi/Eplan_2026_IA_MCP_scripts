---
title: "Creating a text discipline"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eectext_k_create_textdiscipline.htm"
file: "eectext_k_create_textdiscipline"
category: "eectext"
---

# Creating a text discipline

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating Creating a text discipline The Text discipline system library offers the system objects that are required for configuring text disciplines. A library in which a text discipline is to be created must therefore import the TextDiscipline library. A new text discipline is created by using the popup menu New > Text discipline.... When creating the object the discipline name is used in order to ensure that unambiguous names are created. This means that the specified name of the new text discipline is integrated into the name of the library objects. If, for example, you enter HTML for the new discipline, the following 10 objects are created in the library:
     * GenerateHTMLCodeCommand
     * GenerateHTMLStructureCommand
     * HTML
     * HTMLCodeGenerate
     * HTMLComponent
     * HTMLParserConfiguration
     * HTMLRoot
     * HTMLGenerateStructure
     * HTMLGenerateAndOpenStructure
     * OpenHTMLWithEclipseCommand
The objects can be edited in order to adjust the overall configuration of a text discipline. This is to be shown using HTML as an example.
