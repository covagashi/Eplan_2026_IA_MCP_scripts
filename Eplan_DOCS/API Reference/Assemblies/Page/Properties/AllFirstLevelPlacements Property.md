# AllFirstLevelPlacements Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~AllFirstLevelPlacements.html

---

All [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s including [Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)s placed on this page. They are not filtered. All returned [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s are placed directly on this page. This method does not return embedded objects (like for example [Eplan.EplApi.DataModel.Graphics.Shielding](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Shielding.html)).

Syntax

**C#**



public Placement[] AllFirstLevelPlacements {get;}

public:

property array<Placement^>^ AllFirstLevelPlacements {

   array<Placement^>^ get();

}


#### Property Value

All [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s from the page.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the page is transient. |
