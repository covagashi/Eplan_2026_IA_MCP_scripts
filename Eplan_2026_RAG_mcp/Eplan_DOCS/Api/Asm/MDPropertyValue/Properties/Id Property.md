# Id Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Id.html

---

Returns P8-Property descriptor (id and index) of the object.  
Offline MDPropertyValue objects don't have descriptors because they point to value directly. An offline MDPropertyValue is created by operators that take base types values.

Syntax

**C#**



public MDAnyPropertyId Id {get;}

public:

property MDAnyPropertyId^ Id {

   MDAnyPropertyId^ get();

}


Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown when object is offline. |

Example

- [c#](#i-tab-content-71c3cf6b-c9e8-46f9-8bf4-aa992b54e3d3)

```
MDPropertyValue pV = "123";	// Offline object

MDPropertyValue pV2= 12;	// Offline object

MDPropertyValue pV3 = same_parts_database.Part[0].Properties[ Eplan.EplApi.MasterData.Properties.MDPartsDatabaseItem.SAME_PROPERTY /* property id */ ];

//pV3.Id == Eplan.EplApi.MasterData.Properties.MDPartsDatabaseItem.SAME_PROPERTY

// In this case, where index wasn't specified, pV3.Id.Index is 0.

MDPropertyValue pV4 = same_parts_database.Part[0].Properties[ Eplan.EplApi.MasterData.Properties.MDPartsDatabaseItem.SAME_PROPERTY /* property id */ , 1  /* property index */ ];

//pV4.Id == Eplan.EplApi.MasterData.Properties.MDPartsDatabaseItem.SAME_PROPERTY

//pV4.Index == 1

int propertyId	  = pV4.Id.Id;

int propertyIndex = pV4.Id.Index;
```
