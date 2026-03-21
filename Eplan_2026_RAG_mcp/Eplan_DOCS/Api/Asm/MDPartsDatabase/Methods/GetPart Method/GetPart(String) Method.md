# GetPart(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetPart(String).html

---

Gets the part with the given part number. If there are several variants of that part, the first one is taken. First means, that if you sort that parts by their variant that the topmost variant is taken.

Syntax

**C#**



public MDPart GetPart( 

   string sPartNr

)

public:

MDPart^ GetPart( 

   String^ sPartNr

)


#### Parameters

*sPartNr*

Remarks

Returns null, if there is no part with that part number found in the database

Example

If the database contains the parts: "PartA"-"V4", "PartA"-"V1", "PartA"-"V2", "PartA"-"V3" than GetPart("PartA") returns "PartA"-"V1"
