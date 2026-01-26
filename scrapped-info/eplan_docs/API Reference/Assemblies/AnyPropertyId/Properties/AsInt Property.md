# AsInt Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AnyPropertyId~AsInt.html

---

Integer number of this property. When setting a property by number, be aware, that the property might not exist for the object.

Syntax

**C#**



public int AsInt {get; set;}

public:

property int AsInt {

   int get();

   void set (    int value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [PropertyNotFoundException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyNotFoundException.html) | Thrown when property was not found. |
