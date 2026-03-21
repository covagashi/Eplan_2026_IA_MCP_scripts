---
title: "isAvailable()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_datasourceobjects_isavailable.htm"
file: "refformulas_r_datasourceobjects_isavailable"
category: "refformulas"
---

# isAvailable()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  isAvailable() Data source objects Returns true, if a connection to a data source has been successfully established. **isAvailable()**  
---  
Argument |  |  |   
Return value | Boolean | true = connection to the data source is successfully established  
false = no connection to the data source possible  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=type('Lib.Unit.MyDataSource').isAvailable() | false
