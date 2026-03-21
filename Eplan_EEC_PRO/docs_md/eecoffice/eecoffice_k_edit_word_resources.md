---
title: "Edit resources of Word components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecoffice_k_edit_word_resources.htm"
file: "eecoffice_k_edit_word_resources"
category: "eecoffice"
---

# Edit resources of Word components

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Edit resources of Word components

If a Word file is assigned to a Word component as a resource, the editing of the Word file should always be started from EEC.

To edit the resource of a Word component, simply open the popup menu for this component and select Edit main document or Edit fragment document.

Word then opens and the file can be edited.

If Word is closed without saving, all of the changes are lost. If the file is saved and Word is then closed, EEC reads in the modified Word file. If the EEC detects that no changes were made to the required parameters, the new resource is implemented immediately. If changes to the parameters are detected, the Compare Editor opens. Only when this editor has been saved does EEC adopt the changes to the resource. If the Compare Editor is closed without saving, all of the changes to the Word file are lost.

### Note

After changing a Word resource, in some cases Word is not closed completely in background. Therefore the EEC process cannot be closed and the synchronize view cannot be opened, if parameter entries have changed or added. It is also not possible to edit another Word resource.

In these cases the Windows task of Word must be closed in task manager manually.
