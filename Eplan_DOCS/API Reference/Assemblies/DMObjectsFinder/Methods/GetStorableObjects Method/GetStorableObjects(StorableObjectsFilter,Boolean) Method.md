# GetStorableObjects(StorableObjectsFilter,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetStorableObjects(StorableObjectsFilter,Boolean).html

---

This function takes all objects of classes StorableObject and inherited from StorableObject except [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and filters them with the given filter. This method does not return [Eplan.EplApi.DataModel.Graphics.PropertyPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html) and [Eplan.EplApi.DataModel.MasterData.Symbol](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Symbol.html).

Syntax

**C#**



public StorableObject[] GetStorableObjects( 

   StorableObjectsFilter filter,

   bool bWithPlacements

)

public:

array<StorableObject^>^ GetStorableObjects( 

   StorableObjectsFilter^ filter,

   bool bWithPlacements

)


#### Parameters

*filter*
:   a [StorableObjectsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter.html), can be `null`

*bWithPlacements*
:   If Placaments should be returned.

#### Return Value

\* [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s matching given [StorableObjectsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter.html). \* All [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
