# export

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/export.html

---

```
Action to export pages and projects in graphical, DXF, DWG, PXF format.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ```  Type of task to be performed by the action:
 '¢ "PXFPROJECT": Export project in EPJ format.
 '¢ "GRAPHICPROJECT": Export project in graphical format (TIF, GIF, PNG, JPG).
 '¢ "GRAPHICPAGE": Export pages in graphical format (TIF, GIF, PNG, JPG).
 '¢ "DXFPROJECT": Export project in DXF format.
 '¢ "DWGPROJECT": Export project in DWG format.
 '¢ "DXFPAGE": Export page(s) in DXF format.
 '¢ "DWGPAGE": Export page(s) in DWG format.
 '¢ "PDFPAGESSCHEME": Export pages in PDF format. Used together with PAGENAMEn parameters (e.g. /PAGENAME1:=AP+ST1/2 /PAGENAME2:=AP+ST1/4 /PAGENAME3:=AP+ST1/7 etc.) or SELn parameters (e.g. /SEL1:38/4/12/0 (result from StorableObject.ToStringIdentifier())). 
 '¢ "PDFPROJECTSCHEME": Export project in PDF format.
 '¢ "DXFDWGPROJECTSCHEME": Export a project in DXF or DWG format. All settings are read from scheme, also the DXF or DWG format.
 '¢ "DXFDWGPPAGESSCHEME": Export pages in DXF or DWG format. All settings are read from scheme, also the DXF or DWG format.
 Used together with PAGENAMEn parameters (e.g. /PAGENAME1:=AP+ST1/2 /PAGENAME2:=AP+ST1/4 /PAGENAME3:=AP+ST1/7 etc.) or SELn parameters (e.g. /SEL1:38/4/12/0 (result from StorableObject.ToStringIdentifier())).
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` EXPORTFILE
 ``` | ``` If the value of the TYPE parameter is "PXFPROJECT", then this parameter contains the name of the project to be exported (optional). 
 Default value = Project name.
 If the TYPE parameter is set to "PDFPROJECTSCHEME" or "PDFPAGESSCHEME" then this parameter contains the name of the export file (required, full path name).
 The file extension is automatically added by the system.
 ``` |
| ``` EXPORTMASTERDATA
 ``` | ``` Specifies whether master data is to be included in the export (optional, 0 = No, 1 = Yes).
 Default value = 1. This parameter is only effective with the following value of the TYPE parameter: "PXFPROJECT".
 ``` |
| ``` EXPORTCONNECTIONS
 ``` | ``` Specifies whether connections are to be included in the export (optional, 0 = No, 1 = Yes). 
 Default value = 0. This parameter is only effective with the following value of the TYPE parameter: "PXFPROJECT".
 ``` |
| ``` PAGENAME
 ``` | ```  Name of the page to be exported (optional). 
 This parameter is only effective with the "DXFPAGE", "DXFPROJECT", "DWGPAGE", "DWGPROJECT", "GRAPHICPAGE", "GRAPHICPROJECT" values of the TYPE parameter.
 ``` |
| ``` PAGENAMEn
 ``` | ``` Names of the pages to be exported (optional), where n is a number (e.g. /PAGENAME1:=AP+ST1/2 /PAGENAME2:=AP+ST1/4 /PAGENAME3:=AP+ST1/7 etc.). 
 These parameters are only effective with the "DXFPAGE", "DWGPAGE", "PDFPAGESSCHEME" values of the TYPE parameter.
 ``` |
| ``` DESTINATIONPATH
 ``` | ``` Target directory (optional). Relevance of this parameter.
 For "GRAPHICPAGE", "GRAPHICPROJECT": Directory where the graphical files are stored. If this directory does not exist yet, it is created. 
 Below this directory, a new directory with the name of the project is created into which the individual image files are saved.
 For "DXFPAGE", "DXFPROJECT", "DWGPAGE", "DWGPROJECT", Directory to which the data is exported. 
 Default value = project directory.
 For all other exports except DXFDWGPPAGESSCHEME and DXFDWGPROJECTSCHEME,if used with parameter "PAGENAMEn", it is ignored and directory is taken from scheme.
 ``` |
| ``` FORMAT
 ``` | ``` Output format (optional). Supported export formats are:
 '¢ "BMP": available color depth: 1, 4, 8, 16, 24 and 32
 '¢ "TIF": available color depth: 1, 4, 8, 24 and 32
 '¢ "GIF": color depth is irrelevant
 '¢ "PNG": available color depth: 1, 4, 8, 16, 24 and 32
 '¢ "JPG": available color depth: 1, 4, 8, 16, 24 and 32.
 Default value = "TIF". This parameter is only effective with the "GRAPHICPAGE" and "GRAPHICPROJECT" values of the TYPE parameter.
 ``` |
| ``` COLORDEPTH
 ``` | ``` Color depth of the image (optional, default value = 24).
 The possible values are 1, 8, 16, 24, 32. 
 This parameter is only effective with the "GRAPHICPAGE" and "GRAPHICPROJECT" values of the TYPE parameter.
 ``` |
| ``` IMAGEWIDTH
 ``` | ``` Image width in pixels (optional, default value = 80). 
 The height is automatically computed from the page dimensions.
 This parameter is only effective with the "GRAPHICPAGE" and "GRAPHICPROJECT" values of then TYPE parameter.
 ``` |
| ``` IMAGECOMPRESSION
 ``` | ``` Type of compression for output in TIF format (optional).
 This parameter has no effect on other output formats. The color depth is always 1 for CCITT3, CCITT4, and RLE compression, that is, a binary image is created.
 The possible values are LZW, RLE, CCITT3, CCITT4, NONE. Default value = NONE. 
 This parameter is only effective with the "GRAPHICPAGE" and "GRAPHICPROJECT" values of the TYPE parameter.
 ``` |
| ``` BLACKWHITE
 ``` | ``` Sets the color scheme for the output if the TYPE parameter has the value GRAPHICPAGE or GRAPHICPROJECT (optional, 0 = color, 1 = black and white).
 Default value : 1
 Note: This does not affect the image format or size, i.e. the files are not reduced. 
 It is only effective with the "GRAPHICPAGE" and "GRAPHICPROJECT" values of the TYPE parameter.
 This is also used for "PDFPROJECTSCHEME" and "PDFPAGESSCHEME" whereby 
 '¢ 0 = Color,
 '¢ 1 = Black and White, 
 '¢ 2 = Grayscale and
 '¢ 3 = White Inverted (output will be in Black and White; additionally white (Number: 8, 255, 263, 264, 266) graphical elements are inverted or changed to Black)
 ``` |
| ``` USEPAGEFILTER
 ``` | ``` Determines if only filtered pages should be used or all project pages (optional). 
 It corresponds to "Active" check box in GUI. 
 This parameter is only effective with the "GRAPHICPAGE" value of the TYPE parameter when PAGENAME or PAGENAMEn parameter is not used.
 Default value = 0 
 ``` |
| ``` EXPORTSCHEME
 ``` | ``` Scheme for DXF/DWG export (optional).
 This parameter can be the users defined DXF/DWG export scheme settings (myScheme) or the default scheme settings of EPLAN (Standard Settings).  
 If this parameter does not exist or is empty (""), the most recently used DXF/DWG export scheme is taken.
 This parameter supports only the following values of the TYPE parameter:
 "DXFPAGE", "DXFPROJECT", "DWGPAGE", "DWGPROJECT", "PDFPROJECTSCHEME", and "PDFPAGESSCHEME".
 ``` |
| ``` USEZOOM
 ``` | ``` If set to 1, a zoom window is to be used when jumping from navigation pages to components in the PDF file.
 The components are then displayed centered within the zoom window.
 ``` |
| ``` ZOOMLEVEL
 ``` | ``` If USEZOOM is set to 1, you set in ZOOMLEVEL the desired zoom level in "mm".
 The value entered reflects the height of the screen section that is to be displayed magnified after the jump. 
 A smaller value (e.g. 20 mm) thus leads to a greatly magnified display of the respective component on the screen. 
 You can enter values between 1 and 3500.
 If USEZOOM is 0, ZOOMLEVEL has no influence on the result.
 ``` |
| ``` USESIMPLELINK
 ``` | ``` If set to 1, only a simple link is created in the PDF.
 If set to 0 then "three-way" jumps are available for all components in the PDF.
 ``` |
| ``` FASTWEBVIEW
 ``` | ``` If set to 1, fast web display will be enabled in the PDF. 
 ``` |
| ``` READONLYEXPORT
 ``` | ``` If set to 1, the PDF file will be write protected.
 ``` |
| ``` USEPRINTMARGINS
 ``` | ``` If set to 1, print margins will be used during PDF export ignoring the setting in scheme (optional).
 If not passed, setting from scheme will be applied. 
 This parameter is only effective with the "PDFPAGESSCHEME" and "PDFPROJECTSCHEME" values of the TYPE parameter.
 ``` |
| ``` TARGET
 ``` | ``` Specifies whether the target is disk or from Settings. 
 It may have the following values: "Disk", "FromSettings" (case insensitive).
 If value is "FromSettings", the target for the export (also the target directory) is specified by the settings (scheme).
 If value is "Disk", the target directory is specified by the DESTINATIONPATH parameter.
 (Note: If not specified, the target is disk. This option shouldn't be used; preserved for compatibility reasons only.)
 This parameter is only effective with the following values of the TYPE parameter: "DXFDWGPPAGESSCHEME", "DXFDWGPROJECTSCHEME", "DXFPROJECT", "DXFPAGE", "DWGPROJECT", "DWGPAGE".
 When exporting "DXFPAGE" or "DWGPAGE" with PAGENAMEn parameter, TARGET is automatically set to "FromSettings".
 ``` |
| ``` LANGUAGE
 ``` | ``` Language identifier. Specifies the language to translate the project into before the export.
 Note: This parameter is case-sensitive. Correct language specifiers are: "en_US", "de_DE", etc.
 This parameter is only effective with the following values of the TYPE parameter:
 "DXFPROJECT", "DXFPAGE", "DWGPROJECT", "DWGPAGE", "PDFPROJECTSCHEME" and "PDFPAGESSCHEME".
 ``` |
| ``` EXPORTMODEL
 ``` | ``` This is a boolean parameter.  
 If true then any 3D models in the project will be exported along with the desired pages.  
 Note that there are also settings in the scheme that control which models will be exported.
 This parameter is only effective with the following values of the TYPE parameter: "PDFPROJECTSCHEME" and "PDFPAGESSCHEME". 
 ``` |

**Remarks**

```
The following functions are supported:

'¢ Export project in PXF format

'¢ Export project and pages in graphical format (TIF, GIF, PNG, JPG)

'¢ Export project and pages in DXF / DWG format


  '¢ In case of EPJ project export (TYPE: "PXFPROJECT"), it is done with master data and without connections by default. So EXPORTMASTERDATA has "TRUE" value and EXPORTCONNECTIONS is "FALSE" by default.

  '¢ If a page was explicitly entered by the PAGENAME parameter, only this page is exported and the USEPAGEFILTER parameter is ignored.

  '¢ If no specific page was entered by the PAGENAME parameter, project pages are determined. If USEPAGEFILTER is set to 1, only pages filtered in GUI page navigator will be exported. If USEPAGEFILTER is not used or if it is set to 0, all project pages will be exported.

  '¢ USEPAGEFILTER corresponds to "Active" check box in the page navigator.

  '¢ In case of "DXFPAGE", "DXFPROJECT", "DWGPAGE", and "DWGPROJECT" export, if TARGET parameter is not specified, the output target is taken form the settings and the DESTINATIONPATH parameter is ignored.

  '¢ In case of DXF/DWG and PDF exports this action internally calls the "ExportDataExchange" action with the following sets of parameters:

                Action = 'RequestClearTargetDir', Target, ClearTargetDir

    and 

                Action = 'FileFinished', FullFileName, TargetDir, SubDir, FileName

  '¢ When an error occurs during an export operation, a "BaseException" is thrown.

```

**Example**

```
Export a project in EPJ format

export /TYPE:PXFPROJECT /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /EXPORTFILE:C:\temp\myPxf_Sample_Project

Export a project in graphical format

export /TYPE:GRAPHICPROJECT /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /DESTINATIONPATH:C:\temp  /FORMAT:BMP /COLORDEPTH:24 /IMAGEWIDTH:1024 /BLACKWHITE:1

Export a page in graphical format

export /TYPE:GRAPHICPAGE /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /PAGENAME:=AP1+ST1/2 /DESTINATIONPATH:C:\temp /FORMAT:BMP /COLORDEPTH:24 /IMAGEWIDTH:1024 /BLACKWHITE:1

Export a project in pdf format

export /TYPE:PDFPROJECTSCHEME /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /EXPORTFILE:C:\EPLAN_Sample_Project.pdf /EXPORTSCHEME:myScheme

Export several pages in graphical format

export /TYPE:GRAPHICPAGE /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /DESTINATIONPATH:C:\temp /FORMAT:BMP /COLORDEPTH:24 /IMAGEWIDTH:1024 /BLACKWHITE:1 /USEPAGEFILTER:1

Export a project in DXF/DWG format

export /TYPE:DXFPROJECT /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /DESTINATIONPATH:C:\temp

Export a page in DXF/DWG format

export /TYPE:DXFPAGE /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /PAGENAME:=AP1+ST1/2 /DESTINATIONPATH:C:\temp

Export several pages in DXF/DWG format

export /TYPE:DXFPAGE /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /DESTINATIONPATH:C:\temp /EXPORTSCHEME:dxf_scheme

Export several pages in DXF/DWG format. Output path is taken from scheme.

export /TYPE:DXFPAGE /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /PAGENAME1:=AP1+ST1/2 /PAGENAME2:=AP+ST1/4 /EXPORTSCHEME:"Standard Settings"

Export several pages in pdf format. For export a single page use "export /TYPE:PDFPAGE /PAGENAME:=AP+ST1/2"

export /TYPE:PDFPAGESSCHEME /EXPORTSCHEME:myScheme /PAGENAME1:=AP+ST1/2 /PAGENAME2:=AP+ST1/4 /PAGENAME3:=AP+ST1/7 /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /EXPORTFILE:C:\EPLAN_Sample_Project.pdf

```