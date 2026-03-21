---
title: "Macro Folder"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_modelvar_p8macrofolder.htm"
file: "admin_r_modelvar_p8macrofolder"
category: "admin"
---

# Macro Folder

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Macro Folder

Path to model variable:

Disciplines > ECAD > Eplan Electric P8 > Folder

The path in which the initial search for P8 macros is carried out is specified with the model variables Macro Folder.

No default value is specified.

If a relative path is specified for the Macro Folder, the resulting absolute path is composed of the following settings:

    1. The specification for -Dde.eplan.eec.global.resourcePath= in the initialization file (e.g. ec.ini).
    2. The specification for Path to ECAD macros in the settings.
    3. The specification Macro Folder in the model variables.

An absolute path specification for the macro folder overrides the specifications in the initialization file and the settings.
