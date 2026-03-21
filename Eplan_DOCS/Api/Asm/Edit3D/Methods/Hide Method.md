# Hide Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit3D~Hide.html

---

Makes a 3d object invisible in opened 3d graphic editor view.

Syntax

**C#**



public void Hide( 

   Placement3D pPlacement3D

)

public:

void Hide( 

   Placement3D^ pPlacement3D

)


#### Parameters

*pPlacement3D*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Is thrown when parameter is `null`. |
| [System.ArgumentException](#) | Is thrown when parameter is invalid. |
| [System.ApplicationException](#) | Is thrown if the current license does not allow the execution of this task. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | If internal error has occured. Please check exception message. |
