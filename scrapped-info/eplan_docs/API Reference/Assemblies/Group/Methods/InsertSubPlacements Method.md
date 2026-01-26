# InsertSubPlacements Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~InsertSubPlacements.html

---

Insert [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s to a group.

Syntax

**C#**



public bool InsertSubPlacements( 

   Placement[] placements

)

public:

bool InsertSubPlacements( 

   array<Placement^>^ placements

)


#### Parameters

*placements*

#### Return Value

True if successful .

Exceptions

| Exception | Description |
| --- | --- |
| [ElementFromWrongPageException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ElementFromWrongPageException.html) | Thrown when one of given placements has page different from other placements in a group. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown in two cases: 1.When one of given placements is a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). 2. When one of given placements is a parent group of it. |

Remarks

This method doesn't make sense for class "SymbolVariant" and "DimensionGroup". It always throws [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) for class "SymbolVariant" and "DimensionGroup".
