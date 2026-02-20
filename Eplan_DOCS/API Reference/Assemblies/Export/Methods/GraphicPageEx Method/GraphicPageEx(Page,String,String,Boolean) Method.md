# GraphicPageEx(Page,String,String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export~GraphicPageEx(Page,String,String,Boolean).html

---

Exports a page of a project as image file. [Eplan.EplApi.DataModel.Page.PageType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PageType.html) of page can not be [Eplan.EplApi.DataModel.DocumentTypeManager.DocumentType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DocumentTypeManager+DocumentType.html) Returns the name of the created file.

Syntax

**C#**



public string GraphicPageEx( 

   Page oPage,

   string strImageDir,

   string strSchemeName,

   bool bBlackAndWhite

)

public:

String^ GraphicPageEx( 

   Page^ oPage,

   String^ strImageDir,

   String^ strSchemeName,

   bool bBlackAndWhite

)


#### Parameters

*oPage*
:   Page to be exported.

*strImageDir*
:   Directory to which the image files will be written. If NULL or empty, a directory specified in the scheme will be used. If the folder does not exist, it will be created. If the user does not have the necessary rights to access the file system, an exception will be thrown.

*strSchemeName*
:   Name of the configuration scheme to use during the export.

*bBlackAndWhite*
:   If set to true b/w images will be created. This does not influence the image format or the image size.

#### Return Value

Name of the created file.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid arguments. |
| **UnauthorizedAccessException** | No user rights to create files on the \file system. |
| **ApplicationException** | The internal interface for image export could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Errors occurred during export. See the exception message for details. |
