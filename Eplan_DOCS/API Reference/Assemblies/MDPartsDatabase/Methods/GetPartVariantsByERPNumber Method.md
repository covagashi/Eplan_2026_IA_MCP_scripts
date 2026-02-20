# GetPartVariantsByERPNumber Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetPartVariantsByERPNumber.html

---

Gets all part variants with the given ERP number.

Syntax

**C#**



public MDPart[] GetPartVariantsByERPNumber( 

   string sERPNr

)

public:

array<MDPart^>^ GetPartVariantsByERPNumber( 

   String^ sERPNr

)


#### Parameters

*sERPNr*

Remarks

The parts are sorted by part number and variant name

Example

If the database contains the 2 parts each with 2 variants: "PartA"-"V1" and "PartA"-"V2" with ERP-Number "1", "PartB"-"V1" and "PartB"-"V2" with ERP-Number "2" then GetPartVariantsByERPNumber("1") returns "PartA"-"V1" and "PartA"-"V2".
