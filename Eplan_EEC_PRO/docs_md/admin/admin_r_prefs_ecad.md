---
title: "ECAD"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_prefs_ecad.htm"
file: "admin_r_prefs_ecad"
category: "admin"
---

# ECAD

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## ECAD

Path to the preferences:

Menu Window > Preferences

Dialog Preferences > Disciplines > ECAD

     * The Path to ECAD resources specifies which folder is initially searched for Eplan Electric P8 macros.

Default value: <EEC installation folder>\resources\ECAD

The absolute path is shown below the input field.

Absolute local paths, absolute UNC paths as well as relative paths are all valid:

Absolute paths are used as specified.

Relative paths consist of the specification for -Dde.eplan.eec.global.resourcePath in the initialization file (for example ec.ini) and this specification. If no path is specified for -Dde.eplan.eec.global.resourcePath in the initialization file, the path consists of the EEC installation folder and the relative path.

### [Example for a local path](javascript:void\(0\);)

Specification in the initialization file: -Dde.eplan.eec.global.resourcePath=C:\Users\Public\EPLAN\EngineeringConfiguration\2_7_20180202-1530\resources

Specification of Path to ECAD macros = Tutorial\P8

Resulting path = C:\Users\Public\EPLAN\EngineeringConfiguration\2_7_20180202-1530\resources\Tutorial\P8

### [Example for a UNC path](javascript:void\(0\);)

Specification in the initialization file: -Dde.eplan.eec.global.resourcePath=\\\myShare\resources\

Specification of Path to ECAD macros = Tutorial\P8

Resulting path = \\\myShare\resources\Tutorial\P8

### Note

Only existing folders are valid. Non-existing folders are not created by EEC.

### Read more

     * [Preferences for disciplines](admin_r_prefs_disciplines.htm)
