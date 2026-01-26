# CreateTransient Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentPlacement~CreateTransient.html

---

Creates transient and place planning placement on page.

Syntax

**C#**



public void CreateTransient( 

   PlanningSegment pSourceSegment,

   Page pPage

)

public:

void CreateTransient( 

   PlanningSegment^ pSourceSegment,

   Page^ pPage

)


#### Parameters

*pSourceSegment*
:   Planning segment for which placement will be created. Can't be `null`.

*pPage*
:   Page on which placement will be created. Can't be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when parameter is `null`. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when object cannot be created. |
