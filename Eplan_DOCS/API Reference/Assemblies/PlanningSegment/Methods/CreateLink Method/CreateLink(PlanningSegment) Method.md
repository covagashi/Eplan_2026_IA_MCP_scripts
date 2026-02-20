# CreateLink(PlanningSegment) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~CreateLink(PlanningSegment).html

---

Creates a link between this object and given targetSegment.

Syntax

**C#**



public bool CreateLink( 

   PlanningSegment targetSegment

)

public:

bool CreateLink( 

   PlanningSegment^ targetSegment

)


#### Parameters

*targetSegment*
:   Segment which will be linked under this object.

#### Return Value

Returns false when targetSegment is from different project.
