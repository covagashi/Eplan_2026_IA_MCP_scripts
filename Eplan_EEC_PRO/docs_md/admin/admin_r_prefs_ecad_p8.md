---
title: "Eplan Electric P8"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_prefs_ecad_p8.htm"
file: "admin_r_prefs_ecad_p8"
category: "admin"
---

# Eplan Electric P8

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Eplan Electric P8

Path to the preferences:

Menu Window > Preferences

Dialog Preferences > Disciplines > ECAD > Eplan Electric P8

     * Eplan Electric P8 executable specifies the executable file of the Eplan Electric P8 application (W3u.exe). The executable file does not have to be specified, if EEC is only used to create EDZ files.
     * Macro project template specifies the name of a macro project template (*.zw9 file) for generation of schematics. The macro project template does not have to be specified, if EEC is only used to create EDZ files.

The absolute path is shown below the input field.

     * Automatically start API in background starts the Eplan API on start of EEC in background. This option can only be used if valid specifications are contained n the fields Eplan Electric P8 executable and Macro project template.
     * Keep plug/socket text objects avoids deletion of function text for Plugs and Sockets in the created schematics.
     * Keep macro boxes in window macros has the effect that the macro boxes of window macros are retained in the created schematics. If a schematic page with a window macro that consists of several symbol macros is to be created for a new part of the parts database (EDZ file), this option is to be activated.
     * Keep macro boxes in symbol macros has the effect that the macro boxes of symbol macros are retained in the created schematics. If a schematic page with a symbol macro that consists of several window macros is to be created for a new part of the parts database (EDZ file), this option is to be activated.
     * Reuse existing project for schematic generation accelerates the renewed generation of the same project. The creating and deleting of P8 projects using API takes considerable time. Schematic generation has therefore been optimized so that a project already created is kept during repeated creating. If the project already exists when a new schematic is to be created, EEC checks whether the project template for the project has remained the same. If yes, EEC deletes only existing pages and leaves the project. As a secondary effect an error message is no longer created if the project is still opened in a P8. This is particularly useful, if only individual pages are to be checked in a schematic.
     * Convert macros into groups during schematic generation groups all macros, which are located in a created schematic.
     * Continue P8 generation in case of an error prevents that the creation of schematics is canceled by the occurrence of an error. If this option is active, imperfections during the creation of a schematic are skipped and then if necessary C#-Scripts executed.
     * Delete placeholders after generation removes all placeholders after the P8 project has been created.

### Note

The Delete placeholders after generation option can be used as of Version 2.6 HF4 of Eplan Electric P8. If this option is active, the optional function P8 Integration Service Feature cannot be used.

The Communication server section is displayed when the optional function P8 Integration Service Feature is installed. There the set port is displayed with which communication between Eplan Electric P8 and EEC is effected.
