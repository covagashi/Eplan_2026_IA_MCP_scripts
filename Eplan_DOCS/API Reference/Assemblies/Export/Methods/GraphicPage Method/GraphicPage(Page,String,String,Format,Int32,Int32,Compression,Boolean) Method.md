# GraphicPage(Page,String,String,Format,Int32,Int32,Compression,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1337.html

---

Exports a page of a project as image file. [Eplan.EplApi.DataModel.Page.PageType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PageType.html) of page can not be [Eplan.EplApi.DataModel.DocumentTypeManager.DocumentType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DocumentTypeManager+DocumentType.html)

Syntax

**C#**



public void GraphicPage( 

   Page oPage,

   string strImagePath,

   string strFileName,

   Export.Format imageFormat,

   int iColorDepth,

   int iWidth,

   Export.Compression imageCompression,

   bool bBlackAndWhite

)

public:

void GraphicPage( 

   Page^ oPage,

   String^ strImagePath,

   String^ strFileName,

   Export.Format imageFormat,

   int iColorDepth,

   int iWidth,

   Export.Compression imageCompression,

   bool bBlackAndWhite

)


#### Parameters

*oPage*
:   Page to be exported.

*strImagePath*
:   Directory to which the image file will be written. If the folder does not exist, it will be created. If the user does not have the necessary rights to access the file system, an exception will be thrown.

*strFileName*
:   Name of the output file. May be NULL or empty (the name of the page exported will be taken in such case). File name's extension is appended automatically according to the format specified.

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
