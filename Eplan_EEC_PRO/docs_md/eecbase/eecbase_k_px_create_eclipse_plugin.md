---
title: "Creating a plug-in in Eclipse"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_px_create_eclipse_plugin.htm"
file: "eecbase_k_px_create_eclipse_plugin"
category: "eecbase"
---

# Creating a plug-in in Eclipse

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## Creating a plug-in in Eclipse

The PX updates are implemented in Java. To do this, the Eclipse development environment must be set up (see [Implementing native Java](eecscripting_k_implement_native_java.htm)).

A new plug-in project is created using the wizard of the same name:

    1. Open the menu File > New > Other.
    2. Select Plug-in Project.
    3. Confirm the selection with [Next >].

The plug-in project is given a name and settings for the source and output folder in the subsequent dialog.

    4. Enter a name for the plug-in in the Project Name field.
    5. Check the information for the Source folder and Output folder, as well the Eclipse version.
    6. Confirm with [Next >].

Information on the version and publisher of the plug-in is entered in the subsequent dialog.

    7. Enter the name of the plug-in in the Name field.
    8. Enter your own company name in the Provider field.
    9. Close the wizard with [Finish].

Eclipse then switches to the Plug-in Development perspective. Further settings can be configured there.

    10. Open the Dependencies tab.
    11. Add to the list of Required Plug-ins the plug-in com.mind8.project.exchange (1.0.1).
    12. Save the editor using [Ctrl] \+ [S].

The plug-in must be assigned an extension point. This is done in the Extensions tab.

    13. Open the Extensions tab.
    14. Add to the list of All Extensions the extension point com.mind8.project.exchange.IProjectExchangeModelUpdate.
    15. Enter in the toVersion field the version number to which the plug-in is updated (target version).
    16. Enter a self-explanatory name in the name field (optional).
    17. Enter a description of the plug-in in the description field (optional).
    18. Enter the EOX file name of a specific model in the modelID field if the plug-in is relevant only to this model. Do not enter an EOX file name if the PX updates are to be applied to all PX files.
    19. Save the editor using [Ctrl] \+ [S].

The Java class can be created on the same tab.

    20. Click the class link.

The New Java Class dialog opens.

    21. Without entering further information, confirm the dialog with [Finish].

Then, the new Java class is opened in an editor.
