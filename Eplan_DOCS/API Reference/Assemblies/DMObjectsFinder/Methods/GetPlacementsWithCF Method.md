# GetPlacementsWithCF Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlacementsWithCF.html

---

Returns all objects of classes Placement and inherited from Placement, except [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html), which matches to given filter.

Syntax

**C#**



public Placement[] GetPlacementsWithCF( 

   ICustomFilter filter

)

public:

array<Placement^>^ GetPlacementsWithCF( 

   ICustomFilter^ filter

)


#### Parameters

*filter*
:   a custom filter object implementing [ICustomFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ICustomFilter.html)

#### Return Value

\* [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s matching given custom filter. \* All [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
