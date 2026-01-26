# ToDataModelIdentifier Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~ToDataModelIdentifier.html

---

Returns data model identifier which identifies this object.

Syntax

**C#**



public string ToDataModelIdentifier()

public:

String^ ToDataModelIdentifier();


#### Return Value

the data model identifier

Remarks

The string is valid only during current connection to database is opened. When the database to which the object belongs to is closed, the string gets invalid.

Value of this string is generated in runtime and contains data which are used by EPLAN to identify the object and its source.
