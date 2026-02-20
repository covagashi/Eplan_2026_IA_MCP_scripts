# XMExportDCArticleDataAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XMExportDCArticleDataAction.html

---

```
 Starts the export for the external editing.

```

| Parameter | Description |
| --- | --- |
| ``` COMPLETEPROJECT
 ``` | ``` The whole article database is exported, not only the selected objects (optional, 0 = No, 1 = Yes).
  Default value = 0
  
 ``` |
| ``` CONFIGSCHEME
 ``` | ``` Configuration scheme (optional).
  If this parameter is not set, a dialog asking for the configuration scheme is displayed.
 ``` |
| ``` LANGUAGE
 ``` | ``` Language (e.g. "en_US").
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
 XMExportDCArticleDataAction /CONFIGSCHEME:config_scheme /LANGUAGE:en_US /DESTINATION:c:\\temp\\Articles.xlsx /EXECUTIONMODE:0 /COMPLETEPROJECT:1

```