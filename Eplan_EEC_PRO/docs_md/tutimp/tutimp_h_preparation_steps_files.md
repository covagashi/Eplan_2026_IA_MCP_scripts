---
title: "Preparatory steps on a file level"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutimp_h_preparation_steps_files.htm"
file: "tutimp_h_preparation_steps_files"
category: "tutimp"
---

# Preparatory steps on a file level

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Preparatory steps on a file level An adapted mechatronics modular system and various import files are made available via a ZIP file for this tutorial. The files first have to be unzipped and stored into specific directories. Requirements:
     * EEC as a stand-alone installation Version 2.5.1 or higher.
Carry out the following steps to prepare the tutorial:
    1. Create the following folder on a file level (using Windows Explorer):
    
        <EEC installation path>\resources

    1. Unpack the contents of the following ZIP file into the folder of the preceding step:
    
        <EEC installation path>\install\Tutorial\Import\Tutorial_Import.zip

Subsequently the following directory structure exists under \resources:
    
        \Import
    \Import\CSV
    \Import\EOX
    \Import\IMX
    \Import\XML
    \Import\XSL

    1. Copy the file Tutorial_Import.eox from the directory
    
        <EEC installation path>\resources\Import\EOX\

into the directory
    
        <EEC installation path>\eox

The EOX file is used for all the following examples of this tutorial as data back end. A setting in the initialization file (ec.ini) has to be changed to this purpose. To ensure that the data back end file can be used for all steps of the tutorial, the access is restricted to Read-only (mode=r). To change the initialization file:
    1. Open the file <EEC installation path>\ec.ini in an any editor (e.g.++, Notepad).
    2. Replace the row
    
        -Dorg.foederal.sn.connectionURL=eox:///./eox/model.eox?mode=rw

by the row
    
        -Dorg.foederal.sn.connectionURL=eox:///./eox/Tutorial_Import.eox?mode=r

    1. Save the initialization file.
    2. Close the editor.
