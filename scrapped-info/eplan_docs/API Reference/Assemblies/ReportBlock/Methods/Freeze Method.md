# Freeze Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~Freeze.html

---

Removes the selected report block. The associated report pages remain as they are and are no longer updated.

Syntax

**C#**



public void Freeze()

public:

void Freeze();


Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown if this object is an embedded report. |

Remarks

Using this function for embedded reports in invalid and will throw an exception.
