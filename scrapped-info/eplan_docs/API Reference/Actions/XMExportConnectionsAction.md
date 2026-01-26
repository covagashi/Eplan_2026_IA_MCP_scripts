# XMExportConnectionsAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XMExportConnectionsAction.html

---

```
 Action class to export connections of a project.

```

| Parameter | Description |
| --- | --- |
| ``` DatabaseId
 ``` | ```  The database ID of one project (optional).
  If not entered, the ProjectName parameter is used.
  
 ``` |
| ``` ProjectName
 ``` | ```  The full path of project (optional).
  When project specified by ProjectName is not open, this action opens it and closes it automatically after this action is executed.
  If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar).
  
 ``` |
| ``` CompleteProject
 ``` | ```  All connections of the project are exported, not only the selected ones (0 = No, 1 = Yes).
  
 ``` |
| ``` ConfigScheme
 ``` | ```  Configuration scheme (optional).
  Default value = Most recently used configuration scheme.
 ``` |
| ``` Language
 ``` | ```  Language (e.g. "en_US").
 ``` |
| ``` Destination
 ``` | ```  Target file where the export results are saved.
  The following formats are supported: TXT, XLSX, XML. Format must be set according to the extension in ConfigScheme.
 ``` |
| ``` ExecutionMode
 ``` | ```  0 = Export,
  1 = Export and edit,
  2 = Edit and return
 ``` |
| ``` ImmediateImport
 ``` | ``` After edit no question appears to import the data (optional, 0 = No, 1 = Yes).
  Default value = 0
  This only applies to ExecutionMode = 2.
  
 ``` |
| ``` IncludeGraphicalConnections
 ``` | ``` Graphical connections are included in the export (optional, 0 = No, 1 = Yes).
  Default value = 0
  
 ``` |

**Remarks**

```
 This action is provided for backward compatibility. Please use the action "XMActionDCCommonExport" instead.

```

**Example**

```
 XMExportConnectionsAction /ConfigScheme:config_scheme /CompleteProject:1  /Language:en_US /Destination:c:\\temp\\Connection.xlsx /ExecutionMode:0

```