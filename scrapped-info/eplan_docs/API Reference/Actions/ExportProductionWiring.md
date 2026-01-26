# ExportProductionWiring

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/ExportProductionWiring.html

---

```
 Action to export Production Wiring Data for machines according to calling parameters.

```

| Parameter | Description |
| --- | --- |
| ``` MachineType
 ``` | ``` Type of machine (integer, mandatory). Possible values:
  '¢ 1 = "Komax",
  '¢ 2 = "CadCabel",
  '¢ 3 = "Schleuniger",
  '¢ 4 = "Steinhauer PWA",
  '¢ 5 = "Metzner",
  '¢ 7 = "WireList",
  '¢ 8 = "Averex",
  '¢ 9 = "Rittal - Wire Terminal WT" 
 ``` |
| ``` MachineName
 ``` | ``` Name of machine which has to be defined in settings (string, mandatory).
 ``` |
| ``` ProjectName
 ``` | ``` Name of the project (string, optional). If not set, the current project ist exported. If project name (including complete path and extension) is set, project is loaded (if needed) and activated.
 ``` |
| ``` UseSelection
 ``` | ``` Determines whether fields included in the current selection are used (integer, optional).
  0: "don't care for user selection", != 0: "use fields included in actual selection". Only used if ProjectName not set in parameters.
  Default value: 0
 ``` |
| ``` TargetDirectory
 ``` | ``` Determines target export directory (string, optional). If set, content overrides export directory of settings.
 ``` |
| ``` FileName
 ``` | ``` Determines target export file name (string, optional). If set, content overrides export file name of settings.
 ``` |
| ``` Language
 ``` | ``` Language code for export language (string, optional). Default value: "de_DE"
 ``` |
| ``` MultipleConnections
 ``` | ``` Determines wether already exported wires are reexported (bool, otional).
  If true, reexports already exported wires. If false, exports only those wires never exported before.
  Default value: false.
 ``` |

**Example**

```
ExportProductionWiring  /MACHINETYPE:5 /MACHINENAME:Metzner /TARGETDIRECTORY:D:\export /MultipleConnections:1  /UseSelection:0

```