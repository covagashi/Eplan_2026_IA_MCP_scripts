---
title: "Creating plug-in projects"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecscripting_k_implement_create_new_plugin_in_project.htm"
file: "eecscripting_k_implement_create_new_plugin_in_project"
category: "eecscripting"
---

# Creating plug-in projects

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating plug-in projects Note For this documentation Eclipse was used with an English user interface. All following texts that reference it are therefore in English. To create a plug-in, follow these steps:
    1. Open the wizard for a new project by selecting File > New > Project...
    2. Mark the Plug-in Project entry on the Select a wizard page.
    3. Confirm with [Next >].
    4. Enter the name for the new plug-in in the Project Name field.
In order to avoid naming conflicts to the greatest extent possible, the companyâs URL is entered in reverse order, and a meaningful name is added after a period. For example, the name of a Java script that identifies parent and child components is constructed as follows: http://www.eplan.de becomes de.eplan, and the meaningful name eec.scripting is added, resulting in de.eplan.eec.scripting.
    1. Confirm with [Next >].
    2. If desired, enter a longer name for the plug-in in the Name field.
    3. Enter your own company name in the Vendor field.
    4. Deselect the check box labeled This plug-in will make contributions to the UI.
    5. Close the wizard by clicking [Finish].
An adjusted perspective can be applied for the development of the plug-ins. As soon as the wizard for the creation of a new plug-in is closed, a query follows whether the adjusted perspective is to be opened.
    1. Click [Yes] to confirm that the perspective for plug-in development should be opened.
If you want the development perspective for plug-ins to open every time a new plug-in is created, check the Remember my decision check box. Eclipse opens the new plug-in in the plug-in development perspective The next section describes how to add the extension for the new plug-in.
