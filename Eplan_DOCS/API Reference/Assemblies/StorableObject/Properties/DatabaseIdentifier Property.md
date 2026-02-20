# DatabaseIdentifier Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~DatabaseIdentifier.html

---

Returns the project as number. The number is unique for all open projects in one session. The number changes when the project is closed and opened again.

Syntax

**C#**



public uint DatabaseIdentifier {get;}

public:

property uint DatabaseIdentifier {

   uint get();

}


#### Property Value

the number of the project (database id)

Exceptions

| Exception | Description |
| --- | --- |
| [DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | Thrown when the object is invalid. |

Remarks

The string is valid during runtime only. When the project the object belongs to is closed, the number gets invalid.
