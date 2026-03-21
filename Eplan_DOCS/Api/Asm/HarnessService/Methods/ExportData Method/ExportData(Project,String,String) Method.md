# ExportData(Project,String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.HarnessService~ExportData(Project,String,String).html

---

Exports Harness data from project without any filtering.

Syntax

**C#**



public void ExportData( 

   Project oProject,

   string strFileName,

   string strLanguage

)

public:

void ExportData( 

   Project^ oProject,

   String^ strFileName,

   String^ strLanguage

)


#### Parameters

*oProject*
:   Project of which the Harness data will be exported.

*strFileName*
:   Full name of the output file.

*strLanguage*
:   Language used during the export operation, e.g. de\_DE, en\_EN, etc.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing parameters. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the given Project does not exist or isn't valid. |
| **ApplicationException** | \Internal interface for exporting data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the export. |
