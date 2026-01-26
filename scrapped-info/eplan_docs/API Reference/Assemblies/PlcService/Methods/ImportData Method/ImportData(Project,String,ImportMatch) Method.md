# ImportData(Project,String,ImportMatch) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService~ImportData(Project,String,ImportMatch).html

---

Imports PLC data from a file in the PLC standard exchange format (.pbf files) using the PlcDcXMLExchangerUniversal converter.

Syntax

**C#**



public void ImportData( 

   Project oProject,

   string strFullName,

   PlcService.ImportMatch eImportMatch

)

public:

void ImportData( 

   Project^ oProject,

   String^ strFullName,

   PlcService.ImportMatch eImportMatch

)


#### Parameters

*oProject*
:   Project into which the PLC data will be imported.

*strFullName*
:   Full file name of the file to import.

*eImportMatch*
:   Matching criteria for PLC data import.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing parameters. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the given Project does not exist or isn't valid. |
| **ApplicationException** | \Internal interface for importing PLC data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the import. |

Remarks

In order to import PLC data using specific PLC data converter, use the overloaded ImportData method together with the GetAvailableConverters method.
