# ObjectIdentifier Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ObjectIdentifier.html

---

Returns the object identifier as number. The number is unique for all objects of this type.

Syntax

**C#**



public long ObjectIdentifier {get;}

public:

property int64 ObjectIdentifier {

   int64 get();

}


#### Property Value

the number of the object.

Exceptions

| Exception | Description |
| --- | --- |
| [DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | Thrown when the object is invalid. |

Remarks

The number may be reused when an object is deleted and created again.
