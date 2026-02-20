# TryParseIdentifier(String,UInt16,StorableObject) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TryParseIdentifier(String,UInt16,StorableObject).html

---

Returns this object created from the string identifier for the databaseid newDbId.

Syntax

**C#**



public static bool TryParseIdentifier( 

   string strObj,

   ushort newDbId,

   ref StorableObject resultObj

)

public:

static bool TryParseIdentifier( 

   String^ strObj,

   ushort newDbId,

   StorableObject^% resultObj

)


#### Parameters

*strObj*
:   The string identifier for the object. This string has to be created with the ToString() function.

*newDbId*
:   The databaseId, this can change when the project is closed and opened again.

*resultObj*
:   The storable object

#### Return Value

true when the object was created successfully

Remarks

The string is valid during runtime only. When the project the object belongs to is closed, the string gets invalid.
