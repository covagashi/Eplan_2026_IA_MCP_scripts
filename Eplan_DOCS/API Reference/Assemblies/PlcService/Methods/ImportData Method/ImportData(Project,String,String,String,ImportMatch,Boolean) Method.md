# ImportData(Project,String,String,String,ImportMatch,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1398.html

---

Imports PLC data using the specified converter.

Syntax

**C#**



public void ImportData( 

   Project oProject,

   string strConverterID,

   string strLanguage,

   string strInputFileName,

   PlcService.ImportMatch eImportMatch,

   bool bShowCompareDlg

)

public:

void ImportData( 

   Project^ oProject,

   String^ strConverterID,

   String^ strLanguage,

   String^ strInputFileName,

   PlcService.ImportMatch eImportMatch,

   bool bShowCompareDlg

)


#### Parameters

*oProject*
:   Project which the PLC data will be imported to.

*strConverterID*
:   ID of the PLC data converter to use. The IDs of the registered PLC converters together with their full names may be obtained by calling the GetAvailableConverters method.

*strLanguage*
:   Language used during the import process, e.g. de\_DE, en\_EN, etc.

*strInputFileName*
:   The input file name in the format corresponding to the converter used.

*eImportMatch*
:   Matching criteria for PLC data import.

*bShowCompareDlg*
:   Shows compare dialog when true.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing parameters. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the given Project does not exist or isn't valid. |
| **ApplicationException** | \Internal interface for exporting PLC data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the export. |

Remarks

Use the GetAvailableConverters method to get the list of registered PLC data converters.
