# XPlaUpdateDetailAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XPlaUpdateDetailAction.html

---

```
The detail engineering is updated for the selected planning objects

```

| Parameter | Description |
| --- | --- |
| ``` PROJECTNAME
 ``` | ``` Specifies the full path to the project to be updated (optional). 
 ``` |
| ``` UpdateMacros
 ``` | ``` Determines whether the macros related to the planning object are removed and placed again (optional, 0 = No, 1 = Yes). Default value = 0 
 ``` |
| ``` UpdateIdentifier
 ``` | ``` Determines whether the structure identifiers, the symbolic adresses and the pipe names are written to the functions or pipe definitions (optional, 0 = No, 1 = Yes). Default value = 0 
 ``` |
| ``` UpdatePlaceholder
 ``` | ``` Determines whether the placeholder records from macros related to the planning object are updated (optional, 0 = No, 1 = Yes). Default value = 0 
 ``` |
| ``` UpdatePipedata
 ``` | ``` Determines whether the pipe class and substance are written to the pipe definition points and related connections and functions (optional, 0 = No, 1 = Yes). Default value = 0 
 ``` |
| ``` UpdateParts
 ``` | ``` Determines whether the pre-planning parts are synchronized with parts in the detailed planning (optional, 0 = No, 1 = Yes).
  If set to 1, the part information at the main functions in the detailed planning is deleted and replaced with the part information of the assigned segments. Default value = 0 
 ``` |

**Example**

```
   XPlaUpdateDetailAction /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /UpdateMacros:1 /UpdateIdentifier:1

```