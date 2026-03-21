# CreateEmbeddedReport(ReportBlock,Page,PointD) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Reports~CreateEmbeddedReport(ReportBlock,Page,PointD).html

---

Creates embedded report.

Syntax

**C#**



public ReportBlockReference CreateEmbeddedReport( 

   ReportBlock oReportBlock,

   Page oPage,

   PointD oLocation

)

public:

ReportBlockReference^ CreateEmbeddedReport( 

   ReportBlock^ oReportBlock,

   Page^ oPage,

   PointD oLocation

)


#### Parameters

*oReportBlock*
:   Report block which describes the embedded report.

*oPage*
:   `Page` on which the embedded report will me placed.

*oLocation*
:   Location on the `Page` where the upper-left corner of the embedded report will be placed.

#### Return Value

Returns `ReportBlockReference` object related to created report, or null if report wasn't created.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Null was set to one of parameters. |
| [System.ArgumentException](#) | If form which name and type are stored in `oReportBlock` has not been found in project. If name or type of form are incorrect. If page isn't interactive or one of parameters is invalid. |
| [System.ApplicationException](#) | Failed to create embedded report. Please refer to the error message. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An internal error occurred during creating embedded report Please refer to the error message. |
| [Eplan.EplApi.HEServices.Exceptions.InvalidScheme](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Exceptions.InvalidScheme.html) | Thrown when invalid scheme name is set and scheme data is empty. Please refer to the error message for more information. |

Remarks

Embedded report can be created only on interactive page.

If **Eplan::EplApi::DataModel::ReportBlock:** is set and **Eplan::EplApi::DataModel::ReportBlock:** is empty then **Eplan::EplApi::DataModel::ReportBlock:** will be filled automatically. The same is with **Eplan::EplApi::DataModel::ReportBlock:**.

Example

Example shows how to create an embedded report on page:

**C#**

```
String strForm = "F01_002.f01";

ReportBlock oReport = new ReportBlock();

oReport.Create(m_oTestProject);

oReport.FormName = System.IO.Path.GetFileNameWithoutExtension(strForm);

oReport.Type = DocumentTypeManager.DocumentType.PartsList;

oReport.FilterSchemaName = "Project part";

//leave FilterSchemaData blank; this way it will be filled automatically by Reports::CreateEmbeddedReport

//oReport.FilterSchemaData = null;

ReportBlockReference oReportBlockReference = new Reports().CreateEmbeddedReport(oReport);

```
