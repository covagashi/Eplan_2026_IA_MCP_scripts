---
title: "Adding the extension for the plug-in"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecscripting_k_implement_assign_extension_for_plugin.htm"
file: "eecscripting_k_implement_assign_extension_for_plugin"
category: "eecscripting"
---

# Adding the extension for the plug-in

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Adding the extension for the plug-in EEC offers the extension point INativeMethodExtension via which the natively implemented methods can be registered. Once a new plug-in has been created, Eclipse opens the plug-in development perspective.
    1. Open the Extensions tab.
    2. Click [Add..] to start the wizard for creating an extension.
    3. Enter the name INativeMethodExtension in the Extension Point filter field.
Different extension points are now displayed in the list under the field.
    1. Deselect the Show only extension points from the required plug-ins check box to modify the list of extension points displayed.
    2. Select the com.mind8.mechatronic.skill.INativeMethodExtension extension point.
    3. Close the wizard by clicking [Finish].
A query follows whether the plug-in com.mind8.mechatronic.skill that declares the INativeMethodExtension extension point should be added to the list of plug-in dependencies.
    1. Confirm with [Yes].
The extension is now added to the list, but has not yet been saved.
    1. Save with [Ctrl] + [S].
