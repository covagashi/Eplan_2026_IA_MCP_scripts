# ExportData(Project,String,String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService~ExportData(Project,String,String,Boolean).html

---

Exports PLC data in the PLC standard exchange format (.pbf files) using the PlcDcXMLExchangerUniversal converter.

Syntax

**C#**



public void ExportData( 

   Project oProject,

   string strConfigurationProject,

   string strOutputFileName,

   bool bOverwrite

)

public:

void ExportData( 

   Project^ oProject,

   String^ strConfigurationProject,

   String^ strOutputFileName,

   bool bOverwrite

)


#### Parameters

*oProject*
:   Project of which the PLC data will be exported.

*strConfigurationProject*
:   A PLC configuration project. If you pass an empty string, all PLC data contained in the P8 project will be exported.

*strOutputFileName*
:   Full name of the output file without an extension. The filename extension is added automatically.

*bOverwrite*
:   If the output file already exists, this parameter specifies whether it should be overwritten.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing parameters. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the given Project does not exist or isn't valid. |
| **ApplicationException** | \Internal interface for exporting PLC data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the export. |

Remarks

In order to export PLC data using specific PLC data converter, use the overloaded ExportData method together with the GetAvailableConverters method. If the given directory in the full file name does not exist, it will be created.
