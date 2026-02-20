# GetConstruction Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetConstruction.html

---

Gets a construction with the given name that is stored in the parts database.

Syntax

**C#**



public MDConstruction GetConstruction( 

   string name

)

public:

MDConstruction^ GetConstruction( 

   String^ name

)


#### Parameters

*name*
:   The name of the construction that is searched.

Remarks

Returns the found construction (MDConstruction object) - otherwise null, if the construction is not found.
