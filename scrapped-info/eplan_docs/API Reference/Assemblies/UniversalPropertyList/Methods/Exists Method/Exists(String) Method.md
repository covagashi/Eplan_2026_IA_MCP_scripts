# Exists(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Exists(String).html

---

Checks property existence for used object.

Syntax

**C#**



public bool Exists( 

   string strIdentName

)

public:

bool Exists( 

   String^ strIdentName

)


#### Parameters

*strIdentName*
:   Identifying name of property. Can't be `null` or `empty`.

#### Return Value

Returns true if given property exists for used object otherwise false.

Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown when list is not connected with valid database object. |
| [System.ArgumentNullException](#) | Thrown when parameter is null. |
| [System.ArgumentException](#) | Thrown when parameter is empty. |
