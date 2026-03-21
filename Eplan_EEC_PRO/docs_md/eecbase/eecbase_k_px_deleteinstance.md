---
title: "deleteInstance"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_px_deleteinstance.htm"
file: "eecbase_k_px_deleteinstance"
category: "eecbase"
---

# deleteInstance

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

deleteInstace

## deleteInstance

Deletes the project component with the stated name in the superordinate component in all existing projects. The argument deleteAllInstances is to be set to true if all the project components of the specified name and their subordinate project components are to be deleted in all existing projects. The argument deleteAlsoParameters must be set to true even if the parameters of this project component are to be deleted.

deleteInstance(String parentName, String classAbsolutePath, String instanceName, boolean deleteAlsoParameters)  
---  
Argument | String | parentName | Absolute path to the superordinate project component. This specification is mandatory.  
String | classAbsolutePath | Absolute path to the class of the project component.  
String | instanceName | Name of the project component. The absolute path is formed from the parentName and instanceName. This specification is mandatory.  
Boolean | deleteAlsoParameters | Option whether to delete the parameters of the project component as well.  
true = delete parameters.  
false = do not delete parameters.  
Boolean | deleteAllInstances | Option whether all the project components with the specified name and their subordinate project components are to be deleted.  
true = delete all project components with the specified name.  
false = delete only the specified project component.  
Return value | Boolean | true = at least one project component has been deleted.  
false = no project component has been deleted.
