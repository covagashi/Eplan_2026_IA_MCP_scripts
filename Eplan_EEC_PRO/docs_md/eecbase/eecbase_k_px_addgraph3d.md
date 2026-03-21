---
title: "addGraph3D"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_px_addgraph3d.htm"
file: "eecbase_k_px_addgraph3d"
category: "eecbase"
---

# addGraph3D

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

addGraph2D

## addGraph3D

Adds a Graph2D diagram to the project.

An exception is thrown under the following circumstances:

     * If the absolute path to the superordinate project component is null.
     * If the name of the diagram is null.
addGraph3D(String parentAbsPath, String documentName, String documentStoreAsString)  
---  
Argument | String | parentAbsPath | Absolute path to the superordinate project component.  
String | documentName | Name of the document definition.  
String | documentStoreAsString | The content of the diagram.  
Return value | void |
