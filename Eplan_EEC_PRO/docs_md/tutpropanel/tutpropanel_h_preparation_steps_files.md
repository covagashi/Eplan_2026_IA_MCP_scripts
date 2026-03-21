---
title: "Preparatory steps on a file level"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutpropanel_h_preparation_steps_files.htm"
file: "tutpropanel_h_preparation_steps_files"
category: "tutpropanel"
---

# Preparatory steps on a file level

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Preparatory steps on a file level The resource files of the different disciplines are saved in the subdirectories of a resource path. For the discipline Pro Panel you only require the resource IEC_bas001.zw9 for the root component.
    1. Create the following folder structure for the storage of the resources on the file level (with Windows Explorer):
        
                <EEC installation folder>\resources\ECAD\Tutorial
        <EEC installation folder>\resources\ECAD\Tutorial\P8

    2. Copy the file IEC_bas001.zw9 from the <Eplan installation folder>\Data\Templates\<company name> folder into the <EEC installation folder>\resources\ECAD\Tutorial\P8 folder.
[Entering the path to the resources into the initialization file](javascript:void\(0\);) This section can be skipped when the initialization file has already been edited for another discipline of the tutorial. The initialization (ec.ini) file has to be edited in the following way:
    1. Open the initialization file in an editor (for example Notepad).
    2. Extend the specification for -Dde.eplan.eec.global.resourcePath= with .\resources (see [de.eplan.eec.global.resourcePath](admin_r_vmargs_global_resourcePath_new.htm)).  

    3. Save the initialization file.
    4. Close the editor.
