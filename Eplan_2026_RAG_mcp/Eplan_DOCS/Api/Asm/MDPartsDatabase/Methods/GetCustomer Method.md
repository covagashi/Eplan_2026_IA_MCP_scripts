# GetCustomer Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetCustomer.html

---

Gets a customers that ist stored in the parts database.

Syntax

**C#**



public MDAddress GetCustomer( 

   string shortName

)

public:

MDAddress^ GetCustomer( 

   String^ shortName

)


#### Parameters

*shortName*
:   The short name of the customer that is searched.

Remarks

returns null, if the customer is not found.
