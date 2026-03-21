---
title: "Supplementing Eclipse initialization file"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecscripting_k_debug_edit_eclipse_ini_file.htm"
file: "eecscripting_k_debug_edit_eclipse_ini_file"
category: "eecscripting"
---

# Supplementing Eclipse initialization file

Info / CopyrightThis functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Supplementing Eclipse initialization file The initialization file of the installed Eclipse (eclipse.ini) has to be supplemented with the following row below the -vm row:
    
        <path to jdk>/bin/javaw.exe

Replace <path to jdk> with the current path to the installed JDK. Once the initialization file has been modified, EEC has to be restarted. Read more
     * [Software requirements](../../../../../../en-US/Infoportal/Content/swreqs/Content/htm/swreqs_k_eecpro.htm#JRE)
