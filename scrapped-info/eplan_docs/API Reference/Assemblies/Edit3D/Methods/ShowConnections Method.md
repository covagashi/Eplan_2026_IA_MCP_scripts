# ShowConnections Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit3D~ShowConnections.html

---

Makes 3d connections visible in opened 3d graphic editor view.

Syntax

**C#**



public void ShowConnections( 

   IEnumerable<Connection3D> colConnections

)

public:

void ShowConnections( 

   IEnumerable<Connection3D^>^ colConnections

)


#### Parameters

*colConnections*
:   Connections which will be drawn in GED.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Is thrown when parameter is `null`. |
| [System.ApplicationException](#) | Is thrown if the current license does not allow the execution of this task. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | If internal error has occured. Please check exception message. |
