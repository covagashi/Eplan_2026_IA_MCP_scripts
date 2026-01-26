# InsertSubPlacement Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~InsertSubPlacement.html

---

Insert [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) to a group.

Syntax

**C#**



public bool InsertSubPlacement( 

   Placement placement

)

public:

bool InsertSubPlacement( 

   Placement^ placement

)


#### Parameters

*placement*

#### Return Value

True if successful .

Exceptions

| Exception | Description |
| --- | --- |
| [ElementFromWrongPageException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ElementFromWrongPageException.html) | Thrown when given placement has page different from other placements in a group. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown in two cases: 1. When given placement is a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). 2. When given placement is a parent group of it. |

Remarks

This method doesn't make sense for class "SymbolVariant" and "DimensionGroup". It always throws [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) for class "SymbolVariant" and "DimensionGroup".
