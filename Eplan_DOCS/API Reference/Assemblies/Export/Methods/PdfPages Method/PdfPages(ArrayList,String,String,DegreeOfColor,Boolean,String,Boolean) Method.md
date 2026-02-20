# PdfPages(ArrayList,String,String,DegreeOfColor,Boolean,String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1347.html

---

Exports pages of one project as PDF file.

Syntax

**C#**



public void PdfPages( 

   ArrayList arrayPages,

   string strSchema,

   string strPdfExportFileName,

   Export.DegreeOfColor color,

   bool bExportModel,

   string strLanguage,

   bool bUsePrintMargins

)

public:

void PdfPages( 

   ArrayList^ arrayPages,

   String^ strSchema,

   String^ strPdfExportFileName,

   Export.DegreeOfColor color,

   bool bExportModel,

   String^ strLanguage,

   bool bUsePrintMargins

)


#### Parameters

*arrayPages*
:   Array of Pages to be exported. ArrayList should contain only Pages of one project.

*strSchema*
:   The name of the settings scheme. If no name is given, the last used scheme will be used. The schemes are located in "USER.PDFExportGUI.SCHEMAS".

*strPdfExportFileName*
:   Name of the PDF \file to be generated. If left blank, the output file name will be determined by the settings in the scheme. If a path name is given, it will override the directory setting in the scheme. If the directory does not exist, it will be created. If the user does not have the necessary rights to access the file system, an exception will be thrown. If you set a \file name without the extension ".pfd", the extension will be added.

*color*
:   Determines the color setting of the PDF file. "BlackAndWhite" will make all elements including bitmaps black on a white background. "GreyLevel" will use shades of grey for every item. Color will use the full colors.

*bExportModel*
:   3D models will be exported as well as the pages. This requires a separate license for 3D.

*strLanguage*
:   Language or languages of exported pages. To set more than one language, use comma as separator (no blank spaces), e.g. "it\_IT,en\_US". If the "Alternative languages" option is set in the "PDF output languages" settings of the project, the alternative languages from the project settings are used for export.

*bUsePrintMargins*
:   Use print margins. Parameter overrides setting in scheme.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid arguments. |
| **ArgumentNullException** | Thrown if null was passed to a parameter |
| **ArgumentOutOfRangeException** | Thrown if an invalid value was passed to a parameter, e.g. dZoomLevel is out of range. |
| **UnauthorizedAccessException** | No user rights to create files on the \file system. |
| **ApplicationException** | The internal interface for image export could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Errors occurred during export or when project has no pages to export. See the exception message for details. |
| **InvalidScheme** | Thrown if an invalid scheme is given |
| **InvalidOperationException** | Thrown when `strLanguage` is not available in project translation. |
