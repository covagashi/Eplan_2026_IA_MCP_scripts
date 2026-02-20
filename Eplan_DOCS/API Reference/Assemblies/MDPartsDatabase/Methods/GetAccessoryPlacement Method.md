# GetAccessoryPlacement Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetAccessoryPlacement.html

---

Gets a accessory placement with the given name that is stored in the parts database.

Syntax

**C#**



public MDAccessoryPlacement GetAccessoryPlacement( 

   string name

)

public:

MDAccessoryPlacement^ GetAccessoryPlacement( 

   String^ name

)


#### Parameters

*name*
:   The name of the accessory placement that is searched.

Remarks

Returns the found accessory placement (MDAccessoryPlacement object) - otherwise null, if the accessory list is not found
