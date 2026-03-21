# CreateTransient Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~CreateTransient.html

---

Creates transient PlanningSegment object.

Syntax

**C#**



public static PlanningSegment CreateTransient( 

   SegmentDefinition pSegmentDefinition

)

public:

static PlanningSegment^ CreateTransient( 

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
