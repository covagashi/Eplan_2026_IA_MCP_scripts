# XMActionDCCommonExport

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XMActionDCCommonExport.html

---

```
 Starts the export for the external editing.

```

| Parameter | Description |
| --- | --- |
| ``` DATABASEID
 ``` | ``` The database ID of one project (optional).
  If not entered, the ProjectName parameter is used.
  
 ``` |
| ``` PROJECTNAME
 ``` | ``` The full path of project (optional).
  When project specified by ProjectName is not open, this action opens it and closes it automatically after this action is executed.
  If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar).
  
 ``` |
| ``` COMPLETEPROJECT
 ``` | ``` The whole project is exported, not only the selected objects (0 = No, 1 = Yes).
  
 ``` |
| ``` CONFIGSCHEME
 ``` | ``` Configuration scheme (optional).
  If this parameter is not set, a dialog asking for the configuration scheme is displayed.
 ``` |
| ``` LANGUAGE
 ``` | ``` Language (e.g. "en_US", "??_??" - all languages, etc).
 ``` |
| ``` DESTINATION
 ``` | ``` Target file where the export results are saved.
  The following formats are supported: TXT, XLSX, XML. Format must be set according to the extension in CONFIGSCHEME.
 ``` |
| ``` EXECUTIONMODE
 ``` | ``` 0 = Export,
  1 = Export and edit,
  2 = Edit and return
 ``` |
| ``` IMMEDIATEIMPORT
 ``` | ``` After edit no question appears to import the data (optional, 0 = No, 1 = Yes).
  Default value = 0
  This only applies to ExecutionMode = 2.
  
 ``` |

**Example**

```
 XMActionDCCommonExport /CONFIGSCHEME:config_scheme /COMPLETEPROJECT:1  /LANGUAGE:en_US /DESTINATION:c:\\temp\\Pages.xlsx /EXECUTIONMODE:0

```