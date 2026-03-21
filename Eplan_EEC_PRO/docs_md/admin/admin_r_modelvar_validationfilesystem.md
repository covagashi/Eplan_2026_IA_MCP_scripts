---
title: "File system name check"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_modelvar_validationfilesystem.htm"
file: "admin_r_modelvar_validationfilesystem"
category: "admin"
---

# File system name check

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## File system name check

Path to model variable:

Validation

The NTFS file system allows a length of 255 characters for a file name, of which 4 characters are as a rule used for the file extension including the separating dot. In particular the absolute names of discipline components should be selected so that the created files do not exceed this length. The absolute names result amongst others from the depth of hierarchy levels. Components that do not affect the generation of target documents can have any length of name.

The restriction to 260 characters for the path length can be lifted for the Windows 10 operating system via the registry key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem\LongPathEnabled.

Select a value from the dropdown list to determine the type of message.

     * Ignore: Errors in the file system are ignored.
     * Warning: A warning is output for each error in the file system.
     * Error: An error message is output for each error in the file system.

Default value: Warning
