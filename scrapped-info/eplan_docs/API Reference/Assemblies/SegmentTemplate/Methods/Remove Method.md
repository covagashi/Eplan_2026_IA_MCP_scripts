# Remove Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplate~Remove.html

---

Removes object from project with all its children.

Syntax

**C#**



public void Remove()

public:

void Remove();


Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown when template is assigned to planning object. |

Remarks

Object can't be removed if it is assign to a planning segment.
