# AddAccessoryPlacement Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~AddAccessoryPlacement.html

---

Adds a new accessory placement to the parts database

Syntax

**C#**



public MDAccessoryPlacement AddAccessoryPlacement( 

   string name

)

public:

MDAccessoryPlacement^ AddAccessoryPlacement( 

   String^ name

)


#### Parameters

*name*
:   The name of the accessory placement that will be added.

Exceptions

| Exception | Description |
| --- | --- |
|  | If accessory placement already exists. |

Remarks

The name has to be unique in the accessory placement list of the parts database
