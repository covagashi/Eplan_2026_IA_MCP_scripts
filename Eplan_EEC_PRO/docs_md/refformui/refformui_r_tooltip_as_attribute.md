---
title: "Tooltip as Attribute"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_tooltip_as_attribute.htm"
file: "refformui_r_tooltip_as_attribute"
category: "refformui"
---

# Tooltip as Attribute

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Tooltip as Attribute Tooltips may appear in two different forms:
     * as a simple text, which cannot be further specified:
tooltip="Text"
     * as a popup window that has all the facilities of a Form UI:
tooltip="AbsolutePathToComponent#Page:Form-UI-Page" AbsolutePathToComponent = absolute path to the component that contains the Form-UI of the tooltip. Without the path declaration, the page is sought in the own component. #Page:Form-UI-Page = ID of the Form-UI, which is to be displayed as the tooltip A tooltip as simple text: [Example code](javascript:void\(0\);)
    
        <label tooltip="Tooltip with text">Label with text tooltip</label>

Result: A tooltip as popup window: The content is created in a Form-UI, that is located in the same component. [Example code](javascript:void\(0\);)
    
        <label tooltip="Documentation_UI_Configuration.Mechatronic.Documentation#Page:tooltip">

Result:
