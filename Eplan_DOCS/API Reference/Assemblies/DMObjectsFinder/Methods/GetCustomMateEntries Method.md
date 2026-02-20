# GetCustomMateEntries Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetCustomMateEntries.html

---

Returns user defined [Eplan.EplApi.DataModel.E3D.MateEntry](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MateEntry.html)s of all project [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)s matching given filter.

Syntax

**C#**



public MateEntry[] GetCustomMateEntries( 

   Placements3DFilter filter

)

public:

array<MateEntry^>^ GetCustomMateEntries( 

   Placements3DFilter^ filter

)


#### Parameters

*filter*
:   a [Placements3DFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placements3DFilter.html), can be `null`

#### Return Value

\* [Eplan.EplApi.DataModel.E3D.MateEntry](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MateEntry.html)s of all project [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)s matching given [Placements3DFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placements3DFilter.html).  
\* All [Eplan.EplApi.DataModel.E3D.MateEntry](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MateEntry.html)s if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
