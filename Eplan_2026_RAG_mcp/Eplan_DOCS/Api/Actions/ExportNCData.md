# ExportNCData

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/ExportNCData.html

---

```
 Action exports NC Data for machines.

```

| Parameter | Description |
| --- | --- |
| ``` MachineType
 ``` | ``` Type of machine (integer, mandatory). Possible values:
  '¢ 1 = "NC Steinhauer",
  '¢ 2 = "Rittal - Perforex BC",
  '¢ 3 = "NC DXF",
  '¢ 4 = "Drilling template",
  '¢ 5 = "Rittal - Perforex LC",
  '¢ 6 = "Copper NC",
  '¢ 7 = "Copper DXF",
  '¢ 8 = "Pipe bending"
 ``` |
| ``` MachineName
 ``` | ``` Name of machine which has to be defined in settings under COMPANY.NCLog.[MachineTypeScheme].[MachineName] (string, mandatory).
 ``` |
| ``` ProjectName
 ``` | ``` Name of the project (string, optional). If not set, the current project ist exported. If project name (including complete path and extension) is set, project is loaded (if needed) and activated.
 ``` |
| ``` UseSelection
 ``` | ``` Determines whether fields included in the current selection are used (integer, optional).
  0: "don't care for selection", != 0: "use fields included in actual selection". Only used if ProjectName not set in parameters.
  Default value: 0
 ``` |
| ``` TargetDirectory
 ``` | ``` Determines target export directory (string, optional). If set, content overrides export directory of settings.
 ``` |
| ``` MaterialName
 ``` | ``` If set and known in machine settings, this material is set for export (string, optional). Only used for Rittal Perforex BC, LC and Copper NC.
 ``` |

**Example**

```
ExportNCData /MACHINETYPE:2 /MACHINENAME:Standard /TARGETDIRECTORY:D:\export /MATERIALNAME:Steel

```