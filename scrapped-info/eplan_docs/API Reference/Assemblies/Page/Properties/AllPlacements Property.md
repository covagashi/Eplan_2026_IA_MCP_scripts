# AllPlacements Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~AllPlacements.html

---

All [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s, placed on this page. [Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)s are ungrouped and contained [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s are returned. They are not filtered. This method does not return embedded objects (like for example [Eplan.EplApi.DataModel.Graphics.Shielding](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Shielding.html)). This method does not return [Eplan.EplApi.DataModel.Graphics.PropertyPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html).

Syntax

**C#**



public Placement[] AllPlacements {get;}

public:

property array<Placement^>^ AllPlacements {

   array<Placement^>^ get();

}


#### Property Value

All [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s from the page, without [Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)s.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the page is transient. |
