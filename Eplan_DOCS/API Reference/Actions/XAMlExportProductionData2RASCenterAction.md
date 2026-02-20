# XAMlExportProductionData2RASCenterAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XAMlExportProductionData2RASCenterAction.html

---

```
 Export of the construction spaces of the selected project in AutomationML format.

 The generated AutomationML file is intended for import into the Rittal - RiPanel Processing Center,

 which controls the machines for creating the openings or cutting the mounting rails and wiring channels.

```

| Parameter | Description |
| --- | --- |
| ``` ProjectPath
 ``` | ``` Project which should be exported.
  Note, this project has to be opened in P8 beforehand.
  If ProjectPath is invalid, the current Project will be used.
 ``` |
| ``` FileName
 ``` | ``` Projectpath + Filename where the project will be exported to. If this parameter is empty, a dialog will be shown.
 ``` |
| ``` DatabaseId
 ``` | ``` Database ID of the project to be exported.
 ``` |
| ``` WholeProject
 ``` | ``` Determines wether to use the whole project for input objects for export (optional).
 ``` |
| ``` ConfigScheme
 ``` | ``` Configuration scheme (optional). Default value: Most recently used configuration scheme.
 ``` |

**Remarks**

```
If the file used in FileName already exists a dialog will be shown, to ask whether it should be

 overwritten or not.

```

**Example**

```
   XAMlExportProductionData2RASCenterAction /ProjectPath:C:\Projects\EPLAN\EPLAN_Sample_Project.elk

                /FileName:C:\Exports\EPLAN\EPLAN_Sample_Project.aml

        XAMlExportProductionData2RASCenterAction /DatabaseId:27

                /FileName:C:\Exports\EPLAN\EPLAN_Sample_Project.aml

```