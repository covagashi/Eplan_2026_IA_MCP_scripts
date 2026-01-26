# Shielding Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint~Shielding.html

---

Returns the shielding of the connection.

Syntax

**C#**



public Function Shielding {get;}

public:

property Function^ Shielding {

   Function^ get();

}


#### Property Value

Shielding of the function

`null` when shielding does not exist.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when it is impossible to read the shielding. |
