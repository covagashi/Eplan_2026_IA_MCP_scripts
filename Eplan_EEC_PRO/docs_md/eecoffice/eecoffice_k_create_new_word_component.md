---
title: "Creating Word components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecoffice_k_create_new_word_component.htm"
file: "eecoffice_k_create_new_word_component"
category: "eecoffice"
---

# Creating Word components

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Creating Word components

New Word components are created in the library preferably by calling the corresponding unit via the popup menu as follows: New > Word > Main document to create a new main-document component, or New > Word > Fragment document to create a fragment-document component.

For the new Word component, enter a unique name and select the DOCX file to be imported. The path to the (external) DOCX file is subsequently displayed in the Resource path field.

When a resource is first selected, EEC enters the filename without the extension as the suggested value for the name of the component.

### Note

At present, the Office discipline only supports files in Office Open XML format after ECM-376, without macros. These files have a DOCX extension and are the default file format for Microsoft Word 2007 and newer versions of Microsoft Word.

When a new Word file is created in Windows Explorer via the popup menu, the file is 0 KB large and therefore empty. When it is opened for the first time and a zero is entered as the sole content and the file is saved, it increases in size to >10 KB. This is conventional Word behavior; an empty DOCX file is not initialized with the default content of the template (Normal.dot) until it is processed for the first time. However, because the 0 KB files contain no evaluable contents, errors occur when these files are assigned to the Office discipline. It is therefore advisable to create the Word file first, before the associated EEC object is created and the Word file is assigned to it as a resource.
