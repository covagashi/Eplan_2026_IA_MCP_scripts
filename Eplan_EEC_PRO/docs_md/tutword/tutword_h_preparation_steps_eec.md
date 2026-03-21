---
title: "Preparatory steps in EEC"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutword_h_preparation_steps_eec.htm"
file: "tutword_h_preparation_steps_eec"
category: "tutword"
---

# Preparatory steps in EEC

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Preparatory steps in EEC The following steps are required to prepare the tutorial: [Import EOX files for Word tutorial](javascript:void\(0\);) Before the Word discipline can be edited, the T_Mechatronic_Architecture and T_Mechatronic_ModularSystem libraries created in the chapter [Mechatronic](tutmechatronic_h_mechatronic.htm) have to be available. If the T_Mechatronic_Architecture and T_Mechatronic_ModularSystem libraries are not available, please import the following EOX file:
    
        <EEC-Installationsordner>\install\Tutorial\Mechatronic\Mechatronic.eox.

Predefined SequenceSelectionActions used to generate and open the discipline structure, the code, and the PDF file can be found in this EOX file:
    
        <EEC-Installationsordner>\install\Tutorial\Word\Word_Ui.eox.

Read more
     * [Importing libraries/projects as an EOX file](eecbase_k_eox_exchange_library_import.htm)
[Customizing a model variable](javascript:void\(0\);) Various model variables can be customized for Word. Only the Name for Unit for Word Parameter model variable has to be changed in order to create a connection to the existing parameters when importing the Word resources and to ensure that parameters of the same name are not created in a new unit.
    1. Select Model > Model variables.
    2. Navigate to Disciplines > Office > Word.
    3. Select the value true for the model variable Create Parameters On Demand.
    4. Select the value true for the model variable Create Parameter Units On Demand.
[Importing libraries](javascript:void\(0\);) To use the Word function in the T_Mechatronic_ModularSystem library, it is necessary to import the Word system library. Likewise, the Word_Ui and Word_Customizing libraries must be imported to use predefined SequenceSelectionActions. In addition, the MediaSource library has to be imported. This will allow you to insert image objects into the Word file. Import the EOX file <EEC installation folder>\install\Tutorial\Word\Word_Ui.eox. Read more
     * [Importing libraries/projects as an EOX file](eecbase_k_eox_exchange_library_import.htm)
Subsequently the libraries Word_Customizing and Word_Ui are available in the library catalog.
    1. Double-click to open the T_Mechatronic_ModularSystem library.
    2. Select the Imported libraries editor.
    3. Click .
The library finder now appears.
    1. Click [Search].
    2. Select the Word_Ui and MediaSource libraries. The libraries Word und Word_Customizing are imported through dependencies on classes contained in it.
    3. Confirm with [OK].
    1. Save the changes.
In the following text, it is assumed that you save your modifications at the latest before opening the next object (diskette icon top left or by using the shortcut key [Ctrl] \+ [S]), and if not, when you see the prompt click [Yes].
