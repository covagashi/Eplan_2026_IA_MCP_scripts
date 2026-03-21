---
title: "replacePlaceholderAbsPath"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_px_replaceplaceholderabspath.htm"
file: "eecbase_k_px_replaceplaceholderabspath"
category: "eecbase"
---

# replacePlaceholderAbsPath

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

replacePlaceholderAbsPath

## replacePlaceholderAbsPath

Searches the stated absolute path of a placeholder, and replaces it with a new absolute path.

Throws an exception if one of the stated paths contains null or empty strings.

replacePlaceholderAbsPath(String oldPlaceholderAbsPath, String newPlaceholderAbsPath)  
---  
Argument | String | oldPlaceholderAbsPath | Old absolute path of the placeholder.  
String | newPlaceholderAbsPath | New absolute path of the placeholder.  
Return value | Boolean | true = the absolute path of the placeholder has been replaced.  
true = no absolute path of the placeholder has been replaced.
