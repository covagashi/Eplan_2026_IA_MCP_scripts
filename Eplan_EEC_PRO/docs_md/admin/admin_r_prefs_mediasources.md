---
title: "Media sources"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_prefs_mediasources.htm"
file: "admin_r_prefs_mediasources"
category: "admin"
---

# Media sources

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## Media sources

Path to the preferences:

Menu Window > Preferences

Dialog Preferences > Disciplines > Media sources

     * The Resources folder specifies which folder is initially searched for media source files.

Default value: <EEC installation folder>\resources\MediaSources

The absolute path is shown below the input field.

Both absolute local paths, absolute UNC paths as well as relative paths are valid for Resources folders:

Absolute paths are used as specified.

Relative paths consist of the specification for -Dde.eplan.eec.global.resourcePath in the initialization file (for example ec.ini) and this specification. If no path is specified for -Dde.eplan.eec.global.resourcePath in the initialization file, the path consists of the EEC installation folder and the relative path.

### [Example for a local path](javascript:void\(0\);)

Specification in the initialization file: -Dde.eplan.eec.global.resourcePath=C:\Users\Public\EPLAN\EngineeringConfiguration\2022_1\resources

Specification of Resource folder = media

Resulting path = C:\Users\Public\EPLAN\EngineeringConfiguration\2022_1\resources\media

### [Example for a UNC path](javascript:void\(0\);)

Specification in the initialization file: -Dde.eplan.eec.global.resourcePath=\\\myShare\resources\

Specification of Resource folder = media

Resulting path = \\\myShare\resources\media

### Note

Only existing folders are valid. Non-existing folders are not created by EEC.
