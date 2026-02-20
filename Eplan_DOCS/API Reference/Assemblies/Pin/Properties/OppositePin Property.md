# OppositePin Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~OppositePin.html

---

Gets/Sets the potential forwarding for connections of the same function or connections of different functions of the same device.

Syntax

**C#**



public Pin[] OppositePin {get; set;}

public:

property array<Pin^>^ OppositePin {

   array<Pin^>^ get();

   void set (    array<Pin^>^ value);

}


Remarks

Returns `NULL` if this Pin object has been obtained from a FunctionDefinition object.
