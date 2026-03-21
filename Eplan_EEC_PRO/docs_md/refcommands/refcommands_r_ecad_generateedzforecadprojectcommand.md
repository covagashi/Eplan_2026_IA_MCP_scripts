---
title: "ECAD.GenerateEdzForEcadProjectCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_ecad_generateedzforecadprojectcommand.htm"
file: "refcommands_r_ecad_generateedzforecadprojectcommand"
category: "refcommands"
---

# ECAD.GenerateEdzForEcadProjectCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  ECAD.GenerateEdzForEcadProjectCommand Generates an EDZ file of the specified project components of the WiringDiagram type. The name of the created EDZ file is returned. In addition the path to the C# script has to be specified in a parameter. The name of this parameters has to be specified in the model variable [Parameter name for the C# script arguments](admin_r_modelvar_p8scriptargs.htm). Note for use with Web EEC Server Generated EDZ files can be downloaded with the command Engineering.OpenResourceCommand. Note that the file is located in the project folder of the EEC Workspace. The project folder already contains the session ID. Files outside the project folder cannot be downloaded! When using this command, ensure that a relative path is always specified for the targetFolderName argument. If instead an absolute path is to be specified that does not point to the project folder, the EDZ file must still be copied into the project folder after the generation by means of the Engineering.CopyFileCommand command. Argument | Type | Description  
---|---|---  
root | Root | Project component, subcomponents of the WiringDiagram type thereof are collected.  
partXmlFilepath | String | File path to the parts description (part.xml).  
pictureFilepath | String | File path to the parts image.  
companyCode | String | Company name. The specification may not be empty or zero. Is used to form an internal path specification. May only contain characters that are allowed for Windows folder names.  
targetFolderName | String | Name of the target directory, where the created EDZ file is stored.  
If a name or a relative path is specified, the created EDZ file is stored in the project directory.  
An absolute name can be specified alternatively.  
  
The following method creates an EDZ file from which a macro is created during importing to P8. The required values for the file path to the part image (pictureFilePath), the file path to the part description (partXmlFilePath) and the company code (companyCode) have to be specified via parameters in the model. The names of the parameters have to be specified in the model variables (see [Eplan Data Zip (.edz) generation](admin_r_modelvar_eplandatazipgeneration.htm))! Argument | Type | Description  
---|---|---  
root | Root | Project component whose subcomponents of the WiringDiagram type are collected.  
targetFolderName | String | Name of the target directory, where the created EDZ file is stored.  
If a name or a relative path is specified, the created EDZ file is stored in the project directory.  
An absolute name can be specified alternatively.  
  
In the following method the file path to the part description can be entered as an absolute path. The specified absolute path is scanned for the occurrence of the subfolder \partxml. The directory structure below this folder is subsequently used as a relative path. Argument | Type | Description  
---|---|---  
wiringDiagram | WiringDiagram | ECAD component (e.g. page) in the ECAD-structure for which the schematic diagram should be created.  
partXmlFilepath | String | File path to the parts description (part.xml).  
pictureFilepath | String | File path to the parts image.  
companyCode | String | Company name. This specification may not be empty or zero. Is used to form an internal path specification. May only contain characters that are allowed for Windows folder names.  
targetFolderName | String | Name of the target directory, where the created EDZ file is stored.  
If a name or a relative path is specified, the created EDZ file is stored in the project directory.  
An absolute name can be specified alternatively.  
The following method creates an EDZ file from which a macro is created during importing to P8. The required values for the file path to the part image (pictureFilePath), the file path to the part description (partXmlFilePath) and the company code (companyCode) have to be specified via parameters in the model. The names of the parameters have to be specified in the model variables (see [Eplan Data Zip (.edz) generation](admin_r_modelvar_eplandatazipgeneration.htm))! Argument | Type | Description  
---|---|---  
wiringDiagram | WiringDiagram | ECAD component (e.g. page) in the ECAD-structure for which the schematic diagram should be created.  
targetFolderName | String | Name of the target directory, where the created EDZ file is stored.  
If a name or a relative path is specified, the created EDZ file is stored in the project directory.  
An absolute name can be specified alternatively.  
[Example for partXmlFilepath](javascript:void\(0\);) Path specification for partXmlFilepath:
    
        c:/temp/edz/data/partxml/myParts/part.xml

Resulting path specification:
    
        myParts/part.xml

The file path to the part image can be specified as an absolute path. The specified absolute path is scanned for the occurrence of the subfolder \picture. The directory structure below this folder is subsequently used as a relative path. [Example for pictureFilepath](javascript:void\(0\);) Path specification for pictureFilepath:
    
        c:/temp/edz/data/pictures/myPictures/part.jpg

Resulting path specification:
    
        myPictures/part.jpg

[Example in formula](javascript:void\(0\);)
    
        =type('ECAD.GenerateEdzForEcadProjetCommand').execute(mroot,
    	'c:\\parts\\descriptions\sensor001_part.xml',
    	'c:\\parts\\images\\sensor001.jpg','c:\\edz')

[Example in Form-UI](javascript:void\(0\);)
    
        <action name="ECAD.GenerateEdzForEcadProjetCommand"
    	arguments="=List{mroot,
    	'c:\\parts\\descriptions\sensor001_part.xml',
    	'c:\\parts\\images\\sensor001.jpg','c:\\edz'}"
    	type="link">Create EDZ file</action>

[Example in scripting](javascript:void\(0\);)
    
        import com.mind8.mechatronic.skill.eos.TypeClass;
    	TypeClass.findType(self.getUnitOfWork(),
    	"ECAD.GenerateEdzForEcadProjetCommand").perform
    	("execute",mroot,"c:\\parts\\descriptions\sensor001_part.xml",
    	"c:\\parts\\images\\sensor001.jpg","c:\\edz");
