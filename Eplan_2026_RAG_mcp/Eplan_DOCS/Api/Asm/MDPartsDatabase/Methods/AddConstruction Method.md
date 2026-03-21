# AddConstruction Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~AddConstruction.html

---

Adds a new construction to the parts database

Syntax

**C#**



public MDConstruction AddConstruction( 

   string name

)

public:

MDConstruction^ AddConstruction( 

   String^ name

)


#### Parameters

*name*
:   The name of the construction will be added.

Exceptions

| Exception | Description |
| --- | --- |
|  | If construction already exists. |

Remarks

The name has to be unique in the construction list of the parts database.
