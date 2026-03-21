# DeleteLink Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~DeleteLink.html

---

Deletes a link from this object that links given targetSegment.

Syntax

**C#**



public bool DeleteLink( 

   PlanningSegment targetSegment

)

public:

bool DeleteLink( 

   PlanningSegment^ targetSegment

)


#### Parameters

*targetSegment*
:   Segment for which link will be deleted.

#### Return Value

Returns false when targetSegment is from different project.

Remarks

In case there are multiple identical segments, only first will be removed.
