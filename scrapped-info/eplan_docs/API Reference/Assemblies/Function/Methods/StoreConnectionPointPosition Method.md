# StoreConnectionPointPosition Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~StoreConnectionPointPosition.html

---

Stores data from connection point position in function under given index.

Syntax

**C#**



public void StoreConnectionPointPosition( 

   ConnectionPointPosition pConnectionPointPosition,

   short iIndex

)

public:

void StoreConnectionPointPosition( 

   ConnectionPointPosition^ pConnectionPointPosition,

   short iIndex

)


#### Parameters

*pConnectionPointPosition*


*iIndex*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when parameter is `null`. |
| [System.ArgumentException](#) | Thrown when `iIndex` value is less then `0`. |

Remarks

Index starts from 0.

If [AreConnectionPointPositionsLocal](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~AreConnectionPointPositionsLocal.html) is set to false, only values of Name and DeviceTag of [ConnectionPointPosition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointPosition.html) are stored.
