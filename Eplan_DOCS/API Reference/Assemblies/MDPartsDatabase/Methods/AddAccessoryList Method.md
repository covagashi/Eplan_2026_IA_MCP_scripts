# AddAccessoryList Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~AddAccessoryList.html

---

Adds a new accessory list to the parts database

Syntax

**C#**



public MDAccessoryList AddAccessoryList( 

   string name

)

public:

MDAccessoryList^ AddAccessoryList( 

   String^ name

)


#### Parameters

*name*
:   The name of the accessory list that will be added.

Exceptions

| Exception | Description |
| --- | --- |
|  | If accessory list already exists. |

Remarks

The name has to be unique in the accessory list list of the parts database
