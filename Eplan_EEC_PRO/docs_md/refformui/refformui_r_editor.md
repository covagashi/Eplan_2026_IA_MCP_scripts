---
title: "Form-UI editor"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_editor.htm"
file: "refformui_r_editor"
category: "refformui"
---

# Form-UI editor

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Form-UI editor To render the Form-UI elements you can decide between SWT and SWING. The choice of renderer is made in the popup menu before choosing the Form-UI. A default renderer can be specified in the settings. The use of the renderer can also be set via the arguments for the virtual machine in EECâs initialization file (see also [Java Virtual Machine Arguments (VMArgs)](admin_r_vmargs.htm)). If a standard renderer is specified, the choice of renderer is omitted; if no standard renderer is specified, SWT is always used. If the value all is specified in the initialization file, the renderer selection will be triggered first, before the Form-UI selection (see the following illustration). If the choice of which Form-UI to display for a project component is made via the popup menu (1), it is possible to choose first the renderer (2) and then the Form-UI (3) of the project component. The Form-UI (e.g. "Table") is then opened with the new Form-UI editor: The Form-UI editor has no side menu, making the whole monitor surface usable for displaying the Form-UI. Form-UIs called by navigation elements are opened in the same editor. Note If the focus is on the Form-UI editor the data of the displayed Form-UI will be updated by using the [F5] key.
