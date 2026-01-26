# CreateEmbeddedReport(ReportBlock) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Reports~CreateEmbeddedReport(ReportBlock).html

---

Creates embedded report. This method starts an interaction so the report is attached to the mouse pointer.

Syntax

**C#**



public ReportBlockReference CreateEmbeddedReport( 

   ReportBlock oReportBlock

)

public:

ReportBlockReference^ CreateEmbeddedReport( 

   ReportBlock^ oReportBlock

)


#### Parameters

*oReportBlock*
:   Report block which describes the embedded report.

#### Return Value

Returns `ReportBlockReference` object related to created report or null if report wasn't created.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | If `oReportBlock` is null. |
| [System.ArgumentException](#) | If form which name and type are stored in `oReportBlock` has not been found in project. If name or type of the form are incorrect. |
| [System.ApplicationException](#) | Failed to create embedded report. Please refer to the error message. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An internal error occurred during creating embedded report Please refer to the error message. |
| [Eplan.EplApi.HEServices.Exceptions.InvalidScheme](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Exceptions.InvalidScheme.html) | Thrown when invalid scheme name is set and scheme data is empty. Please refer to the error message for more information. |

Remarks

Embedded report can be created only on interactive page.

Method can't be used if the application was start in quiet mode.

If **Eplan::EplApi::DataModel::ReportBlock:** is set and **Eplan::EplApi::DataModel::ReportBlock:** is empty then **Eplan::EplApi::DataModel::ReportBlock:** will be filled automatically. The same is with **Eplan::EplApi::DataModel::ReportBlock:**.

Example

Example shows how to create an embedded report:

**C#**

```
string strForm = "F01_002.f01";

StringCollection oProjectNewEntries = new StringCollection();

oProjectNewEntries.Add(strForm);

new Masterdata().AddToProjectEx(m_oTestProject, oProjectNewEntries);

PointD oPoint = new PointD(100.0, 30.0);

ReportBlock oReport = new ReportBlock();

oReport.Create(m_oTestProject);

oReport.FormName = System.IO.Path.GetFileNameWithoutExtension(strForm);

oReport.Type = DocumentTypeManager.DocumentType.DeviceConnectionDiagram;

ReportBlockReference oReportBlockReference = new Reports().CreateEmbeddedReport(oReport, m_oTestProject.Pages[14], oPoint);

```
