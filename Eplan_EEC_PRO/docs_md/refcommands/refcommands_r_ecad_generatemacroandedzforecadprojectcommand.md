---
title: "ECAD.GenerateMacroAndEdzForEcadProjectCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_ecad_generatemacroandedzforecadprojectcommand.htm"
file: "refcommands_r_ecad_generatemacroandedzforecadprojectcommand"
category: "refcommands"
---

# ECAD.GenerateMacroAndEdzForEcadProjectCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  ECAD.GenerateMacroAndEdzForEcadProjectCommand By using the command data are packed into an EDZ file whose contents represent a part for the P8 parts database. To this purpose a macro is created and packed together with further information and files into an EDZ file. [Requirements](javascript:void\(0\);)  
     * Eplan Electric P8 Version 2.6 and above.
     * The basic project template IEC_bas001.zw9is available in the current P8 version.
     * The enveloping macro has a placeholder object with special properties (see Variable_Placeholder_Object).
     * The executable file for Eplan Electric P8 (W3u.exe) is entered in the EEC settings.
     * Either the option Keep macro boxes in window macros or Keep macro boxes in symbol macros is activated in the EEC settings. In the case of the generation of an EDZ file these options are mutually exclusive! For information on creating macros see [Eplan Electric P8](admin_r_prefs_ecad_p8.htm).
     * The current configuration already contains a valid ECAD structure.
     * The specified C# script contains an EcExportMacroAction in order to create a macro and an EcCleanProjectAction in order to remove the temporarily created projects.
Note for use with Web EEC Server Generated EDZ files can be downloaded with the command Engineering.OpenResourceCommand. Note that the file is located in the project folder of the EEC Workspace. The project folder already contains the session ID. Files outside the project folder cannot be downloaded! When using this command, ensure that a relative path is always specified for the targetFolderName argument. If instead an absolute path is to be specified that does not point to the project folder, the EDZ file must still be copied into the project folder after the generation by means of the Engineering.CopyFileCommand command. The following parameters / model variables are important: Name | Type | Installed in | Standard | Meaning  
---|---|---|---|---  
Disciplines > ECAD > Eplan Electric P8 > **Parameter Name For C# Script** | String | WiringDiagram | Script | Stores the path to the C# script.  
Disciplines > ECAD > Eplan Electric P8 > **Parameter Name For C# Script Arguments** | String | WiringDiagram | ScriptArguments | Stores arguments that are passed to the C# script.  
Disciplines > ECAD > Eplan Electric P8 > Eplan Data Zip (.edz) generation > **Macro Project Template** | String |  | IEC_bas001.zw9 | Basic project template for creating the EDZ data.  
Disciplines > ECAD > Eplan Electric P8 > Eplan Data Zip (.edz) generation > **Parameter Name For Picture Path** | Map | Page | Image path | Stores the source and target paths of the images. The path is specified either absolutely or relatively to the P8 directory for images. While the EDZ file is being imported into P8 the image is stored in a directory that is made up of the P8 directory for images and the relative path. The paths are specified in a map with the syntax =Map{Pair{"src","<source folder>"},Pair{"dest","<destination folder>"}}.  
Disciplines > ECAD > Eplan Electric P8 > Eplan Data Zip (.edz) generation > **Parameter Name For Part Attributes** | Map | Page | Part attributes | The part attributes are specified with the syntax =Map{Pair{"<Attribute name1>","<Value>"},Pair{"<Attribute name2>","<Value>"}}. At least one of these part attributes has to be specified: 
     * P_ARTICLE_PARTTYPE
     * P_ARTICLE_GROUPSYMBOLMACRO
     * P_ARTICLE_PARTNR
     * P_ARTICLE_TYPENR
     * P_ARTICLE_VARIANT  
Disciplines > ECAD > Eplan Electric P8 > Eplan Data Zip (.edz) generation > **Parameter Name For Macro Path** | String | Page | Macro name | Stores the relative path to the macro that is created.  
The following method creates an EDZ file from a schematic page that contains a macro already created. If the schematic contains more than page, an error message is output. The name of the created EDZ file is returned. Argument | Type | Description  
---|---|---  
wiringDiagram | WiringDiagam | Project component of the WiringDiagram type whose subcomponents are collected.  
targetFolderName | String | Name of the target directory, where the created EDZ file is stored. The EDZ file is stored with the specified part number as the file name.  
When a relative path is specified, the created EDZ file is stored in the project directory.  
Alternatively an absolute path can be specified.  
  
The following method creates an EDZ file from a schematic page that contains a macro already created. If the schematic contains more than page, an error message is output. The name of the created EDZ file is returned. Argument | Type | Description  
---|---|---  
root | Root | Project component, subcomponents of the WiringDiagram type thereof are collected.  
targetFolderName | String | Name of the target directory, where the created EDZ file is stored. The EDZ file is stored with the specified part number as the file name.  
When a relative path is specified, the created EDZ file is stored in the project directory.  
Alternatively an absolute path can be specified.  
  
[Example for a placeholder object in Eplan Electric P8](javascript:void\(0\);) The following table lists examples of the required variables of a placeholder object for the generation of an EDZ file: Property | Current value | Variable  
---|---|---  
Macro box > <Macro name> > Macro:Name > Macro:Name[1] | <Name of the macro box> | <Macro name>  
Free text > <MacroVariant> > Text contents | <MacroVariant> | <MacroVariant>  
Free text > <MacroRepresentationType> > Text contents | <MacroRepresentationType> | <MacroRepresentationType>  
Free text > <MacroInsertPointActive> > Text contents | <MacroInsertPoint> | <MacroInsertPoint>  
Properties of the placeholder object in Eplan Electric P8: Read more
     * [XML export / import: Tags and their attributes](../../../../plattform/2025/Content/htm/xmlexport_o_tags.htm)
