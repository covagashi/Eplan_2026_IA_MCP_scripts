---
title: "Preparatory steps on a file level"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_preparation_steps_files.htm"
file: "tutp8_h_preparation_steps_files"
category: "tutp8"
---

# Preparatory steps on a file level

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Preparatory steps on a file level The resource files of the different disciplines are saved in the subdirectories of a resource path. The resource path is entered into the initialization path (for example Ec.ini), whereas the subdirectories are selected in the settings. Create the following folder structure for the storage of the resources on the file level (with Windows Explorer):
    
        <EEC installation folder>\resources\ECAD\Tutorial
    <EEC installation folder>\resources\ECAD\Tutorial\P8

[Entering the path to the resources into the initialization file](javascript:void\(0\);) This section can be skipped when the initialization file has already been edited for another discipline of the tutorial. The initialization (ec.ini) file has to be edited in the following way:
    1. Open the initialization file in an editor (for example Notepad).
    2. Expand the specification for \- D= with <EEC installation folder>/resources/ECAD (see [de.eplan.eec.global.resourcePath](admin_r_vmargs_global_resourcePath_new.htm)).  

    3. Save the initialization file.
    4. Close the editor.
