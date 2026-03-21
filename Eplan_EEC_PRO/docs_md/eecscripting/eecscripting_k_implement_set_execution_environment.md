---
title: "Specifying the runtime environment for the plug-in"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecscripting_k_implement_set_execution_environment.htm"
file: "eecscripting_k_implement_set_execution_environment"
category: "eecscripting"
---

# Specifying the runtime environment for the plug-in

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Specifying the runtime environment for the plug-in To avoid incompatible runtime environments, only the generally defined runtime environment should be specified for the newly developed plug-in. The general runtime environment to be used is defined in the initialization file (ec.ini). Other runtime environments could be entered in the MANIFEST.MF file and should be removed.
    1. Open the MANIFEST.MF file of the new plug-in.
    2. Open the Overview tab.
    3. Remove all entries in the Execution Environments list.
