# ToStringIdentifier Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html

---

Returns this object as string identifier.

Syntax

**C#**



public string ToStringIdentifier()

public:

String^ ToStringIdentifier();


#### Return Value

the string identifier

Exceptions

| Exception | Description |
| --- | --- |
| [DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | Thrown when the object is invalid. |

Remarks

The string is valid during runtime only. When the project the object belongs to is closed, the string gets invalid.
