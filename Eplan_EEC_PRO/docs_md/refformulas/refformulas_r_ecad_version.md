---
title: "version()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_ecad_version.htm"
file: "refformulas_r_ecad_version"
category: "refformulas"
---

# version()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  version() Returns the version of the executable file of the Eplan Electric P8 installation (w3u.exe), which is specified in the settings. version()  
---  
Argument |  |  |   
Return value | String | Version number of the currently selected executable file of the P8 installation. If no executable file of P8 (w3u.exe) is specified in the settings, Version 0.0.0 is returned.  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=type('ECAD.System').version() | 2.5.1
