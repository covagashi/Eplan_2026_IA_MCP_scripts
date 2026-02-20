# Delete Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~Delete.html

---

Deletes all report pages belonging to a report block.

Syntax

**C#**



public void Delete()

public:

void Delete();


Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown if this object is an embedded report. |

Remarks

Using this function on embedded reports is invalid and will throw an exception.
