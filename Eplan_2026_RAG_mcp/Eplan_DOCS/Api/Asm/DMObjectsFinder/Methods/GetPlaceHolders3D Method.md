# GetPlaceHolders3D Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlaceHolders3D.html

---

Returns all [Eplan.EplApi.DataModel.E3D.PlaceHolder3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D.html) from project.

Syntax

**C#**



public PlaceHolder3D[] GetPlaceHolders3D( 

   PlaceHolders3DFilter pFilter

)

public:

array<PlaceHolder3D^>^ GetPlaceHolders3D( 

   PlaceHolders3DFilter^ pFilter

)


#### Parameters

*pFilter*
:   Filter used to customizate search results. Can be `null`.

#### Return Value

Array of found 3d place holders.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
