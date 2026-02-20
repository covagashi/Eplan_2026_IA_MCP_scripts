# ConnectionDefPoints Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~ConnectionDefPoints.html

---

Returns the [ConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html) related to this connection.

Syntax

**C#**



public ConnectionDefinitionPoint[] ConnectionDefPoints {get;}

public:

property array<ConnectionDefinitionPoint^>^ ConnectionDefPoints {

   array<ConnectionDefinitionPoint^>^ get();

}


#### Property Value

An array of [ConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html)s related to this connection.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when it is impossible to read ConnectionDefinitionPoints. |

Remarks

It is necessary to update connections in order to fill this property after creating or setting logical area to Cable.
