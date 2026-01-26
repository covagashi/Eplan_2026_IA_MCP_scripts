# GetFunctions3D Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetFunctions3D.html

---

Returns [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)s matching given filter.

Syntax

**C#**



public Function3D[] GetFunctions3D( 

   Functions3DFilter filter

)

public:

array<Function3D^>^ GetFunctions3D( 

   Functions3DFilter^ filter

)


#### Parameters

*filter*
:   a [Functions3DFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Functions3DFilter.html), can be `null`

#### Return Value

\* [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)s matching given [Functions3DFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Functions3DFilter.html). \* All [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)s if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |

Remarks

The result does not contain [Eplan.EplApi.DataModel.E3D.InstallationSpace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.InstallationSpace.html).  
  
To get all objects of specific Function3D class please use [GetAll<T>](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetAll.html) method.
