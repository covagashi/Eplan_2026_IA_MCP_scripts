---
title: "Preparatory steps in EplanÂ ElectricÂ P8"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_preparation_steps_p8.htm"
file: "tutp8_h_preparation_steps_p8"
category: "tutp8"
---

# Preparatory steps in EplanÂ ElectricÂ P8

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Preparatory steps in Eplan Electric P8 To prepare the creation of macros, copies of the compressed project file Tutorial_P8.zw1 are created and variously re-saved. The first copy (Template_Project.elk) is saved as an empty template. When generating the structure, the macros of the page and sensors are inserted in this file. The second copy (Macro_Project.elk) is saved as a macro project. This is used to create the macros for the page and the sensors: Create path for macros:
    1. Start Eplan Electric P8.
    2. Select the following commands: File > Settings.
    3. Navigate to User > Management > Directories.
    4. Specify the <EEC installation folder>\resources\ECAD\Tutorial\P8 folder for the Templates.
    5. Specify the <EEC installation folder>\resources\ECAD\Tutorial\P8 folder for the Macros.
Enter the folder where EEC is installed instead of EEC installation Folder. The Eplan Electric P8 projects are stored in the default folder.
    6. Confirm with [OK].
Restoring the project Tutorial_P8.zw1:
    1. Select the following commands: File > Open > Browse.
    2. In the Open project dialog navigate to the following file:
    
        <EEC installation folder>\install\Tutorial\P8\Tutorial_P8.zw1

    1. Click [Open].
    2. The Restore project dialog opens.
    3. The file Tutorial_P8.zw1 is entered into the field Projects .
    4. Enter into the field Project name the text Feeder.
    5. Confirm with [OK].
    6. The Backstage view is closed, and the project is opened in the page navigator.
Create the first copy of the Feeder project:
    1. Select the Feeder project.
    2. Select the following commands: File > Copy.
    3. The Copy project dialog opens.
    4. Select the Only header data option.
    5. In the Target project field, enter the file name:
    
        Template_Project.elk

    1. Confirm with [OK].
    2. The Restore project dialog closes and the project in the page navigator opens.
Back up the Template_Project project:
    1. Select the Template_Project project.
    2. Select the following commands: File > Back up.
    3. The Back up projects dialog opens.
    4. Select in the field Backup directory:
    
        <EEC installation folder>\resources\ECAD\Tutorial\P8

This directory should correspond to the path variable $(MD_MACROS).
    1. Confirm with [OK].
    2. The Back up projects dialog closes.
Create another copy of the Feeder project:
    1. Select the Feeder project.
    2. Select the following commands: File > Copy.
    3. The Copy project dialog opens.
    4. If necessary, highlight the Entirely incl. report option.
    5. In the Target project field, enter the file name:
    
        Macro_Project.elk

    1. Confirm with [OK].
    2. The Copy project dialog closes and the project in the page navigator opens.
Change the settings of the Macro_Project project:
    1. Highlight the Macro_Project project.
    2. Select the File command.
    3. The Backstage view Project properties with the Properties tab opens.
    4. For the Type of project in the Value column, select Macro project.
    5. Close the Backstage view.
Create the macro template as the basic project:
    1. Highlight the Macro_Project project.
    2. Select the following commands: File > Extras > Command group Back up > Create basic project.
    3. The Create basic project dialog opens.
    4. Navigate to the following folder: <EEC installation folder>\resources\ECAD\Tutorial\P8.
    5. Enter Macro_Template.zw9 in the File name field.
    6. Confirm with [OK].
    7. The Create basic project dialog closes and the basic project is saved.
The projects Feeder and Template_Project close:
    1. Select the Feeder and Template_Project projects.
    2. In the popup menu select: Project > Close.
    3. Only the Macro_Project project is still available in the page navigator.
This completes all preparatory work.
