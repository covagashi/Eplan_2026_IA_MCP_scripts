# exportToGraphics

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/exportToGraphics.html

---

```
Action to export pages and projects to graphical (TIF, GIF, PNG, JPG) format.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of task to be performed:
 '¢ "GRAPHICPROJECT": Export project in graphical format (TIF, GIF, PNG, JPG).
 '¢ "GRAPHICPAGE":Export pages in graphical format (TIF, GIF, PNG, JPG)
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` PAGENAME
 ``` | ``` Name of the page to be exported (optional). This parameter is only effective  with the GRAPHICPAGE value of the TYPE parameter.
 ``` |
| ``` EXPORTSCHEME
 ``` | ``` Scheme for graphical export (optional). Provides default values for other optional parameters.
 If this parameter does not exist or is empty, the most recently used graphical export  scheme is taken.
 ``` |
| ``` DESTINATIONPATH
 ``` | ``` Target directory where the graphical files are stored. If this directory does not exist yet, it is created. 
 In case of project export, below this directory, a new directory with the name of the project is created into which the individual image files are saved.
 ``` |
| ``` FORMAT
 ``` | ``` Output format. Supported export formats are:
 '¢ BMP: available color depth: 1, 4, 8, 16, 24 and 32
 '¢ TIF: available color depth: 1, 4, 8, 24 and 32
 '¢ GIF: color depth is irrelevant
 '¢ PNG: available color depth: 1, 4, 8, 16, 24 and 32
 '¢ JPG: available color depth: 1, 4, 8, 16, 24 and 32.
 This parameter is optional. If not specified, a default value is taken from the scheme settings.
 ``` |
| ``` COLORDEPTH
 ``` | ``` Color depth of the image.The possible values are 1, 8, 16, 24, 32.
 This parameter is optional. If not specified, a default value is taken from the scheme settings.
 ``` |
| ``` IMAGEWIDTH
 ``` | ``` Image width in pixels. The height is automatically  computed from the page dimensions. 
 This parameter is optional. If not specified, a default value is taken from the scheme settings.
 ``` |
| ``` IMAGECOMPRESSION
 ``` | ``` Type of compression for the output in Tiff format.
 Possible values are LZW, RLE, CCITT3, CCITT4, NONE.
 This parameter has no effect on other output formats. 
 The color depth is always 1 for CCITT3, CCITT4, and RLE compression, that is, a binary image is created.
 This parameter is optional. If not specified, a default value is taken from the scheme settings.
 ``` |
| ``` BLACKWHITE
 ``` | ``` The output is in black and white. Note: This does not affect the image format or size. 
 This parameter is optional.
 Default value: 1 (black/white)
 ``` |
| ``` USEPAGEFILTER
 ``` | ``` Determines if only filtered pages should be used or all project pages (optional). 
 It corresponds to the "Active" check box in GUI page navigator.
 Default value: 0.
 ``` |

**Remarks**

```
If a page was explicitly entered by the PAGENAME parameter, only this page is exported and the USEPAGEFILTER parameter is ignored. 

If no specific page was entered by the PAGENAME parameter and USEPAGEFILTER is set to 1, only pages filtered in GUI page navigator will be exported.

When an error occurs during an export operation, a "BaseException" is thrown.

```

**Example**

```
Export a project 

exportToGraphics /TYPE:GRAPHICPROJECT /PROJECTNAME:C:\\Projects\\EPLAN\\EPLAN_Sample_Project.elk /DESTINATIONPATH:C:\\temp  /FORMAT:BMP /COLORDEPTH:24 /IMAGEWIDTH:1024 /BLACKWHITE:1

Export a page 

exportToGraphics /TYPE:GRAPHICPAGE /PROJECTNAME:C:\\Projects\\EPLAN\\EPLAN_Sample_Project.elk /PAGENAME:=AP1+ST1/2 /DESTINATIONPATH:C:\\temp /FORMAT:BMP /COLORDEPTH:24 /IMAGEWIDTH:1024 /BLACKWHITE:1

Export several pages 

exportToGraphics /TYPE:GRAPHICPAGE /PROJECTNAME:C:\\Projects\\EPLAN\\EPLAN_Sample_Project.elk /DESTINATIONPATH:C:\\temp /FORMAT:BMP /COLORDEPTH:24 /IMAGEWIDTH:1024 /BLACKWHITE:1 /USEPAGEFILTER:1

Export a page with a 'scheme' parameter

exportToGraphics /TYPE:GRAPHICPAGE /PROJECTNAME:C:\\Projects\\EPLAN\\EPLAN_Sample_Project.elk /PAGENAME:=AP1+ST1/2 /EXPORTSCHEME:Bitmap

```