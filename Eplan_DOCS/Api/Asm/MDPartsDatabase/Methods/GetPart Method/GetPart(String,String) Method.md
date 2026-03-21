# GetPart(String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetPart(String,String).html

---

Gets the part with the given part number and variant

Syntax

**C#**



public MDPart GetPart( 

   string partNr,

   string variant

)

public:

MDPart^ GetPart( 

   String^ partNr,

   String^ variant

)


#### Parameters

*partNr*


*variant*

Remarks

Returns null, if there is no part with that part number and variant found in the database
