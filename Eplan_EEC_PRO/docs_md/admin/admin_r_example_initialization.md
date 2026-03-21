---
title: "Example of an ini file"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_example_initialization.htm"
file: "admin_r_example_initialization"
category: "admin"
---

# Example of an ini file

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Example of an ini file
    
        ; Hilfe zu Einstellungen von Laufzeitoptionen finden Sie in der Dokumentation
    ;(https://www.eplan.help/de-de/Infoportal/Content/EECPro/2.9/EPLAN_Help.htm) im Kapitel "Administration, Laufzeitoptionen"
    ;
    ; For additional information on runtime options, please see documentation
    ;(https://www.eplan.help/en-us/Infoportal/Content/EECPro/2.9/EPLAN_Help.htm) chapter "Administration, Runtime options"
    ;-showLocation
    -data
    workspace
    -vmargs
    -Dorg.foederal.sn.connectionURL=eox:///./eox/model.eox?mode=rw
    ; -Dorg.foederal.sn.connectionURL=proxy://any
    -Xmx1536m
    -Dde.eplan.eec.global.resourcePath=
    ;-Dde.eplan.eec.licenseFile=<path_to_.lis_file>
    -Dosgi.nl=de_DE
