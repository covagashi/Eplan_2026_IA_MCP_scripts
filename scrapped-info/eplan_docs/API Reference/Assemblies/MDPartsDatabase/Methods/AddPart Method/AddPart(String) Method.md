# AddPart(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~AddPart(String).html

---

Adds a new part into the parts database. That part will get the default-variant: "1" If it's not possible (because there is already a part with that partnr and variant) an MDInvalidArgumentException will be thrown

Syntax

**C#**



public MDPart AddPart( 

   string sPartNr

)

public:

MDPart^ AddPart( 

   String^ sPartNr

)


#### Parameters

*sPartNr*

Exceptions

| Exception | Description |
| --- | --- |
|  | If part already exists. |

Remarks

Returns the part object of the created part.
