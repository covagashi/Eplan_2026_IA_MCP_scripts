---
title: "Engineering.RemoveImportedLibrariesAndExtensionsCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_engineering_removeimportedlibrariesandextensionscommand.htm"
file: "refcommands_r_engineering_removeimportedlibrariesandextensionscommand"
category: "refcommands"
---

# Engineering.RemoveImportedLibrariesAndExtensionsCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Engineering.RemoveLibrariesAndExtentionsCommand Engineering.RemoveImportedLibrariesAndExtensionsCommand Deletes from the project all instances of the specified library that were inserted into the project via an extension point. Instances of libraries that were imported implicitly by these libraries are also deleted. After deletion, these libraries are removed from libNames list. Argument | Type | Description  
---|---|---  
root | Root | Root object of the mechatronic structure or of a discipline structure  
libNames | List | Libraries to import
