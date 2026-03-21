# XMActionDCImport

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XMActionDCImport.html

---

```
 Imports a data configuration file into an existing EPLAN project.

```

| Parameter | Description |
| --- | --- |
| ``` ProjectLink
 ``` | ``` Project path
 ``` |
| ``` DataConfigurationFile
 ``` | ``` Path of data configuration file
 ``` |
| ``` ProgressTitle
 ``` | ``` Defines the progress title (optional)
 ``` |

**Remarks**

```
 This allows the properties of functions to be changed.

 The data configuration file can be created e.g. via the ribbon item "File > Export > Project Data > External Editing > Properties".

```

**Example**

```
        XMActionDCImport /ProjectLink:c:\\Projects\\EPLAN\\test.elk /DataConfigurationFile:c:\\EPLAN\\DataCfgFile.edc

```