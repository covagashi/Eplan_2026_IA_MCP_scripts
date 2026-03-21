---
title: "globalResourcePath()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_system_globalrecourcepath.htm"
file: "refformulas_r_system_globalrecourcepath"
category: "refformulas"
---

# globalResourcePath()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  globalResourcePath() System methods Determines the EEC global resource folder in Windows notation, that means with backslashes as separators and a final backslash. This folder can also be explicit assigned in the initial file (e.g. ec.ini), for example -Dde.eplan.eec.global.resourcePath=E:\Users\Public\EPLAN\EngineeringConfiguration\2022_1\resources **globalResourcePath()**  
---  
Argument |  |  |   
Return value | String | The EEC resource folder  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=type('Engineering.System').globalResourcePath() | E:\Users\Public\EPLAN\EngineeringConfiguration\2022_1\resources\
