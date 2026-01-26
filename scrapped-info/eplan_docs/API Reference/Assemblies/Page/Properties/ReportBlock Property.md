# ReportBlock Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~ReportBlock.html

---

`ReportBlock` which contains data describing report from this page.

Syntax

**C#**



public ReportBlock ReportBlock {get;}

public:

property ReportBlock^ ReportBlock {

   ReportBlock^ get();

}


Remarks

If a report is assign to a page then this property returns an object which contains data describing it. If no report is assign then this property returns `null`.
