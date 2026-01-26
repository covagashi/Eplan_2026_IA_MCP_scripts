# Pins Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Pins.html

---

Gets/Sets an array of the function's connection points.

Syntax

**C#**



public Pin[] Pins {get; set;}

public:

property array<Pin^>^ Pins {

   array<Pin^>^ get();

   void set (    array<Pin^>^ value);

}


#### Property Value

Array of [Pin](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin.html) objects.

Exceptions

| Exception | Description |
| --- | --- |
| [IncorrectObjectTypeException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IncorrectObjectTypeException.html) | Thrown when trying to create new Pins array on invalid Function |

Remarks

For functions with variable pins (conn. points) count, setting this property may change the actual count of the function's pins. In other cases, exception of IncorrectObjectTypeException type is thrown.
