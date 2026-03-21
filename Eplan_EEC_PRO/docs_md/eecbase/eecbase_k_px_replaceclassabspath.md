---
title: "replaceClassAbsPath"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_px_replaceclassabspath.htm"
file: "eecbase_k_px_replaceclassabspath"
category: "eecbase"
---

# replaceClassAbsPath

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

replaceClassAbsPath

## replaceClassAbsPath

Searches the stated absolute path of a library component, and replaces it with a new absolute path.

Throws an exception if one of the stated paths contains null or empty strings.

replaceClassAbsPath(String oldClassAbsPath, String newClassAbsPath)  
---  
Argument | String | oldClassAbsPath | Old absolute path of the class.  
String | newClassAbsPath | New absolute path of the class.  
Return value | Boolean | true = the absolute path of the class has been replaced.  
false = no absolute path of the class has been replaced.
