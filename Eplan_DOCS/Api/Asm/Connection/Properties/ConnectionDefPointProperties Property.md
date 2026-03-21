# ConnectionDefPointProperties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~ConnectionDefPointProperties.html

---

Allows to access properties of a [ConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html) assigned to this Connection. If there are more then one [ConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html) assigned to this Connection, an exception is thrown. Such situation has to be handled by calling [ConnectionDefPoints](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~ConnectionDefPoints.html) and analyze of the result.

Syntax

**C#**



public ConnectionDefinitionPointPropertyList ConnectionDefPointProperties {get;}

public:

property ConnectionDefinitionPointPropertyList^ ConnectionDefPointProperties {

   ConnectionDefinitionPointPropertyList^ get();

}


#### Property Value

Cable definition related to this Connection.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Different count than 1 [ConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html) related to this Connection. |

Remarks

It is necessary to update connections in order to fill this property after creating or setting logical area to Cable.
