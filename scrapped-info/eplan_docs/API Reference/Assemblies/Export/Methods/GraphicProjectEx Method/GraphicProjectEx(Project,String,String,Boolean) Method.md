# GraphicProjectEx(Project,String,String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export~GraphicProjectEx(Project,String,String,Boolean).html

---

Exports a complete project as image files but instead of pages which [Eplan.EplApi.DataModel.Page.PageType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PageType.html) is [Eplan.EplApi.DataModel.DocumentTypeManager.DocumentType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DocumentTypeManager+DocumentType.html) Returns an array of strings containing names of the created files.

Syntax

**C#**



public string[] GraphicProjectEx( 

   Project oProject,

   string strImagePath,

   string strSchemeName,

   bool bBlackAndWhite

)

public:

array<String^>^ GraphicProjectEx( 

   Project^ oProject,

   String^ strImagePath,

   String^ strSchemeName,

   bool bBlackAndWhite

)


#### Parameters

*oProject*
:   Project to be exported.

*strImagePath*
:   Directory to which the image files will be written. If the folder does not exist, it will be created. If the user does not have the necessary rights to access the file system, an exception will be thrown. A sub\-folder named after the project will be created in which the images will be stored.

*strSchemeName*
:   Name of the configuration scheme to use during the export.

*bBlackAndWhite*
:   If set to true b/w images will be created. This does not influence the image format or the image size.

#### Return Value

An array of strings containing names of the created files.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid arguments. |
| **UnauthorizedAccessException** | No user rights to create files on the \file system. |
| **ApplicationException** | The internal interface for image export could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Errors occurred during export. See the exception message for details. |
