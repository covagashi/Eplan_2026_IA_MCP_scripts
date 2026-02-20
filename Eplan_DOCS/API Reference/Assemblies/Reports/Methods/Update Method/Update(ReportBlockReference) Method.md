# Update(ReportBlockReference) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Reports~Update(ReportBlockReference).html

---

Updates dynamic formular or embedded report represented by [Eplan.EplApi.DataModel.ReportBlockReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlockReference.html).

Syntax

**C#**



public void Update( 

   ReportBlockReference oReportBlockRef

)

public:

void Update( 

   ReportBlockReference^ oReportBlockRef

)


#### Parameters

*oReportBlockRef*
:   Report to be updated.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An internal error occurred during creating embedded report Please refer to the error message. |
| [System.ArgumentNullException](#) | Thrown when `oReportBlockRef` is null, not placed or is invalid. |
