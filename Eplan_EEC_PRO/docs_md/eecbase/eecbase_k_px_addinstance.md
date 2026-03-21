---
title: "addInstance"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_px_addinstance.htm"
file: "eecbase_k_px_addinstance"
category: "eecbase"
---

# addInstance

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

addInstance

## addInstance

Adds a new project component.

addInstance(String parentAbsPath, String classAbsPath, String placeholderAbsPath, String instanceName, boolean isExtensionPlaced)  
---  
Argument | String | parentAbsPath | Absolute path to the superordinate project component.  
String | classAbsPath | Absolute path to the library component to be instantiated.  
String | placeholderAbsPath | Absolute path to the placeholder.  
String | instanceName | New name of the project component.  
Boolean | isExtensionPlaced | true = if the project component is to be added to a placeholder.  
false = if the project component is not to be added to a placeholder.  
Return value | void |
