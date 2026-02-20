# GetPartVariants Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetPartVariants.html

---

Gets all part variants with the given part number.

Syntax

**C#**



public MDPart[] GetPartVariants( 

   string sPartNr

)

public:

array<MDPart^>^ GetPartVariants( 

   String^ sPartNr

)


#### Parameters

*sPartNr*

Remarks

The parts are sorted by the variant name

Example

If the database contains the parts: "PartA"-"V4", "PartA"-"V1", "PartA"-"V2", "PartA"-"V3" than GetPartVariants("PartA") returns "PartA"-"V1", "PartA"-"V2", "PartA"-"V3", "PartA"-"V4"
