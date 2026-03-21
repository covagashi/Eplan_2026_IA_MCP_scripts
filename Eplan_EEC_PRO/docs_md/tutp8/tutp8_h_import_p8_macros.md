---
title: "Import EplanÂ ElectricÂ P8 macros"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_import_p8_macros.htm"
file: "tutp8_h_import_p8_macros"
category: "tutp8"
---

# Import EplanÂ ElectricÂ P8 macros

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Import Eplan Electric P8 macros In the T_Mechatronic_ModularSystem library create the ECAD unit, and in it, the Schematic subunit: See [Creating units](eecbase_k_create_unit.htm). The unit structure should look like this: In the Schematic unit, insert a schematic component:
    1. Select the Schematic unit.
    2. Select New > ECAD > Schematic.
    3. Enter Schematic in the Name field.
    4. In the Resource location panel, click [Assign].
    5. Highlight the Template_Project.zw1 file.
    6. Confirm with [Open].
    7. In this process, the Parameter unit was created in addition. This includes the following parameters:
     * FunctionDesignation
     * LocationDesignation
     * ProjectSupplementaryFields
     * Report
     * Script
     * ScriptArguments
The names of the parameters can be set under Model > Model Variables. This way it is possible to define the structure identifiers in P8 in EEC. Launch the mass import of macros:
    1. Select the ECAD unit.
    2. Select Create Model from Resources from the popup menu.
    3. The Create Model from Resources wizard opens.
    4. Enter the path for the sources in the Source field:
    
        <EEC installation folder>\resources\Tutorial\P8

    1. Confirm via [Next >].
    2. In the next wizard window, the macro files are listed, among other things:
    3. Deactivate all objects that do not reference macros.
    4. For the /Page/page.ema macro, select the Page class.
    5. Apply the new class with [Set].
    6. Confirm with [Finish].
    7. Due to the mass import, the units Page and PLC_Inputs have been created, and they contain the macros. The parameters have been adopted from the macros, and inserted in the Parameters unit:
A parameter is still missing for the page numbering. In the ECAD.Parameter unit create the parameter PageNumber with the type String. Note In unit a point '.' is applied like a backslash '\' is applied in data directories. Specify an abstract page as super class.
    1. Select the Page unit.
    2. Select New > ECAD > Page.
    3. Enter abstractPage in the Name field.
    4. Select the Abstract check box.
    1. Open the Parameters editor page.
    2. Insert the parameters FunctionDesignation, LocationDesignation, PageDescription and PageNumber.
The parameters can be inserted easily in the editor via Drag & Drop. To do so, highlight the parameters and drag them to the editor. The parameters are then sorted exclusively in alphabetical order in the editor. The sequence can be changed via the arrows Move up and Move down. The Page page is to inherit the properties of the abstract page abstractPage (see [Creating discipline components](eecbase_k_create_discipline_component.htm)). Assign the abstractPage super class to the Page page:
    1. Open the Page page.
    2. In the Super class field, select the abstractPage class.
Check the number of parameters. The structure parameters of the abstractPage super class must be included as well as the parameters for the function texts and sockets of the macro file. Name | Standardized | Type | Declared in  
---|---|---|---  
FunctionDesignation | false | String | abstractPage  
Functiontext1 | false | String | Page  
Functiontext2 | false | String | Page  
Functiontext3 | false | String | Page  
Functiontext4 | false | String | Page  
Functiontext5 | false | String | Page  
Functiontext6 | false | String | Page  
Functiontext7 | false | String | Page  
Functiontext8 | false | String | Page  
Input1 | false | Socket | Page  
Input2 | false | Socket | Page  
Input3 | false | Socket | Page  
Input4 | false | Socket | Page  
Input5 | false | Socket | Page  
Input6 | false | Socket | Page  
Input7 | false | Socket | Page  
Input8 | false | Socket | Page  
LocationDesignation | false | String | abstractPage  
PageDescription | false | String | abstractPage  
PageNumber | false | String | abstractPage  
Check the parameters of the sensors. Each sensor has the DT parameter of the String type and IP of the Plug type
