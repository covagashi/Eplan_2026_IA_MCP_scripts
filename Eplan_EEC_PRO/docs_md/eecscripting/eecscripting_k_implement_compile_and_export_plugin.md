---
title: "Compiling and exporting a plug-in"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecscripting_k_implement_compile_and_export_plugin.htm"
file: "eecscripting_k_implement_compile_and_export_plugin"
category: "eecscripting"
---

# Compiling and exporting a plug-in

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Compiling and exporting a plug-in Before the new plug-in is compiled and exported, any EEC that is still running should be stopped. The following steps are necessary to export and compile the plug-in:
    1. Open the export wizard by selecting File > Export...
    2. Open the Plug-in Development branch.
    3. Select Deployable plug-ins and fragments.
    4. Confirm the selection with Next >.
    5. Select the plug-in to be exported (here de.eplan.eec.scripting).
    6. In the Destination tab, select the \dropins sub-folder of the EEC installation folder.
    7. Open the Options tab.
    8. Select the Package plug-ins as individual JAR archives check box.
    9. Finish with Finish.
Eclipse can then be closed and EEC can be restarted. During the start of EEC all plug-ins are registered. New plug-ins that are stored in the /dropins folder are also considered. [Testing registration of the new plug-in](javascript:void\(0\);) Proceed as follows to determine whether the new plug-in was successfully loaded in EEC:
    1. Start EEC
    2. Select Help > About Eplan Engineering Configuration.
    3. Click [Installation details].
    1. Open the Plug-ins tab.
    2. Navigate to the name of the new plug-in (here Example).
If the new plug-in is not listed, it has not been loaded. Check the following points:
     * Is the Native language marked in EEC for the method?
     * Do the specified arguments in the NativeMethodExtension.java correspond with the method definition?
     * Is the AbstractNativeMethod super class specified for the implementation of the method?
     * Is the INativeMethod interface specified for the implementation of the method?
     * Is the visibility modifier of the constructor of the implemented method public?
