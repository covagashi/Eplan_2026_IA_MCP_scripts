# GetAccessoryList Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetAccessoryList.html

---

Gets a accessory list with the given name that is stored in the parts database.

Syntax

**C#**



public MDAccessoryList GetAccessoryList( 

   string name

)

public:

MDAccessoryList^ GetAccessoryList( 

   String^ name

)


#### Parameters

*name*
:   The name of the accessory list that is searched.

Remarks

Returns the found accessory list (MDAccessoryList object) - otherwise null, if the accessory list is not found
