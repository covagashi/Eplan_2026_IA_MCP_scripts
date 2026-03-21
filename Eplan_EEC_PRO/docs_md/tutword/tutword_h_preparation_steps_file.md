---
title: "Preparatory steps on a file level"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutword_h_preparation_steps_file.htm"
file: "tutword_h_preparation_steps_file"
category: "tutword"
---

# Preparatory steps on a file level

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Preparatory steps on a file level Create the following folder on a file level (using Windows Explorer):
    
        <EEC installation folder>\resources\Office\Word\Tutorial

[Entering the path to the resources into the initialization file](javascript:void\(0\);) This section can be skipped when the initialization file has already been edited for another discipline of the tutorial. The initialization (ec.ini) file has to be edited in the following way:
    1. Open the initialization file in an editor (for example Notepad).
    2. Expand the specification for -Dde.eplan.eec.global.resourcePath= with <EEC installation folder>\resources (see [de.eplan.eec.global.resourcePath](admin_r_vmargs_global_resourcePath_new.htm)).
    3. Save the initialization file.
    4. Close the editor.
