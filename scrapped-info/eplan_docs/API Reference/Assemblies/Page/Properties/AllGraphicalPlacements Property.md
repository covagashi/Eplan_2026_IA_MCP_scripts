# AllGraphicalPlacements Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~AllGraphicalPlacements.html

---

All [Eplan.EplApi.DataModel.Graphics.GraphicalPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacement.html)s placed on this page. They are not filtered. This method does not return embedded objects (like for example [Eplan.EplApi.DataModel.Graphics.Shielding](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Shielding.html)).

Syntax

**C#**



public GraphicalPlacement[] AllGraphicalPlacements {get;}

public:

property array<GraphicalPlacement^>^ AllGraphicalPlacements {

   array<GraphicalPlacement^>^ get();

}


#### Property Value

All GraphicalPlacements from the page.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the page is transient. |
