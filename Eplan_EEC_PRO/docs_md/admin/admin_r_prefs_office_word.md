---
title: "Word"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_prefs_office_word.htm"
file: "admin_r_prefs_office_word"
category: "admin"
---

# Word

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Word

Path to the preferences:

Menu Window > Preferences

Dialog Preferences > Disciplines > Office > Word

     * The Resources folder specifies which folder is initially searched for Microsoft Word files.

Default value: <EEC installation folder>\resources\Office\Word

The absolute path is shown below the input field.

Both absolute local paths, absolute UNC paths as well as relative paths are valid for Resources folders:

Absolute paths are used as specified.

Relative paths consist of the specification for -Dde.eplan.eec.global.resourcePath in the initialization file (for example ec.ini) and this specification. If no path is specified for -Dde.eplan.eec.global.resourcePath in the initialization file, the path consists of the EEC installation folder and the relative path.

### [Example for a local path](javascript:void\(0\);)

Specification in the initialization file: -Dde.eplan.eec.global.resourcePath=C:\Users\Public\EPLAN\EngineeringConfiguration\2022_1\resources

Specification for Resources folder = office\word

Resulting path = C:\Users\Public\EPLAN\EngineeringConfiguration\2022_1\resources\office\word

### [Example for a UNC path](javascript:void\(0\);)

Specification in the initialization file: -Dde.eplan.eec.global.resourcePath=\\\myShare\resources\

Specification for Resources folder = office\word

Resulting path = \\\myShare\resources\office\word

### Note

Only existing folders are valid. Non-existing folders are not created by EEC.

### Read more

     * [Preferences for disciplines](admin_r_prefs_disciplines.htm)
