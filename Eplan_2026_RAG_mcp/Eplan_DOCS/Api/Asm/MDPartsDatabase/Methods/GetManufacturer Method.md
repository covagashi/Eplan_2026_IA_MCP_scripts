# GetManufacturer Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetManufacturer.html

---

Gets a manufacturer with the given name that is stored in the parts database.

Syntax

**C#**



public MDAddress GetManufacturer( 

   string shortName

)

public:

MDAddress^ GetManufacturer( 

   String^ shortName

)


#### Parameters

*shortName*
:   The short name of the manufacturer that is searched.

Remarks

Returns the found manufacturer (MDAddress object) - otherwise null, if the manufacturer is not found.
