---
title: "Preparatory steps in EEC"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutpropanel_h_preparation_steps_eec.htm"
file: "tutpropanel_h_preparation_steps_eec"
category: "tutpropanel"
---

# Preparatory steps in EEC

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Preparatory steps in EEC [Importing Eplan Pro Panel discipline libraries](javascript:void\(0\);) [Import EOX files for Eplan Pro Panel](javascript:void\(0\);) The T_ProPanel_Ui discipline library, as well as the T_Mechatronic_Architecture and T_Mechatronic_ModularSystem libraries created in the 'Mechatronics' section, must be available before the Pro Panel discipline components are imported. Based on the initial situation, various EOX files that contain the corresponding libraries must be imported:
     * The model is empty, i.e., only the system libraries are available (also see [Filter](eecbase_k_filter.htm)). Import the following EOX files:
    
        <EEC-Installationsordner>\install\Tutorial\Mechatronic\Mechatronic.eox
    <EEC-Installationsordner>\install\Tutorial\ProPanel\ProPanel_Ui.eox

     * The model contains T_Mechatronic_Architecture and T_Mechatronic_ModularSystem, but not T_ProPanel_Ui. Import this EOX file:
    
        <EEC-Installationsordner>\install\Tutorial\ProPanel\ProPanel_Ui.eox

     * The model contains T_ProPanel_Ui , but not T_Mechatronic_Architecture and T_Mechatronic_ModularSystem. Import this EOX file:
    
        <EEC-Installationsordner>\install\Tutorial\Mechatronic\Mechatronic.eox

Read more
     * [Importing libraries/projects as an EOX file](eecbase_k_eox_exchange_library_import.htm)
[Importing Pro Panel libraries into T_Mechatronic_ModularSystem](javascript:void\(0\);) To add the functions for the Pro Panel discipline to the T_Mechatronic_ModularSystem model, you will need to import the T_ProPanel_Ui library.
    1. Double-click to open the T_Mechatronic_ModularSystem library.
    2. Select the Imported libraries editor.
    3. Click .
The library finder now appears:
    1. Click [Search].
    2. Select the T_ProPanel_Ui library.
    3. Confirm with [OK].
    4. The following screenshot illustrates the dependencies of the imported libraries:
[Set settings in EEC](javascript:void\(0\);) The enclosure is created using IEC_bas001.zw9, the default macro-project template delivered with Eplan Pro Panel.
    1. Select Window > Settings.
    1. Select Disciplines > ECAD > Eplan Electric P8.
    2. In the Macro project template field, enter the path for the file IEC_bas001.zw9.
Eplan Electric P8 is launched by EEC to create the enclosure. For this purpose, the path for the executable file W3u.exe must be made known to EEC:
    1. In the Eplan Electric P8 executable field, enter the path for the file W3u.exe.
The field is already pre-filled with a path, but that path may be different from the one in the version that you use.
    1. Confirm with [OK].
If a different path is shown, you must do a restart after confirming. Note The versions of EEC and Eplan Pro Panel have to have the same version! The minimum required version is 2.3.5 HF2.
