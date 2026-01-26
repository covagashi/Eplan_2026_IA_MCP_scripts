# ExportData(Project,String,String,FilterMode,IEnumerable<String>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1363.html

---

Exports Harness data.

Syntax

**C#**



public void ExportData( 

   Project oProject,

   string strFileName,

   string strLanguage,

   HarnessService.FilterMode nFilterMode,

   IEnumerable<string> colFilterValues

)

public:

void ExportData( 

   Project^ oProject,

   String^ strFileName,

   String^ strLanguage,

   HarnessService.FilterMode nFilterMode,

   IEnumerable<String^>^ colFilterValues

)


#### Parameters

*oProject*
:   Project of which the Harness data will be exported.

*strFileName*
:   Full name of the output file.

*strLanguage*
:   Language used during the export operation, e.g. de\_DE, en\_EN, etc.

*nFilterMode*
:   Defines the scope of export.

*colFilterValues*
:   Specifies the filter criteria for given filtering mode. Collection can contain wire harness names.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing parameters. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the given Project does not exist or isn't valid. |
| **ApplicationException** | \Internal interface for exporting data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the export. |

Example

Following example shows how to use the method:

**C#**

```
new HarnessService().ExportData(m_oTestProject, strDestinationFilePath, strExportLang, HarnessService.FilterMode.HarnessRelated, new List<String>() { strHarnessName1, strHarnessName2 });

```
