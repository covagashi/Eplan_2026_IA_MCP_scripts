# AddManufacturer Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~AddManufacturer.html

---

Adds a new manufacturer to the parts data

Syntax

**C#**



public MDAddress AddManufacturer( 

   string shortName

)

public:

MDAddress^ AddManufacturer( 

   String^ shortName

)


#### Parameters

*shortName*
:   The short name of the manufacturer will be added.

Exceptions

| Exception | Description |
| --- | --- |
|  | If manufacturer already exists. |

Remarks

The short name has to be unique in the manufacture list of the parts database.
