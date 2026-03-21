# print

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/print.html

---

```
Action class to print projects and pages.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of task to ben performed:
 '¢ "PROJECT": Print project.
 '¢ "PAGES": Print pages.
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` PRINTERNAME
 ``` | ``` Name of printer (optional).
 Default value: Printer set on your computer.
 ``` |
| ``` PAGENAME
 ``` | ``` Page to be printed (optional).
 ``` |
| ``` PRINTCOLLATE
 ``` | ``` Sorted order (optional, 0 = No, 1 = Yes).
 Default value: 1
 ``` |
| ``` PRINTREVERSE
 ``` | ``` Reverse order (optional, 0 = No, 1 = Yes).
 Default value: 0 
 ``` |
| ``` NUMBER
 ``` | ``` Number of copies.
 Default:1 
 ``` |
| ``` DESTINATIONFILE
 ``` | ``` Path and name of the output file.
 Default value: Printer set or Specified 
 ``` |
| ``` USEPAGEFILTER
 ``` | ``` Determines if only filtered pages should be used or all project pages (optional). It corresponds to "Active"check box in GUI.
 Default value: 0 
 ``` |
| ``` PRINTCHANGEDPAGES
 ``` | ``` Print only changed pages
 ``` |

**Remarks**

```
'¢ If a page was explicitly entered by the PAGENAME parameter, then only this page is printed and the USEPAGEFILTER, parameter is ignored.

'¢ If no specific page was explicitly entered by the PAGENAME parameter, project pages are determined. If USEPAGEFILTER is set to 1, only pages filtered in GUI page navigator will be printed. If USEPAGEFILTER is not used or if it is set to 0, all project pages will be printed.

'¢ USEPAGEFILTER corresponds to "Active" check box in the page navigator.

'¢ Warning! Please check settings under "Workstation > Graphical editing > Print" because they overwrite parameters of the action.

'¢ When an error occurs during a print operation, a "BaseException" is thrown.

```

**Example**

```
Print page:

print /TYPE:PAGES /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /PAGENAME:=AP+ST1/6 /PRINTERNAME:my_printer /NUMBER:2

Print page to file:

print /TYPE:PAGES /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /PRINTCOLLATE:0 /PRINTREVERSE:1 /DESTINATIONFILE:C:\TEMP\ESS_Sample_Project_print.prn /USEPAGEFILTER:1

Print project:

print /TYPE:PROJECT /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /PRINTCOLLATE:0 /PRINTREVERSE:1 /DESTINATIONFILE:C:\TEMP\\ESS_Sample_Project_print.prn

```