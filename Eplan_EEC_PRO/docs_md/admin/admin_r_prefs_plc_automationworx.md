---
title: "AutomationWorX"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_prefs_plc_automationworx.htm"
file: "admin_r_prefs_plc_automationworx"
category: "admin"
---

# AutomationWorX

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## AutomationWorX

Path to the preferences:

Menu Window > Preferences

Dialog Preferences > Disciplines > PLC > AutomationWorX

     * The Source folder specifies which folder is initially searched for AutomationWorX source files.

Default value: <EEC installation folder>\resources\PLC

The absolute path is shown below the input field.

For Source folders absolute local paths, absolute UNC paths as well as relative paths are valid:

Absolute paths are used as specified.

Relative paths consist of the specification for -Dde.eplan.eec.global.resourcePath in the initialization file (for example ec.ini) and this specification. If no path is specified for -Dde.eplan.eec.global.resourcePath in the initialization file, the path consists of the EEC installation folder and the relative path.

### [Example for a local path](javascript:void\(0\);)

Specification in the initialization file: -Dde.eplan.eec.global.resourcePath=C:\Users\Public\EPLAN\EngineeringConfiguration\2022_1\resources

Specification for Source folder = plc\automationworx

Resulting path = C:\Users\Public\EPLAN\EngineeringConfiguration\2022_1\resources\plc\automationworx

### [Example for a UNC path](javascript:void\(0\);)

Specification in the initialization file: -Dde.eplan.eec.global.resourcePath=\\\myShare\resources\

Specification for Source folder = plc\automationworx

Resulting path = \\\myShare\resources\plc\automationworx

### Note

Only existing folders are valid. Non-existing folders are not created by EEC.

### Read more

     * [Preferences for disciplines](admin_r_prefs_disciplines.htm)
