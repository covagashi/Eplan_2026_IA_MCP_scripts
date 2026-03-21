---
title: "addGraph2D"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_px_addgraph2d.htm"
file: "eecbase_k_px_addgraph2d"
category: "eecbase"
---

# addGraph2D

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

addGraph2D

## addGraph2D

Adds a Graph2D diagram to the project.

An exception is thrown under the following circumstances:

     * If the absolute path to the superordinate project component is null.
     * If the absolute path to the class of the document definition is null.
     * If the name of the document definition is null.
addGraph2D(String parentAbsPath, String documentDefinitionClassAbsName, String documentName, String documentStoreAsString)  
---  
Argument | String | parentAbsPath | Absolute path to the superordinate project component.  
String | documentDefinitionClassAbsPath | Absolute path to the class of the document definition.  
String | documentName | The name of the diagram.  
String | documentStoreAsString | The content of the diagram.  
Return value | void |
