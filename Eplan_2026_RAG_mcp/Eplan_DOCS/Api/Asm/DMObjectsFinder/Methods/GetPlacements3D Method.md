# GetPlacements3D Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlacements3D.html

---

Returns [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)s matching given filter. This method does not return [Eplan.EplApi.DataModel.E3D.MateEntry](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MateEntry.html)s.

Syntax

**C#**



public Placement3D[] GetPlacements3D( 

   Placements3DFilter filter

)

public:

array<Placement3D^>^ GetPlacements3D( 

   Placements3DFilter^ filter

)


#### Parameters

*filter*
:   a [Placements3DFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placements3DFilter.html), can be `null`

#### Return Value

\* [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)s matching given [Placements3DFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placements3DFilter.html). \* All [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)s if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
