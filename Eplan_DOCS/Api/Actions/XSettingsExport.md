# XSettingsExport

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XSettingsExport.html

---

```
 Exports settings to an XML file.

```

| Parameter | Description |
| --- | --- |
| ``` node
 ``` | ``` Path of a setting node (without PROJECT)
 ``` |
| ``` XMLFile
 ``` | ``` Full name of an XML file
 ``` |
| ``` prj
 ``` | ``` Project (has to be open)
 ``` |

**Example**

```
 XSettingsExport /node:USER /XMLFile:c:\my_user.xml

 XSettingsExport /node:STATION /XMLFile:c:\my_station.xml

 XSettingsExport /node:COMPANY /XMLFile:c:\my_company.xml

 XSettingsExport /node:USER.DIALOGSETTINGS /XMLFile:c:\my_dialog_settings.xml

 XSettingsExport /prj:EPLAN_Sample_Project /XMLFile:c:\my_project.xml

 XSettingsExport /prj:EPLAN_Sample_Project /node:XSbGui.CustomSymbols /XMLFile:c:\my_custom_symbols.xml

```