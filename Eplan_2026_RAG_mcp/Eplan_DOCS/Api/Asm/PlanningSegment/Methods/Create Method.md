# Create Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~Create.html

---

Creates PlanningSegment object.

Syntax

**C#**



public static PlanningSegment Create( 

   SegmentDefinition pSegmentDefinition

)

public:

static PlanningSegment^ Create( 

   SegmentDefinition^ pSegmentDefinition

)


#### Parameters

*pSegmentDefinition*
:   Segment definition based on which object will be created. Can't be null.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if `pSegmentDefinition` is `null`. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when object cannot be created. |
| [System.NotImplementedException](#) | Thrown when internal error occured. |
