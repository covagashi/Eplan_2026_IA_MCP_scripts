---
title: "tempLocation()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_system_templocation.htm"
file: "refformulas_r_system_templocation"
category: "refformulas"
---

# tempLocation()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  tempLocation() System methods Determines the EEC temporary data folder in Windows notation, that means with backslashes as separators and a final backslash. This folder can also be explicit assigned in the initial file (e.g. ec.ini), for example âDjava.io.tmpdir=C:\User\username\AppData\Local\Temp **tempLocation()**  
---  
Argument |  |  |   
Return value | String | The EEC folder for temporary data  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=type('Engineering.System').tempLocation | C:\Users\username\AppData\Local\Temp\
