# StoreConnectionPointPosition Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~StoreConnectionPointPosition.html

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
