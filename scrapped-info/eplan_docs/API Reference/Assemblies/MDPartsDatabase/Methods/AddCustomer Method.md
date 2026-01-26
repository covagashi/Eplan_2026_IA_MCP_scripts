# AddCustomer Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~AddCustomer.html

---

Adds a new customer to the parts database.

Syntax

**C#**



public MDAddress AddCustomer( 

   string shortName

)

public:

MDAddress^ AddCustomer( 

   String^ shortName

)


#### Parameters

*shortName*
:   The short name of the customer will be added.

Exceptions

| Exception | Description |
| --- | --- |
|  | If customer already exists. |

Remarks

The short name has to be unique in the Customers List of the parts database.
