---
title: "Preparatory steps on a file level"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task1_preparation_files.htm"
file: "tutstep7_h_task1_preparation_files"
category: "tutstep7"
---

# Preparatory steps on a file level

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Preparatory steps on a file level Create the following folders on a file level (using Windows Explorer):
    
        C:\Users\Public\EPLAN\EngineeringCenter\<Build-ID>\resources\Tutorial
    C:\Users\Public\EPLAN\EngineeringCenter\<Build-ID>\resources\Tutorial\Step7

[Entering the path to the resources into the initialization file](javascript:void\(0\);) This section can be skipped when the initialization file has already been edited for another discipline of the tutorial. The initialization (ec.ini) file has to be edited in the following way:
    1. Open the initialization file in an editor (for example Notepad).
    2. Expand the specification for -Dde.eplan.eec.global.resourcePath= with <EEC installation folder>\resources (see [de.eplan.eec.global.resourcePath](admin_r_vmargs_global_resourcePath_new.htm)).  

    3. Save the initialization file.
    4. Close the editor.
