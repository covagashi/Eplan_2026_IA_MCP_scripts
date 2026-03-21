---
title: "getImportedLibraryNames"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_util_getimportedlibrarynames.htm"
file: "refformulas_r_util_getimportedlibrarynames"
category: "refformulas"
---

# getImportedLibraryNames

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  getImportedLibraryNames Util methods Delivers a list of strings with the names of the directly imported libraries. getImportedLibraryNames  
---  
Argument | String | projectName | Name of the project  
Return value | List | List with the names of the imported libraries  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=type('Engineering.Util').getImportedLibraryNames('Feeder') | [T_Mechatronic_ModularSystem]
