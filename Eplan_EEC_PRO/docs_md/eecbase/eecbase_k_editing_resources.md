---
title: "Editing of resources directly from the EEC"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_editing_resources.htm"
file: "eecbase_k_editing_resources"
category: "eecbase"
---

# Editing of resources directly from the EEC

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Editing of resources directly from the EEC

Resources can be edited directly from within the EEC. For this purpose, in the popup menu of the discipline-specific component, select the Edit Resource action.

This mechanism can be applied to any resource. The editing is launched via the Edit Resource action. This is illustrated in the following example on the basis of the Sensors_Actuators_Body component:

If after editing the resource its interface has changed, the Synchronization editor will launch automatically, in which one must define the effects that the changes have on the model:

EEC finds the editor based on the type of the resource file of a component, for example, a specific editor for *.ema files. The assignment of editors to file types (file codings) is configured in the settings under General > Content types and General > Editors > File Assignments:

For association purposes, it is possible to distinguish between internal and external editors. If no internal editor is assigned, the file type is edited using the external editor that was previously configured in the operating system.

Internal editors: The internal editors are entered by default in the settings as template editors, recognizable by the extension (default), for example, for *.ema files, the internal editor Eplan project (default). We generally recommend the use of the internal template editors. If a resource is not edited by means of the internal template editor, but another internal editor, the synchronization process that keeps the data model consistent will not start. An error message will be displayed to point out this consequence.

External editors: In the file association dialog, external editors can be assigned explicitly within the EC, for example, Microsoft Word for *.txt editors. This mechanism (defined by Eclipse), however, is not used for editing external resources.

Reason: In order to be able to start the synchronization at the right time after editing external files, EEC must start the external editor as a subordinate process to find out the time when it was closed. Therefore, only the editors set up in the operating system are used for editing resources with external editors.

These editors are used automatically if the area Associated editors contains no other entries.
