# IsArticleDataReadOnly Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~IsArticleDataReadOnly.html

---

Determines whether the article reference data can be changed for this object.

Syntax

**C#**



public bool IsArticleDataReadOnly {get;}

public:

property bool IsArticleDataReadOnly {

   bool get();

}


Remarks

If [SegmentTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~SegmentTemplate.html) is assigned to this object then article references from this object can be added/removed/changed.
