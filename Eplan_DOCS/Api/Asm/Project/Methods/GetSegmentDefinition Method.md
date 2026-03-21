# GetSegmentDefinition Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~GetSegmentDefinition.html

---

Returns [Eplan.EplApi.DataModel.Planning.SegmentDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition.html) from this Project with given name.

Syntax

**C#**



public SegmentDefinition GetSegmentDefinition( 

   string strIdentName

)

public:

SegmentDefinition^ GetSegmentDefinition( 

   String^ strIdentName

)


#### Parameters

*strIdentName*
:   Identifying name of the segment definition to be found.

#### Return Value

Segment definition with given identifying name or `null` if such definition is not found.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when name is empty. |
| [System.ArgumentNullException](#) | Thrown when name is `null`. |
