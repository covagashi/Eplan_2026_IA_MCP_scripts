---
title: "Preparatory steps in EEC"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_preparation_steps_eec.htm"
file: "tutp8_h_preparation_steps_eec"
category: "tutp8"
---

# Preparatory steps in EEC

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Preparatory steps in EEC [Import EOX files for Eplan Electric P8](javascript:void\(0\);) The T_Ecad_Ui discipline library, as well as the T_Mechatronic_Architecture and T_Mechatronic_ModularSystem libraries created in the chapter âMechatronicâ must be available before the P8 macros are imported into EEC. Based on the initial situation, various EOX files that contain the corresponding libraries must be imported:
     * The model is empty, i.e., only the system libraries are available (also see [Filter](eecbase_k_filter.htm)). Import the following EOX files:
    
        <EEC installation folder>\install\Tutorial\Mechatronic\Mechatronic.eox
    <EEC installation folder>\install\Tutorial\P8\Ecad_Ui.eox

     * The model contains T_Mechatronic_Architecture and T_Mechatronic_ModularSystem , but not T_Ecad_Ui. Import this EOX file:
    
        <EEC installation folder>\install\Tutorial\P8\Ecad_Ui.eox

     * The model contains T_Ecad_Ui, but not T_Mechatronic_Architecture and T_Mechatronic_ModularSystem. Import this EOX file:
    
        <EEC installation folder>\install\Tutorial\Mechatronic\Mechatronic.eox.

Read more
     * [Importing libraries/projects as an EOX file](eecbase_k_eox_exchange_library_import.htm)
[Import ECAD libraries into T_Mechatronic_ModularSystem](javascript:void\(0\);) To add the functions for the ECAD discipline to the T_Mechatronic_ModularSystem model, you will need to import the T_Ecad_Ui library.
    1. Double-click to open the T_Mechatronic_ModularSystem library.
    2. Select the Imported libraries editor.
    3. Click .
The library finder now appears.
    1. Click [Search].
    2. Select the T_Ecad_Ui library.
    3. Confirm with [OK].
    1. The modifications can be adopted by clicking the disk icon at the top left (or using [Ctrl] \+ [S]).
In the following text, it is assumed that you save your modifications at the latest before opening the next object (diskette icon top left or by using the shortcut key [Ctrl] \+ [S]), and if not, when you see the prompt click [Yes]. [Set settings in EEC](javascript:void\(0\);) The Eplan Electric P8 macros are inserted via mass import. For this to work, the path to the macro files must be set correctly in the settings:
    1. Select Window > Settings.
The Settings window now appears.
    1. Select Disciplines > ECAD.
    1. Enter the following path in the Path of ECAD macros field:
    
        resources\Tutorial\P8

Eplan Electric P8 is started by EEC to generate the schematics. For this purpose, the path for the executable file W3u.exe must be made known to EEC:
    1. Select Disciplines > ECAD > Eplan Electric P8.
    2. In the Eplan Electric P8 executable field, enter the path for the file W3u.exe.
When generating the schematics, the MacroTemplate.zw9 macro project template, which was previously created by means of Eplan Electric P8, is applied.
    1. Select Disciplines > ECAD > Eplan Electric P8.
    2. In the Macro project template field, enter the path for the file Macro_Template.zw9.
    3. Confirm with [OK].
The field is already pre-filled with a path, but that path may be different from the one in the version that you use. If a different path is shown, you must do a restart after confirming.
    1. Confirm with [OK].
[Set model variables in EEC](javascript:void\(0\);) The following model variables have to be set for this tutorial so that both a specific unit for the storage of the parameters as well as specific parameter names exist uniformly for the subsequent importing of the P8 macros:
    1. Select Model > Model variables.
    2. Navigate to Disciplines > ECAD > Eplan Electric P8.
    3. Enter the value LocationDesignation for the model variable Parameter name for location designation.
    4. Enter the value Report for the model variable Parameter Name For The Report.
    5. Enter the value FunctionDesignation for the model variable Parameter Name for function designation.
    6. Enter the value PageNumber for the model variable Parameter Name For The Page Number.
    7. Enter the value SubPageNumber for the model variable Parameter Name For The Sub Page Number.
