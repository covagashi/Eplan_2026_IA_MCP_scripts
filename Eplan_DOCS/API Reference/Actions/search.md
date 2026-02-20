# search

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/search.html

---

```
Action class for search operations. Searchs items in a project.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Describes the search area:
 "DEVICETAG": Search for devices
 "ALLPROPERTIES": Search through all properties
 "TEXTS": Text search
 "PAGEDATA": Search through page data
 "PROJECTDATA": Search through project data
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction (see also "XEsProjectAction") must be used first, otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` SEARCHITEM
 ``` | ``` Text you are searching for.
 ``` |
| ``` CASESENSITIVE
 ``` | ``` Match case (optional, 1 = Yes, 0 = No).
 Default value: Most recently used value which is currently set in GUI.
 ``` |
| ``` WHOLETEXT
 ``` | ``` Find whole texts only (optional, 1 = Yes, 0 = No).
 Default value: Most recently used value which is currently set in GUI.
 ``` |
| ``` LOGICPAGES
 ``` | ``` Search on logic pages (optional, 1 = Yes, 0 = No).
 Default value: Most recently used value which is currently set in GUI.
 ``` |
| ``` GRAPHICPAGES
 ``` | ``` Search on graphical pages (optional, 1 = Yes, 0 = No).
 Default value: Most recently used value which is currently set in GUI.
 ``` |
| ``` EVALUATIONPAGES
 ``` | ``` Search on report pages (optional, 1 = Yes, 0 = No).
 Default value: Most recently used value which is currently set in GUI.
 ``` |
| ``` NOTPLACEDFUNCTIONS
 ``` | ``` Search in unplaced functions (optional, 1 = Yes, 0 = No).
 Default value: Most recently used value which is currently set in GUI.
 ``` |
| ``` FILTERSCHEME
 ``` | ``` Function filter scheme (optional). If this parameter is set, only data matching the function filter scheme criteria will be searched. 
 Default value: Use no function filter scheme.
 ``` |
| ``` SEARCHDB
 ``` | ``` Don't use this parameter any more.
 ``` |

**Remarks**

```
The results of the search will only be visible in the list of results dialog, if the project for which the search was conducted is currently open in EPLAN.

When an error occurs during a search operation, a "BaseException" is thrown.

```

**Example**

```
search /TYPE:TEXTS /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /SEARCHITEM:Hallo /CASESENSITIVE:1 /WHOLETEXT:0 /LOGICPAGES:1

search /TYPE:PAGEDATA /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /SEARCHITEM:Antrieb /CASESENSITIVE:0 /WHOLETEXT:0 /LOGICPAGES:1 /EVALUATIONPAGES:1 /NOTPLACEDFUNCTIONS:1

```