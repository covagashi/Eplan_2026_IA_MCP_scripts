# LocalTemplates Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~LocalTemplates.html

---

Returns set of local templates assigned to this object or to its segment template.

Syntax

**C#**



public StorableObject[] LocalTemplates {get;}

public:

property array<StorableObject^>^ LocalTemplates {

   array<StorableObject^>^ get();

}


Remarks

If [SegmentTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~SegmentTemplate.html) is assigned then set of local templates from segment template are returned. If `not` then set of local templates from this object is returned.
