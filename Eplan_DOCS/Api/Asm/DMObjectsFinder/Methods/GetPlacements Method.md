# GetPlacements Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlacements.html

---

This function takes objects of classes Placement and inherited from Placement except [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and filters them with the given filter. This method does not return embedded objects (like for example [Eplan.EplApi.DataModel.Graphics.Shielding](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Shielding.html)). This method does not return [Eplan.EplApi.DataModel.Graphics.PropertyPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html).

Syntax

**C#**



public Placement[] GetPlacements( 

   PlacementsFilter filter

)

public:

array<Placement^>^ GetPlacements( 

   PlacementsFilter^ filter

)


#### Parameters

*filter*
:   a [PlacementsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementsFilter.html), can be `null`

#### Return Value

\* [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s matching given [PlacementsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementsFilter.html). \* All [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
