# edit

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/edit.html

---

```
Action class for edit functions: Opens a project, opens a specific page (identified by the page name), opens a page with a specific device (identified by the device name) or opens a specific page (identified by the page name) and sets the cursor at the X and Y coordinates.

```

| Parameter | Description |
| --- | --- |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not specified, the selected project is used when the action is called from GUI (e.g. from a script or the ribbon bar). 
 If called from the Windows command line, the PROJECTNAME parameter must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` PAGENAME
 ``` | ``` Name of the page to open (optional). Required if the X and Y parameters are specified.
 ``` |
| ``` DEVICENAME
 ``` | ``` Name of an item (optional).
 ``` |
| ``` X
 ``` | ``` X coordinate (optional). Parameter is only valid if the PAGENAME parameter is specified.
 ``` |
| ``` Y
 ``` | ``` Y coordinate (optional). Parameter is only valid if the PAGENAME parameter is specified.
 ``` |
| ``` INSTALLATIONSPACE
 ``` | ``` Name of the layout space to be opened (optional). Cannot be used with the PAGENAME parameter and with the DEVICENAME3D parameter.
 ``` |
| ``` DEVICENAME3D
 ``` | ``` Name of an item inside of an layout space (optional). Cannot be used with the INSTALLATIONSPACE parameter.
 ``` |
| ``` IGNOREWHENOPEN
 ``` | ``` Specifies whether to ignore action calls when a project is already open. (optional, 0 = No, 1 = Yes).
 ``` |

**Remarks**

```
The current action checks the parameters and performs the corresponding operation. One of the following operations will be executed. 

The operation n° 1 has the highest priority and the operation n° 5 has the lowest priority. 

For example if a page name and device name are set, the operation n° 1 will be executed. 

Otherwise, it checks if it is possible to perform the remaining operations. 

If no parameter is set at all, the project will be opened (operation n° 5).

'¢ 1: Opens a specific page (identified by the page name) with a specific device (identified by the device name). The device will be selected. If the specified device is not found on the page, the page will be opened and no element will be selected.

           In this case, an error message will be inserted into message system.

'¢ 2: Opens a specific page (identified by the page name), X and Y coordinates.

'¢ 3: Opens a specific page (identified by the page name).

'¢ 4: Opens the page containing the first device name found.

'¢ 5: Opens a project.

When an error occurs during an edit operation, a "BaseException" is thrown.

```

**Example**

```
Open a project:

edit /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk

Open a page:

edit /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /PAGENAME:=AP+ST1/7

Open a page by a device tag of a device that is located on the page:

edit /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /DEVICENAME:=AP+PT1-G1

Open a page and set the cursor to X and Y position:

edit /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /PAGENAME:=AP+ST1/7 /X:200 /Y:100

Open a layout space:

edit /PROJECTNAME:$(MD_PROJECTS)\EPLAN_Sample_Project.elk /INSTALLATIONSPACE:"=EB3+ET1 (-MP1)"

Open an item inside of an layout space:

edit /PROJECTNAME:$(MD_PROJECTS)\EPLAN_Sample_Project.elk /DEVICENAME3D:=EB3+ET1-F14

```