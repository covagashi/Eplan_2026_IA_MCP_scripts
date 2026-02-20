# import

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/import.html

---

```
Action for importing projects, macros, and drawings.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of task to be performed by the action:
 '¢ "PXFPROJECT": Import PXF project
 '¢ "DXFDWGFILES": Insert DXF / DWG drawings in macros.
 '¢ "DXFPAGE": Insert DXF drawing into a page
 '¢ "DWGPAGE": Insert DWG drawing into a page
 '¢ "PDFCOMMENTS": Import PDF comments into project.
 There are some settings that need to be set before doing import. 
 For more information please see Eplan Electric P8 Help.
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path. Is required for the following values of the TYPE parameter: "PDFCOMMENTS".
 Is optional if the TYPE parameter has the following values: "PXFPROJECT", "DXFDWGFILES", "DXFPAGE" and "DWGPAGE". 
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar).
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` IMPORTFILE
 ``` | ``` Path and name.
 '¢ "PXFPROJECT": Path and name of the file to be imported. 
 '¢ "DXFPAGE", "DWGPAGE", "PDFCOMMENTS": Path and name of the file to be imported.
 ``` |
| ``` SOURCEPATH
 ``` | ``` Directory where the DXF/DWG files are located. Only applies to the "DXFDWGFILES" value of the TYPE parameter
 ``` |
| ``` DESTINATIONPATH
 ``` | ``` Destination directory where the imported projects and macros are stored. 
 Only applies to the "DXFDWGFILES" values of the TYPE parameter.
 If this value contains "EPLAN4\P" (e.q. "C:\EPLAN4\P\SOMEPROJECTDIR"), then such a directory (DESTINATIONPATH) will be created and project will be imported there. 
 If DESTINATIONPATH parameter doesn't contain "EPLAN4\P", then project will be imported and strDestinationPath will be treated as full project path. 
 Note that in such a case DESTINATIONPATH must contain P8 project file at end of path. (e.q. "C:\test\EPLAN_Sample_Project.elk").
 ``` |
| ``` IMPORTSCHEME
 ``` | ``` Name of the DXF/DWG import scheme (only name, without full path) (optional). Default value = Most recently used scheme. 
 If this parameter does not exist or is empty (""), the most recently used scheme is taken. 
 Only applies to the TYPE parameter values: "DXFPAGE", "DWGPAGE", "DXFDWGFILES"
 ``` |
| ``` PAGENAME
 ``` | ``` Name of page into which the CAD drawing is to be inserted. 
 Only applies to the "DXFPAGE" and "DWGPAGE" values of the TYPE parameter
 ``` |
| ``` XSCALE
 ``` | ``` Scaling in X direction. 
 Default value = 1. 
 Only applies to the DXFPAGE and DWGPAGE values of the TYPE parameter. (optional)
 ``` |
| ``` YSCALE
 ``` | ``` Scaling in Y direction. 
 Default value = 1. 
 Only applies to the DXFPAGE and DWGPAGE values of the TYPE parameter. (optional)
 ``` |
| ``` XOFFSET
 ``` | ``` Move to X direction. 
 Default value = 0. 
 Only applies to the DXFPAGE and DWGPAGE values of the TYPE parameter. (optional)
 ``` |
| ``` YOFFSET
 ``` | ``` Move to Y direction. 
 Default value = 0. 
 Only applies to the DXFPAGE and DWGPAGE values of the TYPE parameter. (optional)
 ``` |
| ``` MACROPROJECT
 ``` | ``` Full path of new macro project with file extension *.elk. 
 ``` |
| ``` ONLYMACROPROJECT
 ``` | ``` Determines whether only the marco projects are created (optional). 
 '¢ 1: Only create macro project. 
 '¢ 0: automatic export of all macros from created project to macro directory. 
 Default value = 0
 ``` |
| ``` CODEPAGE
 ``` | ``` Default value = 437.
 ``` |
| ``` DRIVE
 ``` |  |
| ``` SOURCEMACROPATH
 ``` | ``` The value must be uppercase and the macro must be located at the path: (drive):\EPLAN4\M\.
 ``` |
| ``` BALANCEARTICLES
 ``` | ``` Synchronization of imported parts data with database (optional).
 Default value = 0
 ``` |
| ``` GENERATEAUTOMATICCABLES
 ``` | ``` Indicates whether automatic cables are generated (optional).
 Default value = 0.
 ``` |
| ``` DESTINATIONFILE
 ``` | ``` Destination path with file name. 
 ``` |
| ``` VERIFY
 ``` | ``` Indicates whether a project check is started after the import (0 or 1) (optional).
 Default value = 0
 ``` |

**Remarks**

```
The following functions are supported:

'¢ Import PXF project

'¢ Import DXF/DWG drawings in macros (The import is not made via the project, but the DXF/DWG files are directly imported from a directory into the macros and stored in a directory.

'¢ Insert DXF / DWG drawing into a page

When an error occurs during an import operation, a "BaseException" is thrown.

```

**Example**

```
Import PXF project:

import /TYPE:PXFPROJECT /IMPORTFILE:C:\Projects\EPLAN_Sample_Project.epj /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk

Import DXF / DWG drawings in macros

import /TYPE:DXFDWGFILES /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /SOURCEPATH:C:\Projects\DXF_DWG /DESTINATIONPATH:C:\Macros

Insert DXF / DWG drawing into a page:

import /TYPE:DWGPAGE /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /PAGENAME:=AP+ST1/4 /IMPORTFILE:C:\Projects\EPLAN\DXF_DWG\pline_1.dwg /XSCALE:0.5 /YSCALE:0.5 /XOFFSET:100.0 /YOFFSET:100.0

```