# ReportBlock Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlockReference~ReportBlock.html

---

`ReportBlock` associated with this `ReportBlockReference`.

Syntax

**C#**



public ReportBlock ReportBlock {get;}

public:

property ReportBlock^ ReportBlock {

   ReportBlock^ get();

}


Remarks

Property returns [ReportBlock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock.html) object only for embedded reports. For page reports check [Page.ReportBlock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~ReportBlock.html).
