---
title: "Creating discipline components for Word"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutword_h_create_word_components_1.htm"
file: "tutword_h_create_word_components_1"
category: "tutword"
---

# Creating discipline components for Word

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating discipline components for Word A three-level hierarchy consisting of Body, Chapter, and Row is created as a result of splitting the target file. This hierarchy is now defined in a new unit.
    1. Begin by creating the Word_Components unit in the T_Mechatronic_ModularSystem library.
    2. Select the Word_Components unit.
    3. From the popup menu select New > Word > Main Document.
    4. Click [Import] and select the Body.docx file in the file selection dialog that subsequently appears.
The file name is entered automatically in the Name field.
    1. Repeat steps 2 to 4, but select Fragment document in step 3. Select the Word files Chapter.docx for the Word components with the name Chapter and Row.docx for the Word component with the name Row.
When importing the Word files, the parameters contained in them are automatically detected and are created in the Word.Parameter unit:
