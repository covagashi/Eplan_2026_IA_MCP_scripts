# Create Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~Create.html

---

Creates a new Group object. It is placed on the page of first placement given as parameter.

Syntax

**C#**



public virtual void Create( 

   Placement[] placements

)

public:

virtual void Create( 

   array<Placement^>^ placements

)


#### Parameters

*placements*
:   Placements that create the group.

Exceptions

| Exception | Description |
| --- | --- |
| [ElementFromWrongPageException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ElementFromWrongPageException.html) | Thrown when first placement doesn't have valid page. |
| [InsufficientElementsCountException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InsufficientElementsCountException.html) | Thrown when number of placements is less than two. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown in two cases: 1.When one of given placements is a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). 2. When one of given placements is a parent group of it. |
