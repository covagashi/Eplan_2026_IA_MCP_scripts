---
title: "Engineering.ZipFileCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_engineering_zipfilecommand.htm"
file: "refcommands_r_engineering_zipfilecommand"
category: "refcommands"
---

# Engineering.ZipFileCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Engineering.ZipFileCommand Packs single files or a folder into a ZIP file. Argument | Type | Description  
---|---|---  
contextObject | Object | Only necessary, if a name of a relative paths is specified for targetName. Mechatronic component, root object or project to identify the project folder in the workspace. The created ZIP file is stored in the project directory.  
sourceFileOrFolderName | String | Name of the file or folder, which should be packed. The file or folder must be located in the workspace, otherwise an absolute name can be specified. If a folder is specified the folder itself and its complete content is involved (recursive). If a folder is specified with trailing backslash, only the complete content of the folder is involved (recursive).  
targetFileName | String | Name of the created ZIP file.  
If a name or a relative path is specified, the created ZIP file is stored in the project directory. Therefore the specification of contextObject is necessary.  
If an absolute path is specified, the specification of contextObject is not necessary. The file extension must not be defined.  
[Example in formula](javascript:void\(0\);) Variant with specification of contextObject:
    
        =type('Engineering.ZipFileCommand').execute(mroot,'c:\\temp\\Feeder.txt','Feeder.zip')

Variant without specification of contextObject:
    
        =type('Engineering.ZipFileCommand').execute(null,'c:\\temp\\Feeder.txt','c:\\temp\\Feeder.zip')

Variant without specification of contextObject without folder:
    
        =type('Engineering.ZipFileCommand').execute(null,'c:\\temp\\Feeder\\','c:\\temp\\Feeder.zip')

[Example in Form-UI](javascript:void\(0\);)
    
        <action name="Engineering.ZipFileCommand"
    	arguments="=List{mroot,'c:\\temp\\Feeder\\','Feeder.zip'}"
    	type="link">Create ZIP file</action>

[Example in scripting](javascript:void\(0\);)
    
        import com.mind8.mechatronic.skill.eos.TypeClass;
    TypeClass.findType(self.getUnitOfWork(),"Engineering.ZipFileCommand").perform
    ("execute",arg0,"Feeder","Feeder.zip");
