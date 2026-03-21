# ExportGenerateSchematicConfiguration Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService~ExportGenerateSchematicConfiguration.html

---

Exports generate schematic configuration into xml file. TODO:

Syntax

**C#**



public void ExportGenerateSchematicConfiguration( 

   Project project,

   string fileName

)

public:

void ExportGenerateSchematicConfiguration( 

   Project^ project,

   String^ fileName

)


#### Parameters

*project*
:   Project of which the PLC configuration will be exported.

*fileName*
:   Full name of the export file.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing parameters. |
| **ArgumentException** | Thrown in case of invalid arguments. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the export. |

Remarks

If the given directory in the full file name does not exist, it will be created.
