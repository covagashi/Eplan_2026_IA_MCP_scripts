# GraphicPage(String,String,String,Format,Int32,Int32,Compression,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1336.html

---

Exports a page of a project as image file. [Eplan.EplApi.DataModel.Page.PageType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PageType.html) of page can not be [Eplan.EplApi.DataModel.DocumentTypeManager.DocumentType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DocumentTypeManager+DocumentType.html)

Syntax

**C#**



public void GraphicPage( 

   string strFullLinkFileName,

   string strPageName,

   string strImagePath,

   Export.Format imageFormat,

   int iColorDepth,

   int iWidth,

   Export.Compression imageCompression,

   bool bBlackAndWhite

)

public:

void GraphicPage( 

   String^ strFullLinkFileName,

   String^ strPageName,

   String^ strImagePath,

   Export.Format imageFormat,

   int iColorDepth,

   int iWidth,

   Export.Compression imageCompression,

   bool bBlackAndWhite

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project, which contains the page to export.

*strPageName*
:   Name of the page to be exported.

*strImagePath*
:   Directory to which the image files will be written. If the folder does not exist, it will be created. If the user does not have the necessary rights to access the file system, an exception will be thrown.

*imageFormat*
:   Image format\: Supported export formats are\:

    \* BMP: available color depth: 1, 4, 8, 16, 24 and 32 \* TIF: available color depth: 1, 4, 8, 24 and 32 \* GIF: color depth is irrelevant \* PNG: available color depth: 1, 4, 8, 16, 24 and 32 \* JPG: available color depth: 1, 4, 8, 16, 24 and 32. The enum IMAGE\_FORMAT defines the necessary values. If an invalid format is set, the page will be exported as Tiff.

*iColorDepth*
:   Color depth of the image\: Allowed values are 1, 4, 8, 16, 24, and 32. If an invalid value is set, a color depth of 24 bit us used.

*iWidth*
:   Width of the image in pixels.The height is calculated automatically to keep the aspect ratio of the page.

*imageCompression*
:   Sets the image compression for the Tiff export. This parameter has no influence on other export formats. For the compression according\: CCITT3, CCITT4, and RLE the color depth always is 1, i.e. a binary image is created.

*bBlackAndWhite*
:   If set to true b/w images will be created. This does not influence the image format or the image size.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid arguments. |
| **UnauthorizedAccessException** | No user rights to create files on the \file system. |
| **ApplicationException** | The internal interface for image export could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Errors occurred during export. See the exception message for details. |
| **ArgumentException** | Thrown when one of the arguments passed to the method was not valid. |
| **OutOfMemoryException** | Thrown when the operating system is out of memory and could not allocate memory to process the method call. For an explanation of how constructors use the OutOfMemory status, see the Remarks section at the end of this topic. |
| **MemberAccessException** | Thrown when one of the arguments specified in the application programming interface (API) call is already in use in another thread. |
|  | Thrown when a buffer specified as an argument in the API call is not large enough to hold the data to be received. |
| **NotSupportedException** | Thrown when the method is not implemented. |
|  | Thrown when the object is in an invalid state to satisfy the API call. For example, calling Pen::GetColor from a pen that is not a single, solid color results in a WrongState status. |
| **UnauthorizedAccessException** | Thrown when a write operation is not allowed on the specified file. |
| **NotSupportedException** | Thrown when the specified image file format is not known. |
| **NotImplementedException** | Thrown when the method is not implemented. |
| **ArgumentException** | Thrown when the object is in an invalid state to satisfy the API call. For example, calling Pen::GetColor from a pen that is not a single, solid color results in a WrongState status. |
| [Eplan.EplApi.HEServices.Exceptions.HEServicesBase](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Exceptions.HEServicesBase.html) | Thrown in other cases when error hasn't own exception class or it's unspecified. Please refer to message content. |

Remarks

The project "strFullLinkFileName" may be open in EPLAN or not. If the project was not already open, it will be opened and after the export it will be closed again. This function uses GDI+ library which is also used by .NET. See [System.Drawing.Image](#)
