---
title: "STEP 7"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_prefs_plc_s7.htm"
file: "admin_r_prefs_plc_s7"
category: "admin"
---

# STEP 7

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## STEP 7

Path to the preferences:

Menu Window > Preferences

Dialog Preferences > Disciplines > PLC > STEP 7

     * The Source folder specifies which folder is initially searched for STEP 7 source files.

Default value: <EEC installation folder>\resources\PLC

The absolute path is shown below the input field.

For Source folders absolute local paths, absolute UNC paths as well as relative paths are valid:

Absolute paths are used as specified.

Relative paths consist of the specification for -Dde.eplan.eec.global.resourcePath in the initialization file (for example ec.ini) and this specification. If no path is specified for -Dde.eplan.eec.global.resourcePath in the initialization file, the path consists of the EEC installation folder and the relative path.

### [Example for a local path](javascript:void\(0\);)

Specification in the initialization file: -Dde.eplan.eec.global.resourcePath=C:\Users\Public\EPLAN\EngineeringConfiguration\2022_1\resources

Specification for Source folder = plc\step7

Resulting path = C:\Users\Public\EPLAN\EngineeringConfiguration\2022_1\resources\plc\step7

### [Example for a UNC path](javascript:void\(0\);)

Specification in the initialization file: -Dde.eplan.eec.global.resourcePath=\\\myShare\resources\

Specification for Source folder = plc\step7

Resulting path = \\\myShare\resources\plc\step7

### Note

Only existing folders are valid. Non-existing folders are not created by EEC.

### Read more

     * [Preferences for disciplines](admin_r_prefs_disciplines.htm)
