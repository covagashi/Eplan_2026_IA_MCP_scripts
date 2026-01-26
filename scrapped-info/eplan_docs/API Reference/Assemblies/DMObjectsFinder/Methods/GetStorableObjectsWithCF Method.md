# GetStorableObjectsWithCF Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetStorableObjectsWithCF.html

---

Returns all objects of classes StorableObject and inherited from StorableObject, except [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html), which matches to given filter.

Syntax

**C#**



public StorableObject[] GetStorableObjectsWithCF( 

   ICustomFilter filter

)

public:

array<StorableObject^>^ GetStorableObjectsWithCF( 

   ICustomFilter^ filter

)


#### Parameters

*filter*
:   a custom filter object implementing [ICustomFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ICustomFilter.html)

#### Return Value

\* [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s matching given custom filter. \* All [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
