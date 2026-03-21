# StoreToObject Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointPosition~StoreToObject.html

---

Stores data from connection point position.

Syntax

**C#**



public void StoreToObject()

public:

void StoreToObject();


Remarks

If `AreConnectionPointPositionsLocal` of parent is set to false, only values of [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointPosition~Name.html) and [DeviceTag](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointPosition~DeviceTag.html) of [ConnectionPointPosition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointPosition.html) are stored.

For some function definitions it makes no sense to store some information. This method will not throw an exception if some properties are not stored for this reason. For example changing side of connection point will not make effect for non-terminal.
